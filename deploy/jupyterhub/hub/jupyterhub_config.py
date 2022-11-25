import os
import sys

c = get_config() # pyright: reportUndefinedVariable=false

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']

network_name = os.environ['DOCKER_NETWORK_NAME']
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_host_config = { 'network_mode': network_name }

c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.bind_url = 'http://:8000/jupyterhub/'

# this is commented out, because the reverse proxy handles this. See secHeaders middleware in traefik/data/dynamic_conf.yml
# c.Spawner.args = [f'--NotebookApp.allow_origin=*']
# c.JupyterHub.tornado_settings = {
#     'cookie_options': {"SameSite": "None", "Secure": True},
#     'headers': {
#         'Content-Security-Policy': "frame-ancestors 'self' http://localhost:80 http://127.0.0.1:80 http://localhost:8000 http://127.0.0.1:8000"
#     }
# }

# Persist hub data on volume mounted inside container
data_dir = os.environ.get('DATA_VOLUME_CONTAINER', '/data')

c.JupyterHub.cookie_secret_file = os.path.join(data_dir,
    'jupyterhub_cookie_secret')

# Redirect to JupyterLab, instead of the plain Jupyter notebook
c.Spawner.default_url = '/lab'

#idle culler setup:
c.JupyterHub.load_roles = [
    {
        "name": "jupyterhub-idle-culler-role",
        "scopes": [
            "list:users",
            "read:users:activity",
            "read:servers",
            "delete:servers",
            # "admin:users", # if using --cull-users
        ],
        # assignment of role's permissions to:
        "services": ["jupyterhub-idle-culler-service"],
    }
]
c.JupyterHub.services = [
    {
        "name": "jupyterhub-idle-culler-service",
        "command": [
            sys.executable,
            "-m", "jupyterhub_idle_culler",
            "--timeout=3600",
        ],
        # "admin": True,
    }
]

# database setup
c.JupyterHub.db_url = 'postgresql://postgres:{password}@{host}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    password=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB'],
)

# Dummy authenticator for testing purposes
# c.JupyterHub.authenticator_class = "dummy"

# JWT Authenticator Setup
# JSONWebTokenLocalAuthenticator provides local user creation
c.LocalAuthenticator.create_system_users=True
c.JupyterHub.authenticator_class = 'jwtauthenticator.jwtauthenticator.JSONWebTokenLocalAuthenticator'
# The secrect key used to generate the given token
c.JSONWebTokenAuthenticator.secret = os.environ['JWT_SECRET']
# The claim field contianing the moodle user id
c.JSONWebTokenAuthenticator.username_claim_field = 'name'
# This config option should match the aud field of the JSONWebToken, empty string to disable the validation of this field.
c.JSONWebTokenAuthenticator.expected_audience = ''
# This will enable local user creation upon authentication, requires JSONWebTokenLocalAuthenticator
c.JSONWebLocalTokenAuthenticator.create_system_users = True
# Query param to retrieve JWT token
c.JSONWebTokenAuthenticator.param_name = 'auth_token'
