# -*- coding:utf-8 -*-
# @FileName  :urls.py
# @Time      :2022/11/17 15:59
# @Author    :John Doe
from django.urls import path

from user.views import HealthCheckAPI

urlpatterns = [
    path('health/', HealthCheckAPI.as_view()),
]
