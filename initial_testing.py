import os
import json
import sqlite3
from sqlite3 import Error

def build_create_table_query()


def initialise_system(creation_schema_filepath):
	with open(creation_schema_filepath) as file:
		schema = json.load(file)
	database_filepath = schema["payload"]["path"]["database"]
	database_path = "/".join(database_filepath.split("/")[:-1])
	database_filename = "/".join(database_filepath.split("/")[-1])

	if not os.path.exists(database_path):
		print("h")
		os.makedirs("/".join(database_filepath.split("/")[:-1]))

	connection = sqlite3.connect(database_filepath)

	try:
		cursor = connection.cursor()

		cursor.execute("ffef")

		connection.commit()
	except connection.Error:
		print("Transaction failed, reverting...")

		connection.rollback()
	
initialise_system("creation-schema.json")