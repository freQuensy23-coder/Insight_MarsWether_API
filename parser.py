import os
import requests as req
import json
import logging
import datetime
import time

API_KEY = os.getenv("nasa_api_key")


# API_KEY = os.getenv("nasa_demo_key")


def make_request():
    """Making requests to NASA's api. If some error occured try again and log. Returns dict"""
    request_mask = "https://api.nasa.gov/insight_weather/?api_key={key}&feedtype=json&ver=1.0".\
                    format(key=API_KEY)
    while True:
        try:
            r = req.get(request_mask)

            if r.status_code != 200:
                logging.critical("Exception occurred while sending requests." +
                                 "Requests status code is  {status}".format(status=r.status_code),
                                 exc_info=True)
            else:
                # If everything is good (No ex. and r.status = 200) log info that req is successful
                logging.info(
                    "Made successful request to nasa server."
                )
                logging.debug(
                    "Nasa server request's answer: {answer}".format(answer=r.json())
                )
                break

        except req.exceptions.ConnectTimeout:
            logging.error("Exception occurred while sending requests. Connecting time out.",
                          exc_info=True)
        except req.exceptions.ConnectionError:
            logging.error("Exception occurred while sending requests. Nasa server is not responding.",
                          exc_info=True)
        except:
            logging.error("Some other exception occurred wile sending requests to nasa api.",
                          exc_info=True)

        time.sleep(60 * 35)  # Sleep for 35 mins if something going wrong
    return r.json()


def save_to_DB(dictionary: dict):
    """Save dict with data to mysql DB"""
    #
    # def prettify_data(data: dict):
    #     """ """
    #     # TODO: Add docs
    #     result = {}
    #
    #     def represents_number(string):
    #         try:
    #             int(string)
    #             return True
    #         finally:
    #             return False
    #
    #     # TODO Add logging and try except block
    #
    #     keys = list(data.keys())
    #     for key in keys:
    #         if represents_number(key):
    #             result[key] = data[key]
    #         else:
    #             # If it is not sol data, but validity check we should get all sols checks and add it to result
    #             if key == "validity_checks":
    #
    #                 for k in list(result.keys()):
    #                     # All sols should have required hours to check validity
    #                     result[k]["validity_checks"]["sol_hours_required"] = \
    #                         data["validity_checks"]["sol_hours_required"]
    #
    #                 for sol_valid_check_num in list(data["validity_checks"].keys()):
    #                     # Check all validity_checks and add them to their sols
    #                     if represents_number(sol_valid_check_num):
    #                         result[sol_valid_check_num]["validity_checks"] = \
    #                             data["validity_checks"][sol_valid_check_num]
    #     return result


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    requests_json = make_request()

    print(requests_json)
