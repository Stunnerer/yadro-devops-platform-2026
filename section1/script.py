import http.client
import urllib.parse
import logging
import json

URL = "https://httpbin.org/status/{}"


def check_response(url):
    parts = urllib.parse.urlparse(url)
    if parts.scheme == "https":
        client = http.client.HTTPSConnection(parts.hostname)
    else:
        client = http.client.HTTPConnection(parts.hostname)
    client.request("GET", url)
    response = client.getresponse()
    response_code = response.status
    if 100 <= response_code <= 399:
        response_headers = dict(response.getheaders())
        body = response.read()
        logging.info(
            f"request to {url} succeeded: {response_code} {http.HTTPStatus(response_code).phrase}"
        )
        logging.info(f"body: {body}")
        logging.info(f"headers: {json.dumps(response_headers)}")
    else:
        raise http.client.HTTPException(
            f"Invalid response code for url {url}: {response_code} {http.HTTPStatus(response_code).phrase}"
        )


def main():
    logging.basicConfig(level=logging.INFO)
    for i in [101, 200, 302, 404, 502]:
        req_url = URL.format(i)
        try:
            check_response(req_url)
        except http.client.HTTPException as e:
            logging.error(e)

if __name__ == "__main__":
    main()
