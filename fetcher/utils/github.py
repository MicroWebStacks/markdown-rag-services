import os
import requests
import zipfile
import fnmatch
from os.path import join
from utils import utils as utl
from datetime import datetime

def get_repo(params, cache_path):
    start = datetime.now()
    result = {}
    repository  = params["repository"]
    ref         = params["ref"]
    if("dest" in params):
        dest_path        = join(cache_path, params["dest"])
    else:
        dest_path        = join(cache_path, params["resource"])
    result["path"] = dest_path
    file_filter = params["filter"]
    # GitHub URL to download the repository as a zip file
    url = f"https://api.github.com/repos/{repository}/zipball/{ref}"

    # Download the zip file
    response = requests.get(url, stream=True)
    response.raise_for_status()  # Check for request errors

    # Define the path for saving the downloaded zip file temporarily
    utl.make_empty_dir(dest_path)
    zip_file = join(dest_path, 'repo.zip')
    # Write the zip file to the disk
    with open(zip_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    # Extract specific files from the zip
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        # List all file names in the zip
        all_files = zip_ref.namelist()
        result["total_files"] = len(all_files)
        base_folder = all_files[0].split('/')[0]
        # Filter files based on the given glob pattern
        #filtered_files = [f for f in all_files if Path(f).match(file_filter)]
        filtered_files = [f for f in all_files if fnmatch.fnmatch(f, base_folder+'/'+file_filter)]
        result["filtered_files"] = len(filtered_files)
        # Extract only the filtered files
        for file in filtered_files:
            zip_ref.extract(file, dest_path)
    utl.move_to_parent(join(dest_path,base_folder))
    # Remove the downloaded zip file after extraction
    os.remove(zip_file)
    size_bytes = utl.dir_size(dest_path)
    size_text = utl.format_size(size_bytes)
    result["size_bytes"] = size_bytes
    result["size_text"] = size_text
    stop = datetime.now()
    result["duration"] = str(stop-start)
    result["duration_text"] = utl.format_duration(stop-start)
    return result
