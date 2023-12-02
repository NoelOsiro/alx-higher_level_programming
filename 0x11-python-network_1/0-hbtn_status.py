#!/usr/bin/python3
""" Get status in https://intranet.hbtn.io"""
import urllib.request


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    with urllib.request.urlopen(
            urllib.request.Request(
                'https://intranet.hbtn.io/status',
                headers=headers)) as response:
        html = response.read()
        print("Body response:$")
        print("\t- type: {}\n\t- content: {}".format(type(html), html))
        print("\t- utf8 content: {}".format(html.decode('UTF-8')))
