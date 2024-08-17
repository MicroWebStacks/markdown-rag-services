from os.path import abspath,dirname,join,exists
from os import makedirs
service_path = dirname(dirname(abspath(__file__)))
root_path = dirname(service_path)
from utils import sentence_utils as sutl
import numpy as np


def print_vectors_dim(np_vectors):
    if(len(np_vectors) == 0):
        return
    vector_dims = [len(vector) for vector in np_vectors]
    if all(dim == vector_dims[0] for dim in vector_dims):
        print(f"vectors dimension: {vector_dims[0]}")
    else:
        print(f"vectors dimensions: min {min(vector_dims)} max {max(vector_dims)}")
    return

def embed_chunk_list(chunks,model_name,cache_only=False):
    new_payloads = []
    new_hashes = []
    cached_results = {}
    tokens = 0
    if(model_name in vectors_cache):
        cache = vectors_cache[model_name]
    else:
        cache = None

    for chunk in chunks:
        if (("payload" in chunk) and ("hash" in chunk)):
            if (cache and (chunk["hash"] in cache)):
                cached_results[chunk["hash"]] = cache[chunk["hash"]]
            else:
                new_payloads.append(chunk["payload"])
                new_hashes.append(chunk["hash"])
                tokens += chunk["tokens"]

    if(cached_results):
        print(f"cached_results {len(cached_results.keys())} entries in cache")
    if(new_payloads):
        if(cache_only):
            print(f"cache_only, would need to encode {len(new_payloads)} new text entries with a total of {tokens} tokens")
            return cached_results
        print(f"start encoding {len(new_payloads)} text entries with a total of {tokens} tokens")
        np_vectors = sutl.text_list_encode(new_payloads,model_name)
        new_results = {new_hashes[i]: np_vectors[i] for i in range(len(new_payloads))}
        update_vectors_cache(new_results,model_name)
    else:
        new_results = {}

    results = {**cached_results, **new_results}
    print_vectors_dim(results.values())
    return results

def update_vectors_cache(new_results,model_name):
    cache_dir = join(root_path, "cache/process/embeddings")
    model_cache_file = join(cache_dir, f"{model_name}.npz")
    
    if exists(model_cache_file):
        #do not reaload, rely on existing load
        cache = vectors_cache[model_name]
        nb_existing = len(cache.keys())
    else:
        makedirs(cache_dir, exist_ok=True)
        cache = {}
        nb_existing = 0
    nb_new = len(new_results.keys())
    cache.update(new_results)
    nb_total = len(cache.keys())
    nb_added = nb_total - nb_existing
    if(nb_added > 0):
        np.savez(model_cache_file, **cache)
        print(f"saved '{model_name}' vectors cache. Added {nb_added} vectors. {nb_existing} -> {nb_total}")
    else:
        print(f"unexpeted all {nb_new} new vectors already exist in cache Total {nb_total} unchanged")
    return

def load_vectors_cache():
    cache = {}
    for model_name in models_list:
        model_cache_file = join(root_path,f"cache/process/embeddings/{model_name}.npz")
        if(exists(model_cache_file)):
            cache[model_name] = dict(np.load(model_cache_file))
            print(f"loaded '{model_name}' vectors cache file with {len(cache[model_name].keys())} vectors")
    return cache

models_list = [
    "all-MiniLM-L6-V2",
    "all-mpnet-base-v2",
    "text-embedding-3-small",
    "text-embedding-3-large"
]

providers = {
    "SentenceTransformer":[
            "all-MiniLM-L6-V2",
            "all-mpnet-base-v2"
    ],
    "openai":[
        "text-embedding-3-small",
        "text-embedding-3-large"
    ]
}

vectors_cache = load_vectors_cache()
