import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import json

TOPIC = "orinlakantobad"
USERNAME = "flolikewater"  # "flolikewater GMDACBGLR6"
UID = "GMDACBGLR6"  #
# UID = input("Swap your card: ")

print("UID: ", UID)
reader_data = {
    "type": "access",
    "time": 1572542188,
    "isKnown": "true",
    "access": "Admin",
    "username": USERNAME,
    "uid": UID,
    "door": "esp-rfid",
}
payload = json.dumps(reader_data)
mqtt_broker = "broker.hivemq.com"
client = mqtt.Client("Cafeteria")
client.connect(mqtt_broker)

try:
    while True:
        # payload = input("Flash your card :")
        client.publish(TOPIC, payload)
        print(f"Just published {payload} to topic {TOPIC}")
        time.sleep(15)
except KeyboardInterrupt:
    print(" \n Ctrl + C pressed!")

# client.disconnect()
