import os
import requests

UW_API_KEY = os.environ.get('UW_API_KEY', None)


class APIKeyMissingError(Exception):
    pass

if UW_API_KEY is None:
    raise APIKeyMissingError(
        "Missing: UW_API_KEY"
        "All methods require an API Key. "
        "Refer to https://uwaterloo.ca/api/ "
        "For how to register for an API key."
    )

session = requests.Session()
session.params = {'key': UW_API_KEY}

from .uwaterloodriver import UW_Driver
