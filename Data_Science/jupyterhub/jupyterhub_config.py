# Configuration file for jupyterhub.
import os

c = get_config()

# Set the Proxy's IP address and port
#c.JupyterHub.ip = '192.168.1.2'
c.JupyterHub.port = 443

# User containers will access hub
# by container name on the Docker network
c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_port = 8080

# Enabling SSL encryption
## 1. Using an SSL certificate
#c.JupyterHub.ssl_key = 'path/to/my.key'
#c.JupyterHub.ssl_certs = 'path/to/my.cert'

## 2. Using letsencrypt
c.JupyterHub.ssl_key = os.environ['SSL_KEY']
c.JupyterHub.ssl_cert = os.environ['SSL_CERT']

# Cookie secret
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/jupyterhub_cookie_secret'

# Authenticator
## 1. use GitHub OAuthenticator for local users
c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# create system users that don't exist yet
c.LocalAuthenticator.create_system_users = True

# Spawner: single-user server
## 1. Docker spawner
# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# pick a docker image. 
# This should have the same version of jupyterhub in it as our Hub.
c.DockerSpawner.image = os.environ['DOCKER_NOTEBOOK_IMAGE']
# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# user data presistence
# see https://github.com/jupyterhub/dockerspawner/blob/master/docs/source/data-persistence.md
# Explicitly set notebook directory because we'll be mounting a host volume to
# it.  Most jupyter/docker-stacks *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention.
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }

# Memory limits
c.Spawner.mem_limit = '2G'

# delete containers when the stop
c.DockerSpawner.remove = True

# User whitelist - set of users allowed to use the Hub
c.Authenticator.whitelist = {"kaka-lin"}

# Administrators= set of users who can administer the Hub itself
c.Authenticator.admin_users = {"kaka-lin"}
# Grant admin users permission to access single-user servers.
c.JupyterHub.admin_access = True
