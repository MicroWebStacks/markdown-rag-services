import paho.mqtt.client as mqtt
import json
import os

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    for action in actions:
        client.subscribe(action["topic"])
    if(status_topic != ""):
        client.publish(status_topic,"connected")

def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}")
    for action in actions:
        if msg.topic == action["topic"]:
            try:
                data = json.loads(msg.payload)
                action["function"](msg.topic,data)
            except json.decoder.JSONDecodeError as e:
                print(f"json.decoder.JSONDecodeError {e}")

def start():
    print(f"connecting to {BROKER}:{PORT}")
    client.connect(BROKER, PORT, 60)
    # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
    client.loop_forever()
    return

def set_status_topic(topic):
    global status_topic
    status_topic = topic
    client.will_set(status_topic, "disconnected", qos=2)
    return

def add_action(topic,function):
    actions.append({
        "topic":topic,
        "function":function
    })
    return

def publish(topic, data):
    client.publish(topic, json.dumps(data))
    return

# Constants
BROKER = os.getenv("BROKER","localhost")
PORT = 1883

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

actions = []
status_topic = ""
