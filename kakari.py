import urllib

appid = "hogehoge"
sentence = "u庭には二羽鳥がいる。"
postdata = {
        "appid": appid,
        "sentence": sentence
        }
params = urllib.urlencode(postdata)

url = "http://jlp.yahooapis.jp/DAService/V1/parse"
result = urllib.urlopen(url, params)

print(result.read())
