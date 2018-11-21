import os
import sys
import urllib.request
import json

def translate(eng):
    client_id = "8NAS73nvqmTR0aI6FkfN"
    client_secret = "R4fbBeuWxV"
    data = "source=en&target=ko&text=" + eng
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        json_data = json.loads(response_body)
        return json_data['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)