import os
import typesense
from dotenv import load_dotenv
from datetime import datetime
import sys
sys.path.append("../common/utils")
from utils import format_duration

def load_env():
    # Try to load .env from the current directory
    env_path = '.env'
    if load_dotenv(env_path):
        print("Loaded .env from current directory.")
    else:
        # Try to load .env from the parent directory
        parent_env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
        if load_dotenv(parent_env_path):
            print("Loaded .env from parent directory.")
        else:
            print("No .env file found.")

def create_collection(schema):
  print("* creating collection")
  client.collections.create(schema)
  return

def create_documents_on_by_one(collection,documents):
  print(f"* creating {len(documents)} documents:")
  for document in documents:
    client.collections[collection].documents.create(document)
  return

def create_documents(collection,documents):
  start = datetime.now()
  print(f"* creating {len(documents)} documents:")
  client.collections[collection].documents.import_(documents, {'action': 'create'})
  duration = datetime.now() - start
  print(f"* created {len(documents)} documents in {format_duration(duration)}")
  return

def collection_exists(collection_name):
  try:
      docs = client.collections[collection_name].retrieve()
      print(f"collection '{collection_name}' exists")
      return True
  except typesense.exceptions.ObjectNotFound as e:
      print(e)
      print(f"collection '{collection_name}' does not exist")
      return False

def collection_delete(collection_name):
  client.collections[collection_name].delete()
  return

def collections_list():
  print("listing all collections:")
  collections = client.collections.retrieve()
  for collection in collections:
      print(f" - {collection['name']}")
  return

def get_client():
   return client

def create_client():

  print(f"connecting typesense client to http://{host}:{port}")

  client = typesense.Client({
  'api_key': api_key,
  'nodes': [{
      'host': host,
      'port': port,
      'protocol': "http"
  }],
  'connection_timeout_seconds': 10
  })
  return client

def search(collection,params):
  search_result = client.collections[collection].documents.search(params)
  return search_result


load_dotenv()
host = os.getenv('SEARCH_HOST','localhost')
port = 8108
api_key = os.getenv('TYPESENSE_API_KEY')
if(api_key is None):
    print("API key not found, provide TYPESENSE_API_KEY variable in .env")
    exit(0)

client = create_client()
