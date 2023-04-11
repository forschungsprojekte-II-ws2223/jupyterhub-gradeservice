FROM python:3.11.2-bullseye

RUN apt update && apt -y upgrade
RUN apt-get install -y pandoc
RUN apt-get install -y texlive-xetex texlive-fonts-recommended texlive-plain-generic

WORKDIR /app

COPY . .

RUN pip install .

CMD ["/bin/bash", "-c", "cd gradeservice;uvicorn src.gradeservice.main:app --reload --host 0.0.0.0 --port 5000"]
