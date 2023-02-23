FROM python:3.9

ADD app.py ./

RUN pip install otter-grader \
    requests \
    flask

CMD [ "python", "app.py" ], 