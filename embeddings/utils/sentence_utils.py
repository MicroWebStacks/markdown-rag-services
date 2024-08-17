from os.path import abspath,dirname,join,exists
from os import makedirs
service_path = dirname(dirname(abspath(__file__)))
root_path = dirname(service_path)
from common import utils as utl
from sentence_transformers import SentenceTransformer
import warnings
from openai import OpenAI
import os
import time
from numpy.linalg import norm
import numpy as np

# Suppress specific FutureWarning from transformers
warnings.filterwarnings("ignore", message="`clean_up_tokenization_spaces` was not set. It will be set to `True` by default.", category=FutureWarning)

def text_list_encode_in_batches(text_list, model_name, batch_size=200):
    "100 1s ; 200 1.5s ; 500 2.5s"
    results = []
    batches = [text_list[i:i + batch_size] for i in range(0, len(text_list), batch_size)]
    total_tokens = 0
    for batch in batches:
        if model_name in providers["openai"]:
            start = time.time()
            response = client.embeddings.create(
                input=batch,
                model=model_name
            )
            batch_results = [item.embedding for item in response.data]
            results.extend(batch_results)
            print(f"Processed a batch of {len(batch)} texts, used tokens: {response.usage.total_tokens} in {utl.time_text(time.time()-start)}")
            total_tokens += response.usage.total_tokens
    return results,total_tokens

def text_list_encode(text_list,model_name="all-MiniLM-L6-V2"):
    create_models()
    if(model_name in providers["SentenceTransformer"]):
        results = models[model_name].encode(text_list, normalize_embeddings=True, show_progress_bar=True)
    elif(model_name in providers["openai"]):
        results,total_tokens = text_list_encode_in_batches(text_list,model_name)
        print(f"openai total used tokens : {total_tokens}")
    return results

def text_encode(text,model_name="all-MiniLM-L6-V2"):
    create_models()
    if(model_name in providers["SentenceTransformer"]):
        results = models[model_name].encode([text], normalize_embeddings=True)
        result = results[0]
    elif(model_name in providers["openai"]):
        start = time.time()
        response = client.embeddings.create(input = [text], model=model_name)
        result = response.data[0].embedding
        print(f"text_encode openai {model_name} ; used {response.usage.total_tokens} tokens in {utl.time_text(time.time()-start)}")
    return result

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b) / (norm(a) * norm(b))

def similarity(query_embedding, documents_embeddings,top_k):
    similarity_list = [cosine_similarity(query_embedding, doc) for doc in documents_embeddings]
    hash_similarity_pairs = [{'index': idx, 'similarity': score} for idx, score in enumerate(similarity_list)]
    sorted_pairs = sorted(hash_similarity_pairs, key=lambda x: x['similarity'], reverse=True)
    top_k_entries = sorted_pairs[:top_k]
    return top_k_entries

def model_similarity(query_embedding, documents_embeddings,model_name="all-MiniLM-L6-V2"):
    create_models()
    similarity = models[model_name].similarity(query_embedding, documents_embeddings)
    return similarity[0]

def create_models():
    global client
    global models
    if(client is not None):
        return
    for model_name in models_list:
        if(model_name in providers["SentenceTransformer"]):
            models[model_name] = SentenceTransformer(model_name)
        elif((model_name in providers["openai"]) and client is None):
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return models

models_list = [
    "all-MiniLM-L6-V2",
    "all-mpnet-base-v2",
    "text-embedding-3-small",
    "text-embedding-3-large"
]

providers = {"SentenceTransformer":[
            "all-MiniLM-L6-V2",
            "all-mpnet-base-v2"
        ],
        "openai":[
            "text-embedding-3-small",
            "text-embedding-3-large"
        ]
    }

client = None
models = {}
