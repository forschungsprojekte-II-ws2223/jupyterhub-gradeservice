FROM python:3.11.2-bullseye

WORKDIR /app

COPY . .

RUN pip install .

CMD ["/bin/bash", "-c", "cd gradeservice;uvicorn src.gradeservice.main:app --reload --host 0.0.0.0 --port 5000"]
