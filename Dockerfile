FROM python:3.8

ADD . /app

WORKDIR /app

RUN pip3 install flask gunicorn oyaml

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app"]