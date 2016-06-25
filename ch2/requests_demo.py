# -*- coding: utf-8 -*-
import requests

URL_IP = 'http://localhost:8000/ip'
URL_GET = 'http://localhost:8000/get'


def use_simple_requests():
    response = requests.get(URL_IP)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Response body:'
    print response.text


def use_params_requests():
    params = {'param1': 'hello', 'param2': 'world'}
    response = requests.get(URL_GET, params=params)
    print '>>>>Response Headers:'
    print response.headers
    print '>>>>Status Code:'
    print response.status_code
    print '>>>>Reason:'
    print response.reason
    print '>>>>Request body:'
    print response.text

if __name__ == '__main__':
    print '>>>Use simple requests:'
    use_simple_requests()
    print ''
    print '>>>Use params requests:'
    use_params_requests()
