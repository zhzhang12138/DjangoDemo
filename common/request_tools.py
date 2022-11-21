# -*- coding:utf-8 -*-
# @FileName  :request_tools.py
# @Time      :2022/11/17 16:43
# @Author    :John Doe
import requests


def server_requests(method, url, data=None, files=None, multipart=False, root_path=None, headers=None):
    upper_method = method.upper()
    absolute_url = root_path + url
    if multipart:
        response = requests.request(method=upper_method, url=absolute_url, data=data, files=files, headers=headers)
    else:
        response = requests.request(method=upper_method, url=absolute_url, json=data, headers=headers)
    return response
