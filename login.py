#!/user/bin/python
#-*- coding:utf-8 -*-


import requests
import json


def login():
    url = "http://content.test.17zuoye.net/search/api/auth/login"
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {"username": "15811431882", "password": "Spp19930715"}

    response = requests.post(url, json=data, headers=headers)
    result=response.json()
    #print(response.json())
    #print(type(result))
    #print(result.get('success'))
    cook = response.cookies
    return result,cook

if __name__ == '__main__':
    print(login())

