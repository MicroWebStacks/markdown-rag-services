from utils import mqtt_client as mc
import threading
import subprocess
import os

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
        os.environ['OUT_DIR']       = f'/web/{resource}'
        os.environ['PUBLIC_BASE']   = ''
        os.environ['STRUCTURE']     = f'/process/{resource}/structure'
        os.environ['CONTENT']       = path
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
