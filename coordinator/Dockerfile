
FROM python:3.9-slim

WORKDIR /coordinator/flaskr/app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 6060

CMD ["python", "flaskr/app.py"]
