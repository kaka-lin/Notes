FROM python:3.6.11-alpine
LABEL maintainer="kaka <vn503024@gmail.com>"

RUN mkdir /root/docker_compose_example
ADD . /root/docker_compose_example
WORKDIR /root/docker_compose_example
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
