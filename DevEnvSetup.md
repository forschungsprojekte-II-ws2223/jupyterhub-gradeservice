# 1. Prerequesites

Install the following tools:

- [VS Code](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/)

# 2. Moodle Docker Setup

```
docker-compose -f setup/jupyterhub_docker/docker-compose.yml up -d --build
docker-compose -f setup/moodle_docker/docker-compose.yml up -d --build
```

# 3. VS Code Setup

Install the following extensions:

- Dev Containers
- Docker
- EditorConfig
- ESLint
- HTML CSS Supporrt
- Mustache Template - Snippets & Autocomplete
- PHP Extension Pack
- PHP Sniffer
- Prettier
- Python

You can use the following command to install the extensions from the command line:

```sh
code --install-extension ms-vscode-remote.remote-containers \
  --install-extension ms-azuretools.vscode-docker \
  --install-extension EditorConfig.EditorConfig \
  --install-extension dbaeumer.vscode-eslint \
  --install-extension ecmel.vscode-html-css \
  --install-extension imgildev.vscode-mustache-snippets \
  --install-extension xdebug.php-pack \
  --install-extension wongjn.php-sniffer \
  --install-extension esbenp.prettier-vscode \
  --install-extension ms-python.python
```

## Attatch to container and install extensions

## Clone the repository

`git clone git@sopra.informatik.uni-stuttgart.de:kib3-students-project/moodle-mod_jupyter.git ./jupyter`

TODO: finish this...
