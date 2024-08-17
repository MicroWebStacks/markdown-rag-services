import sys
from os.path import abspath,dirname,join
service_path = dirname(abspath(__file__))
root_path = dirname(service_path)
sys.path.append(root_path)
from common import utils as utl
from common.utils import github as gutl
import json

def process_fetch_list(fetch_list):
    for entry in fetch_list:
        try:
            results = []
            if entry["type"] == "github":
                print("Fetching files for repository:", entry['repository'])
                result = gutl.get_repo(entry, CACHE_PATH)
                entry.update(result)
                results.append(entry)
            else:
                print(f"fetcher/error type not supported {entry['type']}")
            print("fetcher/fetch/finish", json.dumps(results))
            if("resource" in entry):
                print(f"fetcher/resources/{entry['resource']}", json.dumps(results))
        except Exception as e:
            print(f"unhandled exception {e}")
            print("fetcher/error", json.dumps({"error": str(e)}))
    return

# Constants
CACHE_PATH = "../cache/fetch"
manifest = utl.load_yaml(join(root_path,"manifest.yaml"))


if __name__ == "__main__":
    process_fetch_list(manifest["fetcher"])
