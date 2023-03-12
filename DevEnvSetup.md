# Dev Environment Setup

## 1. Prerequesites

Install the following tools:

- [VS Code](https://code.visualstudio.com/) (if you are on windows make sure that add VS Code to PATH is checked during installation)
- [Docker](https://www.docker.com/)

## 2. Moodle and Jupyterhub setup

Build and start the Moodle and Jupyterhub containers by running these two commands:

```sh
docker-compose -f setup/jupyterhub_docker/docker-compose.yml up -d --build
docker-compose -f setup/moodle_docker/docker-compose.yml up -d --build
```

## 3. VS Code Setup

Install the following extensions:

- Dev Containers
- Docker
- EditorConfig
- HTML CSS Supporrt
- Mustache Template - Snippets & Autocomplete
- PHP Extension Pack
- PHP Sniffer
- Prettier
- Python
- Markdownlint

You can use the following command to install the extensions from the command line:

```sh
code --install-extension ms-vscode-remote.remote-containers \
  --install-extension ms-azuretools.vscode-docker \
  --install-extension EditorConfig.EditorConfig \
  --install-extension ecmel.vscode-html-css \
  --install-extension imgildev.vscode-mustache-snippets \
  --install-extension xdebug.php-pack \
  --install-extension wongjn.php-sniffer \
  --install-extension esbenp.prettier-vscode \
  --install-extension ms-python.python \
  --install-extension davidanson.vscode-markdownlint
```

## 4. Attatch to moodle container and install extensions

- Open up VS Code
- Click on the green icon at the bottom left of the window
- From the popup menu that apears, select the option "Attach to Running Container..."
- Select the moodle container (should be called moodle_docker-moodle-1 or similar)
- A new window will open and you should be able to browse the filesystem of the moodle docker container
- Open up the extensions tab from the menu on the left and select "Install in container" for the following extensions:
  - EditorConfig
  - PHP Extension Pack
  - PHP Sniffer
  - HTML CSS Support
  - Mustache Template - Snippets & Autocomplete
  - Markdownlint

## Clone the repository

Follow this guide for sharing git credentials with the container: <https://code.visualstudio.com/docs/devcontainers/containers#_sharing-git-credentials-with-your-container>

After you have successfuly set up git, you can clone the repository into the moddle plugin directory:  
Open the VS Code command line by pressing `Ctrl+J` (Windows, Linux) or `⌘+J` (MacOS) and run the following commands.

```sh
cd /bitnami/moodle/mod/
```

if you are using ssh for authenticating with git:

```sh
git clone git@github.com:forschungsprojekte-II-ws2223/moodle-mod_jupyter.git ./jupyter
```

if you are using http:

```sh
git clone https://github.com/forschungsprojekte-II-ws2223/moodle-mod_jupyter.git ./jupyter
```

Change to the plugin folder and install the php dependencies:

```sh
cd jupyter && composer install
```

Open a new vs code window in the repository folder:

```sh
code .
```

You can now close the old window.

## 5. Using the Moodle and JupyterHub

Moodle is running on <http://127.0.0.1:80>, the default admin username is `user` and password is `bitnami`.  
Upon loging in to moodle for the first time you should see the installation screen for our plugin.  
The JupyterHub is running on <http://127.0.0.1:8000>.

## Further reading/information

[Learn Visual Studio Code in 7min (Official Beginner Tutorial)](https://code.visualstudio.com/docs/introvideos/basics)  
[Using Git source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)  
[VS Code Documentation](https://code.visualstudio.com/docs)  
[DevContainers Documentation](https://code.visualstudio.com/docs/devcontainers/containers)  
[Keybind Cheat Sheet Windows](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)  
[Keybind Cheat Sheet MacOS](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)
