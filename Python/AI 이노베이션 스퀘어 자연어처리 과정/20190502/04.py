import requests
import json
from urllib import request, error, parse

#header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}

def download(url, params={}, retries=3):
    resp = None

    try:
        resp = requests.get(url, params=params) #headers = header)
        #resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= e.response.status_code < 600 and retries > 0:
            print(retries)
            resp = download(url, params, retries - 1)
        else:
            print(e.response.status_code, "\n")
            print(e.response.reason, "\n")
            print(e.request.headers, "\n")

    return resp

url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

params = {
    "serviceKey":"SOiHe0eIo6uoLf60XK0keAAwBXmx33hU4bEEdZZ0rYoCbbWRYswGsk2JdpJsUcHRQbvdp0ACEbmu5YcpfiJcKw%3D%3D",
    "numOfRows":10,
    "pageNo":1,
    "sidoName":"",
    "ver":"1.3",
    "_returnType":"json"
}

print(params["serviceKey"])

result = download(url, params)

from requests.utils import quote, unquote

params["serviceKey"] = unquote(params["serviceKey"])
print(params["serviceKey"])
result = json.loads(result.text)
print(result)