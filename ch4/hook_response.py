# -*- coding: utf-8 -*-
import requests


def get_key_info(response, *args, **kwargs):
    print response.headers['Content-Type']


def main():
    requests.get('https://www.baidu.com', hooks=dict(response=get_key_info))

main()
