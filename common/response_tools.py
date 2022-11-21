# -*- coding:utf-8 -*-
# @FileName  :response_tools.py
# @Time      :2022/11/17 16:43
# @Author    :John Doe
from rest_framework.renderers import JSONRenderer
import json
from collections import OrderedDict


def jsonify_response_content(response):
    if 200 <= response.status_code < 500:
        data = json.loads(response.content.decode(), object_pairs_hook=OrderedDict)
    else:
        data = response.content
    response.data = data
    return response


class Response(JSONRenderer):
    """ 自定义返回数据 Json格式
    {
        "code": 0,
        "msg": "success",
        "data": { ... }
    }
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            response = renderer_context['response']
            code = 0 if int(response.status_code / 100) == 2 else -1
            msg = 'success'
            if isinstance(data, dict):
                msg = data.pop('msg', msg)
                code = data.pop('code', code)
                if not data.get("page_size"):
                    data = data.pop('data', data)
            if code != 0 and data:
                try:
                    msg = data.pop('detail', 'failed')
                except Exception as e:
                    msg = 'failed'
            res = {
                'code': code,
                'msg': msg,
                'data': data,
            }
            return super().render(res, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)
