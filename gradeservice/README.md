# Gradeservice

## Setup

1. Make sure you have pthon >= 3.11 installed
1. Open up a terminal window and cd into the gradeservice folder
1. Install dependencies with:

   ```sh
   pip install -e ".[dev]"
   ```

## Adding dependencies

Open `requirements-(dev|base).in` file and add the dependency you need.

Compie the .in file to .txt:

```sh
pip-compile requirements-(dev|base).in
```

## Run

Run the api with:

```sh
uvicorn gradeservice.main:app --reload
```
