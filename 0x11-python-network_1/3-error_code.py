#!/usr/bin/python3
"""sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            utf8_body = body.decode('utf-8')
            print(utf8_body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
