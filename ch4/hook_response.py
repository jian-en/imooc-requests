# -*- coding: utf-8 -*-
import requests


def get_key_info(response, *args, **kwargs):
    """回调函数
    """
    print response.headers['Content-Type']


def main():
    """主程序
    """
    requests.get('https://api.github.com', hooks=dict(response=get_key_info))

main()
