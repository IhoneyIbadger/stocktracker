FROM python:3

RUN mkdir -p /home/app

COPY . /home/app

CMD ["python3", ".home/app/app/app.py"]