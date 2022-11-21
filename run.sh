# 打包
docker build -t django_demo:1.0 -f ./Dockerfile .

# 部署
docker run -d -p 9001:9090 --name django_demo_01 -t django_demo:1.0
