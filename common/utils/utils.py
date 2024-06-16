import os
from os import makedirs
from os.path import join, isdir, abspath, basename, dirname
import shutil
import json
import yaml
from datetime import timedelta

def make_dir(file_path):
    path = dirname(file_path)
    if(path):
        makedirs(path, exist_ok=True)
    return

def load_yaml(fileName):
    with open(fileName, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return

def load_json(fileName):
    return json.load(open(fileName,encoding='utf-8'))

def save_json(data,fileName):
    path = dirname(fileName)
    if(path):
        makedirs(path, exist_ok=True)
    jfile = open(fileName, "w")
    jfile.write(json.dumps(data, indent=4))
    jfile.close()
    return

def load_text(fileName):
    """Read text from a file encoded in UTF-8 and return its content."""
    with open(fileName, 'r', encoding='utf-8') as file:
        return file.read()

def save_text(data,fileName):
    path = dirname(fileName)
    if(path):
        makedirs(path, exist_ok=True)
    jfile = open(fileName, "w")
    jfile.write(data)
    jfile.close()
    return

def make_empty_dir(path):
    # Check if the directory exists
    if isdir(path):
        # Remove all contents of the directory
        shutil.rmtree(path)
    # Create the directory
    os.makedirs(path, exist_ok=True)

def move_to_parent(dir_path):
    # Ensure the directory exists
    if not isdir(dir_path):
        print(f"Directory does not exist: {dir_path}")
        return

    parent_dir = dirname(dir_path)  # Get the parent directory

    # Move each item in the directory to the parent directory
    for item in os.listdir(dir_path):
        src_path = join(dir_path, item)
        dst_path = join(parent_dir, item)

        # Move the item to the parent directory
        shutil.move(src_path, dst_path)

    # Remove the now empty directory
    os.rmdir(dir_path)
    print(f"Moved contents and removed directory: {dir_path}")

def dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

def format_size(bytes):
    # Define the unit thresholds and labels
    units = [("GB", 1024**3), ("MB", 1024**2), ("KB", 1024)]

    results = []
    remaining_bytes = bytes

    for unit, threshold in units:
        if remaining_bytes >= threshold:
            count = remaining_bytes // threshold
            remaining_bytes %= threshold
            results.append(f"{count} {unit}")
    
    # Join all non-zero results
    return " ".join(results) if results else "0 KB"

def format_duration(duration: timedelta):
    # Ensure that the duration is non-negative
    if duration < timedelta(0):
        duration = -duration
    # Extract days, seconds, and microseconds from the timedelta object
    days = duration.days
    seconds = duration.seconds
    microseconds = duration.microseconds
    milliseconds = microseconds // 1000  # Convert microseconds to milliseconds

    # Calculate hours, minutes, and seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    # Build the duration text string
    text = ""
    if days > 0:
        text += f"{days} d "
    if hours > 0:
        text += f"{hours} h "
    if minutes > 0:
        text += f"{minutes} mn "
    if seconds > 0:
        text += f"{seconds} s "
    if milliseconds > 0:
        text += f"{milliseconds} ms "

    return text.strip()  # Remove any trailing space
