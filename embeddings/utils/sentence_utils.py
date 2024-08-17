from sentence_transformers import SentenceTransformer

def text_list_encode(text_list,model_name="all-MiniLM-L6-V2"):
    results = models[model_name].encode(text_list, normalize_embeddings=True, show_progress_bar=True)
    return results

def create_models():
    models = {}
    for model_name in models_list:
        if(model_name in providers["SentenceTransformer"]):
            models[model_name] = SentenceTransformer(model_name)
    return models

models_list = [
    "all-MiniLM-L6-V2"
]

providers = {"SentenceTransformer":[
            "all-MiniLM-L6-V2"
        ],
        "openai":[
            "text-embedding-3-small",
            "text-embedding-3-large"
        ]
    }

models = create_models()
