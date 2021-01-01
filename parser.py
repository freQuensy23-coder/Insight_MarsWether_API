import os
import logging
import time
from db import DB
from Nasa_api import Nasa_API

logger = logging.getLogger("parser")
logging.basicConfig(level=logging.DEBUG)

API_KEY = os.getenv("nasa_api_key")
nasa_API = Nasa_API(key=API_KEY)

db = DB(file_name="data.sqlite")


if __name__ == '__main__':
    today = int(time.time() / 3600 / 24)
    logger.info(f"Parser started at {time.time()}, {today} from unix era started")

    requests_json = nasa_API.make_request()
    logger.info(f"Parser get json with data form nasa. Requests json: {requests_json}")

    db.add_new_day_info(day=today, info=repr(requests_json))
    logger.info("Parser save json to db")

    logger.info("Parser stops. That is all for today.")
