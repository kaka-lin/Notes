FROM jupyter/minimal-notebook:8ccdfc1da8d5
ARG JUPYTERHUB_VERSION
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --no-cache \
    jupyterhub==$JUPYTERHUB_VERSION
