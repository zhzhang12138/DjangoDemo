# -*- coding:utf-8 -*-
# @FileName  :production.py
# @Time      :2022/11/17 16:01
# @Author    :John Doe
from DjangoDemo.settings import *

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES['default']['USER'] = "USER"
DATABASES['default']['PASSWORD'] = "PASSWORD"
DATABASES['default']['HOST'] = "HOST"
DATABASES['default']['PORT'] = "PORT"
