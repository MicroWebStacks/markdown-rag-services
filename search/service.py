from utils import mqtt_client as mc
import threading
from collect import collect_elements

def service_collect_elements(resource):
    try:
        collect_elements(resource)
        mc.publish("markdown/build/finish",resource)
    except Exception as e:
        print(f"unhandled exception {e}")
        mc.publish("search/collect", {"error": str(e)})
    return

def action_collect(topic,payload):
    print("search service")
    mc.publish("search/collect/start",{"build":payload})
    if("resource" in payload):
        resource = payload["resource"]
        thread = threading.Thread(target=service_collect_elements,args=(resource))
        thread.start()
    return


mc.add_action("search/collect",action_collect)
mc.set_status_topic("search/status")
mc.start()
