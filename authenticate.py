import json
import sys
import webbrowser
from os import path
from time import sleep

import requests
from requests_oauthlib import OAuth2Session

import config


def get_authenticated_client(persist=True):
    """ Gets a client that may be used to make authenticated requests to elicient's data API

    :param persist: Indicates whether credentials should be persisted to the local device (default is True)
    :return: A client that may be used to make authenticated requests
    """
    token = __get_token(persist)
    return OAuth2Session(config.client_id, token=token, auto_refresh_url=f"{config.oauth_base_url}/oauth/token",
                         auto_refresh_kwargs={"client_id": config.client_id})


def __get_token(persist):
    try:
        secrets_file = open(path.join(config.secrets_path, config.secrets_filename), "r")
        refresh_token = json.loads(secrets_file.read())['refresh_token']
        refresh_token_request = requests.post(url=f"{config.oauth_base_url}/oauth/token",
                                              data={"client_id": config.client_id, "grant_type": "refresh_token",
                                                    "refresh_token": refresh_token}).json()
        return {
            "access_token": refresh_token_request["access_token"],
            "refresh_token": refresh_token,
            "token_type": refresh_token_request["token_type"],
            "expires_in": refresh_token_request["expires_in"]
        }
    except:
        pass

    verify_response = requests.post(url=f"{config.oauth_base_url}/oauth/device/code",
                                    data={"client_id": config.client_id, "scope": "offline_access",
                                          "audience": config.oauth_audience}).json()
    webbrowser.open(verify_response['verification_uri_complete'])
    print(f"Confirm the code in your browser matches {verify_response['user_code']}")
    verify_success = False
    verify_interval = float(verify_response['interval'])
    while (not verify_success):
        sleep(verify_interval)
        token_request = requests.post(url=f"{config.oauth_base_url}/oauth/token",
                                      data={"grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                                            "device_code": verify_response['device_code'], "client_id": config.client_id})
        verify_success = token_request.ok
        token_request_data = token_request.json()

        if "error" in token_request_data and token_request_data["error"] != "authorization_pending":
            print(f"Could not authorize: {token_request_data['error_description']}")
            sys.exit(-1)

    if persist:
        secrets_file = open(path.join(config.secrets_path, config.secrets_filename), "w")
        secrets_file.write(json.dumps({"refresh_token": token_request_data['refresh_token']}))
        secrets_file.close()

    return token_request_data
