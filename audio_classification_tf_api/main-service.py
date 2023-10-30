"""Audio-Classification API module."""


import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("public.mqtthq.com",1883,60)

client.publish("Audio-service/status", "END");

client.disconnect();
print("End Service")

