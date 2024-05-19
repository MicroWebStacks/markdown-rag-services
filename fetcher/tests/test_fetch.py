import utils as utl
import github as gutl
from os.path import join,dirname

# Constants
root_path = join(dirname(__file__),"../../..")
cache_path = join(root_path,"cache")

def main():
    # Load YAML configuration
    manifest = utl.load_yaml(join(root_path,'manifest.yaml'))
    fetch_list = manifest["fetch"]
    for entry in fetch_list:
        if (entry["type"] == "github"):
            print("Fetching files for repository:", entry['repository'])
            gutl.get_repo(entry,cache_path)

if __name__ == "__main__":
    main()
