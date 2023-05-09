# Gradeservice

## Setup

1. Make sure you have Python >= 3.11 installed
1. Open up a terminal window and `cd` into the _gradeservice_ folder
1. Install dependencies:

   ```sh
   pip install -e ".[dev]"
   ```

## Run

Start the api:

```sh
uvicorn gradeservice.main:app --reload
```

## Adding dependencies

1. Install the dependency with pip
1. Open `requirements-(dev|base).in` file and add the dependency you need.
1. Compile the .in file to .txt:

    ```sh
    pip-compile requirements-(dev|base).in
    ```
