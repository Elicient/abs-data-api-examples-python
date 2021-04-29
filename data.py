from config import api_base_url
import json
from time import sleep


def meta(client):
    """ Lists all available cubes from the API.

    :param client: The authenticated client to be used when making requests to the API
    :return: An array of available cubes
    """
    result = client.get(f"{api_base_url}/meta")
    return result.json()["cubes"]

def load(client, query):
    """
    Synchronously executes the query on the server and returns the results as an array of dictionaries
    :param client: The authenticated client to be used when making requests to the API
    :param query: The query to be executed
    :return: The query results, as an array of dictionaries
    """
    result = __get_query(client, query)
    contents = result.json()

    while result.ok and "error" in contents and contents["error"] == "Continue wait":
        sleep(2)
        result = __get_query(client, query)
        result.raise_for_status()
        contents = result.json()

    if not result.ok:
        print(contents)
        raise ValueError("Data API request was not successful")

    return contents["data"]


def __get_query(client, query):
    return client.get(f"{api_base_url}/load", params={"query": json.dumps(query)})
