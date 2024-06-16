import sqlite3
import utils as utl
from os import makedirs
from os.path import dirname

reserved_keys = ["order", "group", "select", "where", "join"]

def connect(db_file):
    path = dirname(db_file)
    if(path):
        makedirs(path, exist_ok=True)
    global conn
    conn = sqlite3.connect(db_file)
    return conn

def execute(command_text):
    cursor = conn.cursor()
    cursor.execute(command_text)
    conn.commit()
    return

def execute_file(fileName):
    print(f"executing file {fileName}")
    sql_command_text = utl.load_text(fileName)
    execute(sql_command_text)
    return

def create_table(sample_data, table_name, overwrite=True):
    fields = sample_data.keys()

    field_types = {}
    for key in fields:
        value = sample_data[key]
        if isinstance(value, int):
            field_types[key] = 'INTEGER'
        elif isinstance(value, float):
            field_types[key] = 'REAL'
        else:
            field_types[key] = 'TEXT'

    field_definitions = []
    for i, field in enumerate(fields):
        field_type = field_types[field]
        if field in reserved_keys:
            field = f'"{field}"'  # Enclose field name in quotes
        if i == 0:
            field_definition = f"{field} {field_type} PRIMARY KEY"
        else:
            field_definition = f"{field} {field_type}"
        field_definitions.append(field_definition)
    fields_statement = ", ".join(field_definitions)

    if overwrite:
        create_table_command_text = f"DROP TABLE IF EXISTS {table_name}; CREATE TABLE {table_name} ({fields_statement});"
    else:
        create_table_command_text = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields_statement});"

    print(f"executing create_table for '{table_name}'")
    print(create_table_command_text)
    #execute(create_table_command_text)
    return

def check_table(table_name):
    """Check if a table exists in the database."""
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
    result = cursor.fetchone()
    if(result is not None):
        print(f"{table_name} exists")
    else:
        print(f"{table_name} do not exist")
    return result

def insert_tuples(tuple_data):
    sql_insert = ''' INSERT INTO documents(sid, uid, path, url, url_type, slug, format, title, content_type, level, order)
                     VALUES(?,?,?,?,?,?,?,?,?,?,?) '''
    cursor = conn.cursor()
    cursor.executemany(sql_insert, tuple_data)
    conn.commit()

def json_to_tuples(json_data):
    return [(item['sid'], item['uid'], item['path'], item['url'], item['url_type'], item['slug'], 
             item['format'], item['title'], item['content_type'], item['level'], item['order']) for item in json_data]

def insert_data(data):
    tuple_data = json_to_tuples(data)
    insert_tuples(tuple_data)
    return

conn = None
