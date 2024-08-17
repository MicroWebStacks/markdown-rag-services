import sys
from os.path import abspath,dirname,join
service_path = dirname(abspath(__file__))
root_path = dirname(service_path)
sys.path.append(root_path)
from common import utils as utl
from utils import sentence_utils as sutl
import numpy as np
import time

def find_similar_entries(query_text, top_k=5):
    print(f"find similarities in {resource} using {model_name}")
    query_embedding = sutl.text_encode(query_text,model_name=model_name)
    embeddings_dir = join(root_path,"cache/process/embeddings",resource)
    resource_embeddings_map = dict(np.load(join(embeddings_dir,f'{model_name}.npz')))
    print(f"loaded {len(resource_embeddings_map.keys())} embeddings")

    hashes = list(resource_embeddings_map.keys())
    resource_embeddings = np.stack(list(resource_embeddings_map.values()))
    start = time.time()
    similarities = sutl.similarity(query_embedding,resource_embeddings,top_k)
    print(f"{len(similarities)} similarities found in {utl.time_text(time.time()-start)}")
    print("Similarities")
    for k in similarities:
        print(f"{hashes[k['index']]} : {k['similarity']}")
    return

manifest = utl.load_yaml(join(root_path,"manifest.yaml"))
model_name = "text-embedding-3-small"
#model_name = "all-mpnet-base-v2"
#model_name = "all-MiniLM-L6-V2"
resource = "home-website"
if __name__ == "__main__":
    utl.load_env(service_path)
    find_similar_entries("This is a low power sensor")
