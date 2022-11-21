FROM ccr.ccs.tencentyun.com/changchao/python:3.6

ENV ENV production

ADD . /code

WORKDIR /code

RUN pip3 install -i https://mirrors.aliyun.com/pypi/simple/ --upgrade -q pip
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:9090", "--preload", "DjangoDemo.wsgi:application"]

EXPOSE 9090
