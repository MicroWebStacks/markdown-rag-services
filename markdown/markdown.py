import sys
from os.path import abspath,dirname,join
service_path = dirname(abspath(__file__))
root_path = dirname(service_path)
sys.path.append(root_path)
from common import utils as utl
from common.utils import mqtt_client as mc
import threading
import subprocess
import os
import argparse

def markdown_builder(topic,payload):
    print("markdown builder")
    mc.publish("markdown/build/start",{"build":payload})
    if("resource" in payload):
        resource = payload["resource"]
        path = payload.get("path")
        thread = threading.Thread(target=build_website,args=(resource,path))
        thread.start()
    return

def build_website(build_list):
    for entry in build_list:
        resource = entry["resource"]
        path = entry["path"]
        try:
            original_dir = os.getcwd()
            os.chdir("/builder")
            os.environ['OUT_DIR']       = f'/web/{resource}'
            os.environ['STRUCTURE']     = f'/process/structure/{resource}'
            os.environ['CONTENT']       = path
            os.environ['PUBLIC_BASE']   = ''
            subprocess.run("pnpm run build", shell=True, check=True)
            os.chdir(original_dir)

            mc.publish("markdown/build/finish", resource)
        except Exception as e:
            print(f"unhandled exception {e}")
            mc.publish("markdown/error", {"error": str(e)})
            return

def run_mqtt():
    mc.add_action("markdown/build", markdown_builder)
    mc.set_status_topic("markdown/status")
    mc.start()

def main():
    parser = argparse.ArgumentParser(description="Run the Markdown builder")
    parser.add_argument('command', choices=['run', 'build'], help="Commands: 'run' to start MQTT client, 'build' to build directly")
    args = parser.parse_args()

    if args.command == 'build':
        build_website(manifest["markdown"])
    elif args.command == 'run':
        run_mqtt()

# Constants
CACHE_PATH = "../cache/fetch"
manifest = utl.load_yaml(join(root_path,"manifest.yaml"))

if __name__ == "__main__":
    main()