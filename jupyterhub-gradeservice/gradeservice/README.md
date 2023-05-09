# Gradeservice

## Setup

1. Open up a terminal window. Install dependencies with:

   ```sh
   pip install -e ".[dev]"
   ```

## Adding dependencies

**TODO**
Open a \*.in file and write the dependency you need. Run:

```sh
pip-compile requirements-*.in
```

## Run

**TODO**
Run the api with:

```sh
uvicorn src:app --reload
```
