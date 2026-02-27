FROM python:3.8.10

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY /app/requirements.txt .

RUN pip install --upgrade pip==20.0.2 && pip install -r requirements.txt

COPY /app/src/ .

CMD [ "python", "./app.py" ]