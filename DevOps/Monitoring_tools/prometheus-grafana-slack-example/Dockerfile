FROM python:3.8-alpine
LABEL maintainer="kaka <vn503024@gmail.com>"

RUN mkdir -p /root/prometheus_example
ADD . /root/prometheus_example
WORKDIR /root/prometheus_example

# need for install gevent
RUN apk update && apk add build-base libffi-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# reduce image size
RUN apk del build-base libffi-dev

CMD ["python", "app.py"]
