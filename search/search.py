import sys
sys.path.append("../common/utils")
import mqtt_client as mc
import threading
from collect import collect_elements
from inject import inject_elements

def service_collect_elements(resource):
    try:
        collect_elements(resource)
        mc.publish("search/collect/finish",resource)
    except Exception as e:
        print(f"unhandled exception {e}")
        mc.publish("search/collect/error", {"error": str(e)})
    return

def service_inject_elements(resource):
    try:
        inject_elements(resource)
        mc.publish("search/inject/finish",resource)
    except Exception as e:
        print(f"unhandled exception {e}")
        mc.publish("search/inject/error", {"error": str(e)})
    return

def action_collect(topic,payload):
    print("search service - action_collect()")
    mc.publish("search/collect/start",payload)
    if("resource" in payload):
        resource = payload["resource"]
        thread = threading.Thread(target=service_collect_elements,args=(resource,))
        thread.start()
    else:
        mc.publish("search/collect/error", {"error": "resource needed in payload"})
        print("search service error resource needed in payload")
    return

def action_inject(topic,payload):
    print("search service - action_inject()")
    mc.publish("search/inject/start",payload)
    if("resource" in payload):
        resource = payload["resource"]
        thread = threading.Thread(target=service_inject_elements,args=(resource,))
        thread.start()
    else:
        mc.publish("search/inject/error", {"error": "resource needed in payload"})
        print("search service error resource needed in payload")
    return

mc.add_action("search/collect",action_collect)
mc.add_action("search/inject",action_inject)
mc.set_status_topic("search/status")
mc.start()
