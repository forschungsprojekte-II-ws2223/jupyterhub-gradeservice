# Jupyterhub Docker
This folder contains a simple JupyterHub docker deployment, that uses a postgres database and spawns Notebooks as Docker containers.

# Setup

If you want to use this setup with a Moodle other than the development setup, the URL of the Moodle instance needs to be
added to the according settings files before executing the server. There add your URL to the list in 
[jupyterhub_config.py](./jupyterhub/jupyterhub_config.py) in line 20 and to the list in 
[jupyter_notebook_config.py](./jupyterlab/jupyter_notebook_config.py) in line 14.

- To build the containers images (This step is only needed if you modified the dockerfiles or related config files):
``` shell
docker compose build
```
 
- To create and start the containers:
```shell
docker-compose up -d
``` 

Run `docker compose down` if you want to delete the containers. The data volumes are not affected by this. If you want to delete these aswell run `docker volume prune` after you executed `docker compose down` (this deletes ALL unused volumes, not just the jupyterhub volumes).

## Testing
The JupyterHub uses a json web token [authenticator](https://github.com/izihawa/jwtauthenticator_v2).  
- To test this setup, you can create a json web token on this [site](https://jwt.io/#debugger-io). 
In the 'verify signature' field the secret can stay 'your-256-bit-secret' as it is (the secret should match the one in the [environment file](.env)).
The 'secret base64 encoded' should NOT be checked. 
- You can now add the token as a query parameter to the address that your JupyterHub is running on.  
For example: http://127.0.0.1:8000/?auth_token=**your token here**

## Manage dependencies
### Update docker dependencies
- Stop the running containers
- Make the version changes in the [docker-compose](docker-compose.yml) file you want to make.
- Run `docker-compose pull` then wait for the download of the new dependencies.
- Run `docker-compose up -d` and wait for the containers to be recreated.
- Then the containers can be used again.

### Manage python dependencies
The libraries are managed through the [requirements.txt](https://pip.pypa.io/en/stable/reference/requirements-file-format/). This way one can specify certain versions, upgrade versions or add additional libraries.

## Architecture

This setup was derived from these two guides: [OpenDreamKit](https://opendreamkit.org/2018/10/17/jupyterhub-docker/), [GitHub repo](https://github.com/jupyterhub/)

This is a quick explanation on how the deployment is built:
- create new directory
- create a docker-compose.yml file with JupyterHub and a postgres database as services
    - add port forwarding for the UI and the API
    - add volumes
    - add environment variables
- create a .env file with the given content
- create JupyterLab directory
    - create jupyter_notebook_config.py with the JupyterLab configuration
    - create a Dockerfile
        - point to JupyterLab docker image
        - copy jupyter_notebook_config.py into the image
        - install required dependencies
- create JupyterHub directory
    - create a jupyterhub_config.py with the JupyterHub configuration
    - create a Dockerfile
        - point to JupyterHub docker image
        - copy jupyterhub_config.py into the image
        - install required dependencies
