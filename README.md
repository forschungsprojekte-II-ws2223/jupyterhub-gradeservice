# Jupyterhub Docker

This folder contains a simple JupyterHub docker deployment, that uses a postgres database and spawns single-user Jupyter notebooks as docker containers.

## Setup

1. If you want to use this setup with a Moodle that is not running on your local machine, the URL of the Moodle instance needs to be
   added to the following settings files:
   [jupyterhub_config.py](./jupyterhub_docker/jupyterhub_config.py) in line 34
   [jupyter_notebook_config.py](./jupyterhub_docker/jupyterlab/jupyter_notebook_config.py) in line 28.

1. Build the jupyterlab image

   ```shell
   docker build ./jupyterlab -t jupyterlab
   ```

   This will take some time because of the dependencies in [requirements.txt](./jupyterlab/requirements.txt).
   You can do the next step while waiting for the image to be built.

1. Pull the otter-grader docker image

   ```sh
   docker pull ucbdsinfra/otter-grader
   ```

1. Make sure to set secure passwords/secrets in the [.env](./.env) file for the following enviroment variables:

   - `POSTGRES_PASSWORD`
   - `JWT_SECRET`
   - `API_TOKEN`

1. Build and start the hub

   After the jupyterlab image hase been built and environment variables are set up you can start the JupyterHub:

   ```shell
   docker compose up -d --build
   ```

- The JupyterHub runs on port `8000` by default.
- Gradeservice runs on port `5000` by default.
- You can change this in the [docker-compose.yml](./docker-compose.yml).

Run `docker compose down` if you want to delete the containers. The data volumes are not affected by this. If you want to delete these aswell run `docker volume prune` after you executed `docker compose down` (this deletes ALL unused volumes, not just the jupyterhub volumes).

## Testing

The JupyterHub uses a json web token [authenticator](https://github.com/izihawa/jwtauthenticator_v2).

- To test this setup, you can create a json web token on this [site](https://jwt.io/#debugger-io).
  In the 'verify signature' field the secret can stay 'your-256-bit-secret' as it is (the secret should match the one in the [environment file](.env)).
  The 'secret base64 encoded' should NOT be checked.
- You can now add the token as a query parameter to the address that your JupyterHub is running on.
  For example: <http://127.0.0.1:8000/?auth_token=>{your token here}

## Manage dependencies

### Update docker dependencies

- Stop the running containers
- Make the version changes in the [docker-compose](docker-compose.yml) file you want to make.
- Run `docker-compose pull` then wait for the download of the new dependencies.
- Run `docker-compose up -d` and wait for the containers to be recreated.
- Then the containers can be used again.

### Manage python dependencies

External dependencies for the JupyterLab containers are managed through the [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/). This way one can specify certain versions, upgrade versions or add additional libraries.
