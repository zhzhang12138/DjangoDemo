import os
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckAPI(APIView):
    """
    GET -> 健康检查
    """
    authentication_classes = []

    def get(self, request):
        print("当前进程号", os.getpid())
        return Response({"code": 0, "msg": "success"})
