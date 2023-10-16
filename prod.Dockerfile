FROM python:3.12.0

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt
RUN pip install gunicorn


ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]
