import sys
sys.path.append("../common/utils")
from utils import load_json
from os.path import join
import typesense_utils as tyutl

def inject_elements(resource):
    if(tyutl.collection_exists(resource)):
        print(f" collection {resource} existing - deleting old collection")
        tyutl.collection_delete(resource)

    print(f" creating new {resource} collection")
    schema_fields = load_json("schema.json")
    schema = {
        "name": resource,
        "fields": schema_fields
    }
    tyutl.create_collection(schema)
    tyutl.collections_list()

    pages_elements = load_json(join(CACHE_PATH,"process",resource,"elements.json"))
    tyutl.create_documents(resource,pages_elements)

CACHE_PATH = "../cache"

if __name__ == "__main__":
    inject_elements("test-website")
