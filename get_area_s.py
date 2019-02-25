import json
import requests

with open("area_s.json") as f:
    jsonData = json.load(f)

area_s_list = [i["areacode_s"] for i in jsonData["garea_small"]]


def post(areacode_s, offset):
    request_URL = "https://api.gnavi.co.jp/RestSearchAPI/v3/"

    parameter = {
        "keyid": "4d3bba864a562b13280648a4922bcba0",
        "areacode_s": areacode_s,
        "hit_per_page": 100,
        "offset": offset,
    }
    r = requests.get(request_URL, params=parameter)
    return r.text


if __name__ == "__main__":
    i = 1
    hit_per_page = 100
    store_names = []
    area = "AREAS4503"

    while True:
        text = post(area, i)
        if i == 1:
            total_hit_count = int(text["total_hit_count"])
        print(i * hit_per_page)
        store_names.extend([i["name"] for i in text["rest"]])
        if i * hit_per_page >= total_hit_count:
            break
        i += 1

print(store_names)
# shopname = [POST(i) for i in area_s_list]
# with open("area_name.json", "w") as f:
#     f.write("[")
#     [f.write("'" + i + "'," + "\n") for i in area_s_list]
#     f.write("]")
