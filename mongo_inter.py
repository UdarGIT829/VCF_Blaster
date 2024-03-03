import json
from pymongo import MongoClient

from blaster_rest import blast_sequence

def process_file(file_path):
    # Assuming you've extracted sequences from the VCF already, let's simulate it
    sequence = "ACTGCTAGCTAGCTAGCTCGATCGATGCTAGCTAGCTA"
    
    # BLAST the sequence using the API
    blast_result = blast_sequence(sequence)
    
    # Save the BLAST result to MongoDB or handle it as you need
    if blast_result:
        save_to_mongodb({"file": file_path, "blast_result": blast_result})
    else:
        print("Failed to get BLAST results for", file_path)

def save_to_mongodb(data):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['your_database']
    collection = db['your_collection']
    collection.insert_one(data)