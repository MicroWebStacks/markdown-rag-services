import json
import paho.mqtt.client as mqtt
from utils import github as gutl
import threading

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("fetcher/fetch")
    client.publish("fetcher/status","up")

def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}")
    if msg.topic == "fetcher/fetch":
        try:
            fetch_list = json.loads(msg.payload.decode())
            client.publish("fetcher/fetch/start", json.dumps(fetch_list))
            thread = threading.Thread(target=process_fetch_list,args=(client,fetch_list))
            thread.start()
        except Exception as e:
            print(f"unhandled exception {e}")
            client.publish("fetcher/error", json.dumps({"error": str(e)}))

def process_fetch_list(client,entry):
    try:
        results = []
        if entry["type"] == "github":
            print("Fetching files for repository:", entry['repository'])
            result = gutl.get_repo(entry, CACHE_PATH)
            entry.update(result)
            results.append(entry)
        else:
            client.publish("fetcher/error", json.dumps({
                "error": "type not supported",
                "type": entry["type"]
                }))

        client.publish("fetcher/fetch/finish", json.dumps(results))
        if("resource" in entry):
            client.publish(f"fetcher/resources/{entry['resource']}", json.dumps(results))
        return
    except Exception as e:
        print(f"unhandled exception {e}")
        client.publish("fetcher/error", json.dumps({"error": str(e)}))

# Constants
BROKER = 'mosquitto'
PORT = 1883
CACHE_PATH = "/fetch"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
