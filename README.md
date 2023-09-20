# Тестовое задания для Junior разработчика 

Нужно забрать показания температуры погоды по API для станции с ID S50, S107 и статус "api_info" и передать в MQTT брокер с шифрованием SSL и аутентификацией. Стандартный порт брокера – 8885.

Язык программирования в приоритете С++, но вы можете использовать Python.

### Готовое задание должно содержать:

2 топика с id и температурой. Адрес топика должен иметь вид: /api/temperature/id
1 топик статус api_info. Адрес топика должен иметь вид: /api/status

### Ссылки для выполнения задания: 
открытое API для сбора показаний о погоде: https://api.data.gov.sg/v1/environment/air-temperature 
MQTT брокер: Mosquitto Test Server 

### Формат репрезентации задания: 
исходный код и скомпилированная программа для windows/linux
