# Gradeservice

## Setup

1. Install Anaconda (or Miniconda for a more minimal version) for setting up the python virtual environment.
   This repo contains an [`environment.yml`](environment.yml) file which defines all of the requirements for the environment.

   Setup the environment:

   ```sh
   conda env create -f environment.yml
   ```

   After the environment is installed reload your vs code (ctrl+shift+p reload window). Open a .py file and select the python interpreter matching the virtual environment in the bottom right.

1. Open up a terminal window. Make sure the virtual environment is activated. Install dependencies with:

   ```sh
   pip install -e ".[dev]"
   ```

## Adding dependencies

**TODO**
...

## Run

**TODO**
Run the api with:

```sh
uvicorn src:app --reload
```
