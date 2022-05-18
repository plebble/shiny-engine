import os
import json
import sqlite3
from sqlite3 import Error

with open("creation-schema.json") as file:
    schema = json.load(file)
database_filepath = schema["payload"]["path"]["database"]
database_path = "/".join(database_filepath.split("/")[:-1])
database_filename = "/".join(database_filepath.split("/")[-1])

if not os.path.exists(database_path):
    print("h")
    os.makedirs("/".join(database_filepath.split("/")[:-1]))
    

connection = sqlite3.connect(database_filepath)