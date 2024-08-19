import json
from sentence_transformers import SentenceTransformer
import time
import warnings
from os.path import abspath,dirname,join,exists
# Suppress specific FutureWarning from transformers
warnings.filterwarnings("ignore", message="`clean_up_tokenization_spaces` was not set. It will be set to `True` by default.", category=FutureWarning)

def time_text(duration):
    duration = abs(duration)
    milliseconds = int((duration - int(duration)) * 1000)
    seconds = int(duration) % 60
    minutes = (int(duration) // 60) % 60
    hours = (int(duration) // 60) // 60
    text = ""
    if(hours > 0):
        text += f"{hours} h "
    if(minutes > 0):
        text += f"{minutes} mn "
    if(seconds > 0):
        text += f"{seconds} s "
    if(milliseconds > 0):
        text += f"{milliseconds} ms "
    return text

start = time.time()
model_name = 'all-MiniLM-L6-v2'
print(f"Start loading model '{model_name}'")
model_path = join("/cache/models",model_name)
if(not exists(model_path)):
    print(f"model path not found '{model_path}'")
    exit(1)
model = SentenceTransformer(model_path,local_files_only=True)
print(f"Loaded model in {time_text(time.time()-start)}")

def lambda_handler(event, context):
    start = time.time()
    print(f"testing with event: '{event}'")
    sentence = event.get('sentence', '')
    embedding = model.encode(sentence, normalize_embeddings=True, convert_to_tensor=False)
    embedding_list = embedding.tolist()  # Convert numpy array to list
    print(f"status code : 200 ; body {len(embedding_list)} {type(embedding_list)} after {time_text(time.time()-start)}")
    return {
        'statusCode': 200,
        'body': json.dumps(embedding_list)
    }
