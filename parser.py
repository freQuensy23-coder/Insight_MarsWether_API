import os
import requests as req
import json
import logging
import datetime
import time
from db import DB
from Nasa_api import Nasa_API

API_KEY = os.getenv("nasa_api_key")
nasa_API = Nasa_API(key=API_KEY)


def save_to_DB(dictionary: dict):
    """Save dict with data to mysql DB"""


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    requests_json = nasa_API.make_request()

    print(requests_json)
