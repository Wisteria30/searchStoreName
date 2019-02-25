# -*- coding: utf-8 -*-
import requests
from xml.etree.ElementTree import *
import sys


def POST(body):
    request_URL = "http://jlp.yahooapis.jp/MAService/V1/parse"

    parameter = {"appid": "hogehoge", "sentence": body, "results": "ma"}
    r = requests.get(request_URL, params=parameter)
    print(parameter)
    yield (r, r.text)


def XML_parse(body):
    elem = fromstring(body)
    for e in elem.getiterator("{urn:yahoo:jp:jlp}surface"):
        print(e.text)


if __name__ == "__main__":
    # with open("./yahoo.key") as f:
    #    appid = f.read()
    # print(appid)
    for response in POST(body=sys.argv[1]):
        r = response[0]
        text = response[1]
    print(text)
    XML_parse(text.encode("utf-8"))  # encodeしないとUnicode-error
