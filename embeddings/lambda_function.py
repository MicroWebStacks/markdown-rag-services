import json
from sentence_transformers import SentenceTransformer
import warnings
# Suppress specific FutureWarning from transformers
warnings.filterwarnings("ignore", message="`clean_up_tokenization_spaces` was not set. It will be set to `True` by default.", category=FutureWarning)

model = SentenceTransformer('all-MiniLM-L6-v2')

def lambda_handler(event, context):
    sentence = event.get('sentence', '')
    embedding = model.encode(sentence, normalize_embeddings=True, convert_to_tensor=False)
    embedding_list = embedding.tolist()  # Convert numpy array to list
    return {
        'statusCode': 200,
        'body': json.dumps(embedding_list)
    }

if __name__ == "__main__":
    event = {'sentence': 'This is a test sentence'}
    context = {}
    print(f"testing with event: '{event}'")
    result = lambda_handler(event, context)
    embedding_list = json.loads(result['body'])
    print(f"status code : {result['statusCode']} ; body {len(embedding_list)} {type(embedding_list)}")
