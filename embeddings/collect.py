import sys
from os.path import abspath,dirname,join
service_path = dirname(abspath(__file__))
root_path = dirname(service_path)
sys.path.append(root_path)
from common import utils as utl
import embed_utils as eutl
from datetime import datetime

def get_pages_elements(structure_dir):
    start = datetime.now()
    pages_elements = []
    docs_list = utl.load_json(join(structure_dir,"document_list.json"))
    for doc in docs_list:
        if(doc["format"].startswith("markdown")):
            content = utl.load_json(join(structure_dir,f"documents/{doc['sid']}/content.json"))
            pages_elements.extend(eutl.get_headings(content))
            pages_elements.extend(eutl.get_tables(content))
            pages_elements.extend(eutl.get_images(content))
            pages_elements.extend(eutl.get_codes(content))
            pages_elements.extend(eutl.get_paragraphs(content))

    # filter out empty entries
    pages_elements = [el for el in pages_elements if((len(el["text"])>0))]
    duration = datetime.now() - start
    print(f"collected pages elements in {utl.format_duration(duration)}")
    return pages_elements

def collect_one_resource(resource_name):
    structure_dir = join(root_path,"cache/process/structure",resource_name)
    pages_elements = get_pages_elements(structure_dir)
    embeddings_dir = join(root_path,"cache/process/embeddings",resource_name)
    utl.save_json(pages_elements,join(embeddings_dir,"elements.json"))

manifest = utl.load_yaml(join(root_path,"manifest.yaml"))

if __name__ == "__main__":
    collect_one_resource("home-website")
