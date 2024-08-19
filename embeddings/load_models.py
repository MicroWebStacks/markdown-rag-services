from os.path import abspath,dirname,join,exists
from os import makedirs
from sentence_transformers import SentenceTransformer


models_list = [
                "all-MiniLM-L6-v2",     
                #"all-mpnet-base-v2",
                #"multi-qa-mpnet-base-dot-v1"
               ]

for model_name in models_list:
    service_path = dirname(abspath(__file__))
    root_path = dirname(service_path)
    model_path = join(root_path,"cache/models",model_name)
    if(not exists(model_path)):
        makedirs(model_path) 
        print(f"creating model {model_name}")
        model = SentenceTransformer(model_name)
        model.save(model_path)
    else:
        print(f"model {model_name} already exists")
