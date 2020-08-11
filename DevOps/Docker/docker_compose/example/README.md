# Docker Compose Example

Build a simple Python web application running on Docker Compose.

This application uses the Flask framework and
maintains a hit counter in Redis

```
Flask + Redis 網頁人數統計的範例
```

## Build and Run

```bash
$ docker-cpmpose up

# run services in background
# -d: datached mode
$ docker-compose up -d
```

## Stop && Remove Container

```bash
$ docker-compose down

# --volumes: remove the data volume
#            used by the Redis container
$ docker-compose down --volumes
```

## Reference

1. [Get started with Docker Compose](https://docs.docker.com/compose/gettingstarted/)

2. [Docker Compose 建置 Web service 起步走入門教學](https://blog.techbridge.cc/2018/09/07/docker-compose-tutorial-intro/)
