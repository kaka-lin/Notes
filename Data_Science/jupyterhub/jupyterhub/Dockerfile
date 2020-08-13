ARG JUPYTERHUB_VERSION
FROM jupyterhub/jupyterhub:$JUPYTERHUB_VERSION
LABEL maintainer="kaka <vn503024@gmail.com>"

# Install oauthenticator, dockerspawner
RUN pip install --upgrade pip
RUN pip install --no-cache-dir \
    oauthenticator \
    dockerspawner

# Copy jupyterhub_config.py
COPY jupyterhub_config.py /srv/jupyterhub

# Copy SSL certificate 
ENV SSL_CERT /srv/jupyterhub/secrets/jupyterhub.crt
ENV SSL_KEY /srv/jupyterhub/secrets/jupyterhub.key
COPY ./secrets/*.pem $SSL_CERT
COPY ./secrets/*.key $SSL_KEY
RUN chmod 700 /srv/jupyterhub/secrets && \
    chmod 600 /srv/jupyterhub/secrets/*
