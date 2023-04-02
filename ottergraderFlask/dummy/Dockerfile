FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /dummyWeb .

ENTRYPOINT [ "python3", "main.py" ], 