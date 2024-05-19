import sys
sys.path.append("../common/utils")
import mqtt_client as mc
import threading
import subprocess
import os
from os.path import join

def markdown_builder(topic,payload):
    print("markdown builder")
    mc.publish("markdown/build/start",{"build":payload})
    if("resource" in payload):
        resource = payload["resource"]
        path = payload.get("path")
        thread = threading.Thread(target=build_website,args=(resource,path))
        thread.start()
    return

def build_website(resource,path):
    try:
        original_dir = os.getcwd()
        os.chdir("/builder")
        os.environ['OUT_DIR']       = f'../cache/web/{resource}'
        os.environ['STRUCTURE']     = f'../cache/process/{resource}/structure'
        os.environ['CONTENT']       = join("../cache",path)
        os.environ['PUBLIC_BASE']   = ''
        subprocess.run("pnpm run build", shell=True, check=True)
        os.chdir(original_dir)

        mc.publish("markdown/build/finish", resource)
    except Exception as e:
        print(f"unhandled exception {e}")
        mc.publish("markdown/error", {"error": str(e)})
        return

mc.add_action("markdown/build",markdown_builder)
mc.set_status_topic("markdown/status")
mc.start()
