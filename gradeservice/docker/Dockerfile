FROM python:3.11.2-bullseye

WORKDIR /app

COPY requirements-base.txt .

RUN pip install --no-cache-dir -r requirements-base.txt

COPY src .
COPY tests/otter/testdata .

CMD ["/bin/bash", "-c", "cd gradeservice;uvicorn main:app --reload --host 0.0.0.0 --port 5000"]
