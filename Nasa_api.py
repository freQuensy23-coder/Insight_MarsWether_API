import requests as req
import logging as log
import time

logging = log.getLogger("Nasa_API")


class Nasa_API:
    def __init__(self, key):
        self.api_key = key

    def make_request(self):
        """Making requests to NASA's api. If some error occured try again and log. Returns dict"""
        request_mask = "https://api.nasa.gov/insight_weather/?api_key={key}&feedtype=json&ver=1.0". \
            format(key=self.api_key)
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
            except Exception as e:
                logging.error(f"Some other exception occurred wile sending requests to nasa api. {e}",
                              exc_info=True)

            time.sleep(60 * 35)  # Sleep for 35 mins if something going wrong
        return r.json()
