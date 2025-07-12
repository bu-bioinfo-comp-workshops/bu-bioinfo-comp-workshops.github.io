import os
import glob
import json
from llama_index import VectorStoreIndex, Document
from llama_index.core import StorageContext
from llama_index.storage.docstore.dynamodb import DynamoDBDocumentStore
from llama_index.storage.index_store.dynamodb import DynamoDBIndexStore
from llama_index.vector_stores.dynamodb import DynamoDBVectorStore

# Ensure AWS credentials are set in your environment or ~/.aws/credentials
TABLE_NAME = "llamaindex_scc"

DATA_DIR = "/home/labadorf/computational_workshop_generator/external_materials/scc"
INDEX_DIR = "/home/labadorf/computational_workshop_generator/external_materials/scc_index"

def load_json_documents(data_dir):
    docs = []
    for filepath in glob.glob(os.path.join(data_dir, "*.json")):
        with open(filepath, "r") as f:
            data = json.load(f)
            # If each file contains a list of records
            if isinstance(data, list):
                for record in data:
                    docs.append(Document(text=json.dumps(record), metadata={"source": filepath}))
            else:  # Single record per file
                docs.append(Document(text=json.dumps(data), metadata={"source": filepath}))
    return docs

if __name__ == "__main__":
    documents = load_json_documents(DATA_DIR)
    # Set up DynamoDB storage context
    storage_context = StorageContext.from_defaults(
        docstore=DynamoDBDocumentStore.from_table_name(table_name=TABLE_NAME),
        index_store=DynamoDBIndexStore.from_table_name(table_name=TABLE_NAME),
        vector_store=DynamoDBVectorStore.from_table_name(table_name=TABLE_NAME)
    )
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
    print(f"Index created and saved to DynamoDB table '{TABLE_NAME}'")
