from django.http import HttpResponse
import paho.mqtt.client as mqtt
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


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


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]

    return Response(routes)


def getsocket(request):
    return render(request, "chat/cache.html")
