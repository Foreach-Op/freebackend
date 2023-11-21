# mqttapp/views.py
from django.http import HttpResponse
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("your_topic")


def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")


def mqtt_subscribe(request):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Replace 'mqtt.eclipse.org' with your MQTT broker address
    client.connect("23.88.63.32", 1883, 60)

    # Start the loop
    client.loop_start()

    return HttpResponse("MQTT Subscription Started.")
