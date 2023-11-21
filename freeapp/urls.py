# mqttapp/urls.py
from django.urls import path
from .views import mqtt_subscribe

urlpatterns = [
    path('mqtt_subscribe/', mqtt_subscribe, name='mqtt_subscribe'),
]
