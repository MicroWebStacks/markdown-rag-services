import sys
from os.path import abspath,dirname,join
service_path = dirname(abspath(__file__))
root_path = dirname(service_path)
sys.path.append(root_path)
from common import utils as utl
import tiktoken
from copy import deepcopy
from utils import chunk_utils as cutl

def chunk_one_resource(resource_name):
    embeddings_dir = join(root_path,"cache/process/embeddings",resource_name)
    elements = utl.load_json(join(embeddings_dir,"elements.json"))
    encoding = tiktoken.encoding_for_model("text-embedding-ada-002")
    elements_embeddings = []
    for el in elements:
        #headings are irrelevant for semantic search and question answering
        if (el["type"] not in ["paragraph", "diagram", "code", "table"]):
            elements_embeddings.append(el)
            continue
        results = cutl.split_chunk_text(el["text"],1000,200)
        for index,result in enumerate(results,1):
            el_part = deepcopy(el)
            el_part["text_len"] = len(result["text"])
            el_part["chunk_len"] = len(result["chunk"])
            el_part["text"] = result["text"]
            payload = ""
            if(el["heading"] is not None):
                payload += "heading="+el["heading"]+"\n"
            if("meta" in el):
                payload += el["meta"]+"\n"
            payload += result["chunk"]
            el_part["payload"] = payload
            el_part["hash"] = utl.short_md5(payload)
            el_part["tokens"] = len(encoding.encode(payload))
            if(len(results)>1):
                el_part["part"] = index
            elements_embeddings.append(el_part)
    utl.save_json(elements_embeddings,join(embeddings_dir,"chunks.json"))
    return

manifest = utl.load_yaml(join(root_path,"manifest.yaml"))

if __name__ == "__main__":
    chunk_one_resource("home-website")
