import paho.mqtt.client as mqtt
import json
import requests
import time

from paho.mqtt.client import Client

# MQTT брокер и порт
MQTT_BROKER_ADDRESS = "test.mosquitto.org"
MQTT_BROKER_PORT = 8885

# Список станций и их ID
station_ids = ["S50", "S107"]


# Функция для получения данных о погоде с API
def get_weather_data(station_id):
    url = f"https://api.data.gov.sg/v1/environment/air-temperature?id={station_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data["items"][0]["readings"][0]["value"]
        return temperature
    else:
        print(f"Failed to fetch weather data for station {station_id}. Status code: {response.status_code}")
        return None


# Функция для публикации данных в MQTT
def publish_temperature_to_mqtt(client, station_id, temperature):
    topic = f"/api/temperature/{station_id}"
    client.publish(topic, temperature)
    print(f"Published temperature data for station {station_id}: {temperature}")


# Инициализация MQTT клиента
client: Client = mqtt.Client()
client.connect(MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT)

try:
    while True:
        for station_id in station_ids:
            temperature = get_weather_data(station_id)
            if temperature is not None:
                publish_temperature_to_mqtt(client, station_id, str(temperature))

        # Публикация статуса api_info в топике /api/status
        status_topic = "/api/status"
        client.publish(status_topic, "api_info is healthy")
        print("Published api_info status: api_info is healthy")

        # Ожидание перед следующим запросом данных
        time.sleep(10)  # Ожидание 30 минут

except KeyboardInterrupt:
    print("Interrupted")
    client.disconnect()