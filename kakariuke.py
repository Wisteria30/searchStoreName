# -*- coding: utf-8 -*-
import requests
import bs4
from xml.etree.ElementTree import *
import sys


def POST(body):
    request_URL = "https://jlp.yahooapis.jp/DAService/V1/parse"
    parameter = {"appid": "", "sentence": body}
    r = requests.get(request_URL, params=parameter)
    # print(parameter)
    yield (r, r.text)


def XML_parse(body):
    elem = fromstring(body)
    for e in elem.getiterator("{urn:yahoo:jp:jlp:DAService}surface"):
        print(e.text.encode("utf-8"))


if __name__ == "__main__":
    # with open("./yahoo.key") as f:
    #    appid = f.read()
    # print(appid)
    for response in POST(body=u"うちの庭には二羽鶏がいます。"):
        r = response[0]
        text = response[1]
        # print(text.encode("utf-8").decode("unicode-escape"))
        print(bs4.BeautifulSoup(text, "xml"))
    # XML_parse(text.encode("utf-8"))#encodeしないとUnicode-error

