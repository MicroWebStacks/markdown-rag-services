import sys
from os.path import abspath,dirname,join
service_path = dirname(abspath(__file__))
root_path = dirname(service_path)
sys.path.append(root_path)
from common import utils as utl
from utils import embed_utils as eutl
import numpy as np

def embed_one_resource(resource_name):
    embeddings_dir = join(root_path,"cache/process/embeddings",resource_name)
    chunks = utl.load_json(join(embeddings_dir,"chunks.json"))
    print(f"loaded {len(chunks)} chunks")
    resource_embeddings = eutl.embed_chunk_list(chunks,model_name)
    np.savez(join(embeddings_dir,f'{model_name}.npz'), **resource_embeddings)
    print(f"saved embeddings.npz in {embeddings_dir}")
    return

manifest = utl.load_yaml(join(root_path,"manifest.yaml"))
model_name = "all-MiniLM-L6-V2"
if __name__ == "__main__":
    embed_one_resource("home-website")
