import sys
sys.path.append("../common/utils")
import utils as utl
from os.path import join
import sqlite_utils as sql

CACHE_PATH = "../cache"

documents = utl.load_json(join(CACHE_PATH,"process/structure/test-website/document_list.json"))
print(f"imported {len(documents)} documents")

db_file = join(CACHE_PATH,"data/sqllite/markdown.db")
utl.make_dir(db_file)
db = sql.Database(db_file)

if(db['documents'].count == 0):
    db["documents"].insert_all(documents, pk='sid')

schema = db["documents"].schema
print(schema)

print(f"{db['documents'].count} documents available")
if(db['documents'].count != 0):
    print("first document")
    print(documents[0])
