# -*- coding:utf-8 -*-
# @FileName  :authentications.py
# @Time      :2022/11/17 16:45
# @Author    :John Doe
from rest_framework.authentication import BaseAuthentication


class UserServerAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # 自定义认证方案
        return
