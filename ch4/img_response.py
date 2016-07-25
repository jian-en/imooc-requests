# -*- coding: utf -*-
import requests


def download_image():
    """demo: 下载图片, 文件
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
    url = "http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg"
    response = requests.get(url, headers=headers, stream=True)
    with open('demo.jpg', 'wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)


def download_image_improved():
    """demo: 下载图片
    """
    # 伪造headers信息
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'}
    # 限定url
    url = "http://img3.imgtn.bdimg.com/it/u=2228635891,3833788938&fm=21&gp=0.jpg"
    response = requests.get(url, headers=headers, stream=True)
    from contextlib import closing
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open('demo1.jpg', 'wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)

download_image_improved()
