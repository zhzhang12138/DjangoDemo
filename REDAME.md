### 快速启动

> 1、修改数据库链接 develop.py

```
DATABASES['default']['USER'] = "USER"
DATABASES['default']['PASSWORD'] = "PASSWORD"
DATABASES['default']['HOST'] = "HOST"
DATABASES['default']['PORT'] = "PORT"
```

> 2、docker打包部署

```shell
docker build -t django_demo:1.0 -f ./Dockerfile . 

docker run -d -p 9001:9090 --name django_demo_01 -t django_demo:1.0


访问：http://localhost:9001/user/health
```

