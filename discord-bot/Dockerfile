FROM python:3.9-buster

WORKDIR /usr/src/discord-bot/

COPY main.py .
COPY requirements.txt .
COPY .env .

RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]