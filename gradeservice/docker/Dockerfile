FROM python:3.11.2-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY /src .
COPY /test .
COPY /tutorial .


#CMD ["/bin/bash", "-c", "cd src/gradeservice;uvicorn main:app --reload --host 0.0.0.0 --port 5000"]
