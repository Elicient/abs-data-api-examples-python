from os import path

"""Path where your credentials will be saved so you do not need to re-authenticate each time"""
secrets_path = path.expanduser("~")
"""Name of file where your credentials will be saved so you do not need to re-authenticate each time"""
secrets_filename = ".elicient_secrets"

"""Id of client used for authentication.  Provided to you by elicient."""
client_id = "CxZJH3ByyiUCB1fBkC03hnPAGNhnQzm0"

"""Location of elicient's authentication server"""
oauth_base_url = "https://login.elicient.com"

"""Audience required for token to authenticate to the data API"""
oauth_audience = "https://data.elicient.com"

"""API base url for making requests"""
api_base_url = "https://data.elicient.com/abs/v1"
