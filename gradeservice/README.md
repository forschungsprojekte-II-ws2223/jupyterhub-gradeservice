# Gradeservice

## Environment Setup

To set up an environment for working on Otter, we recommend using
[Conda](https://docs.conda.io/en/latest/miniconda.html). This repo contains an
[`environment.yml`](environment.yml) file which defines all of the requirements for an environment
used to work on Otter.

Running

```sh
conda env create -f environment.yml
```

Run the api with:

```sh
uvicorn src:app --reload
```
