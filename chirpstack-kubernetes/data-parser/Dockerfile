FROM arm32v7/python:3.10.0a5-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV MQTT_SERVER "localhost"

CMD ["sh", "-c", "python main.py $MQTT_SERVER"]

