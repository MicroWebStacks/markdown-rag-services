import asyncio
from aiomqtt import Client,Will
import json
import yaml
import os

def load_yaml(fileName):
    with open(fileName, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return

async def run():
    print("async run()")
    workflow = load_yaml("/app/workflow.yaml")
    print("workflow loaded - waiting for event")
    async with Client(BROKER, PORT, will=Will("runner/status", "disconnected", 2, True)) as client:
        await client.publish("runner/status","connected")
        for action in workflow:
            finish_topic = action["action"] + "/finish"
            await client.publish(f"runner/start", payload=json.dumps(action))
            await client.subscribe(finish_topic)
            await client.publish(action["action"], payload=json.dumps(action))
            async for message in client.messages:
                print(f"received message on {message.topic}")
                print(message.payload)
                break
            await client.unsubscribe(finish_topic)
            await client.publish(f"runner/finish", payload=json.dumps(action))
        await client.disconnect()
    return

BROKER = os.getenv("BROKER","localhost")
PORT = 1883

asyncio.run(run())
