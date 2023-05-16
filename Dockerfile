FROM python:3

RUN mkdir -p /home/app

COPY requirements.txt ./
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . /home/app

CMD ["python3", ".home/app/app/app.py"]