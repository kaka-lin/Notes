---
title: "[DS] Build JupyterHub with docker"
date: 2020-08-14
tags: [JupyterHub]
categories: [Data Science]
---

# JupyterHub

Use Docker to build a `JupyterHub` for multiple users

## Notices

Before your start to build a `JupyterHub` with docker, please download the relative file at [example](https://github.com/kaka-lin/Notes/tree/master/Data_Science/jupyterhub).

## Enable HTTPS (SSL encryption)

1. Generate a self-signed certificate with `openssl`, as below:

   - [create a self-signed certificate.](https://jupyter-notebook.readthedocs.io/en/latest/public_server.html#using-ssl-for-encrypted-communication)

    For example, the following command will create a certificate valid for 365 days with both the key and certificate data written to the same file:

    ```bash
    $ openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout jupyterhub.key -out jupyterhub.pem
    ```

2. Copy the certificate and key file to a director named `secrets` in the root directory.

    ```bash
    $ mkdir -p secrets
    $ cp jupyterhub.key jupyterhub.pem secrets/
    ```

## Create a JupyterHub Data Volumn

```bash
$ docker volume create --name jupyterhub-data
```

## Create a Docker Network

```bash
$ docker network create jupyterhub-network
```

## DockerSpawner: Build the Jupyter Notebook Image

```bash
$ make notebook_image
```

## Build the JupyterHub Image

```bash
$ make build
```

## Run JupyterHub

```bash
$ docker-compose up -d
```

## Stop JupyterHub

```bash
$ docker-compose down

```

Stops containers and remove volumes created by `up`.

```bash
$ docker-compose down --volumes
```
