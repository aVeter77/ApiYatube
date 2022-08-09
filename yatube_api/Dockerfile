FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r ./requirements.txt --no-cache-dir

COPY ./ .


CMD ["gunicorn", "yatube_api.wsgi:application", "--bind", "0:8000" ] 
