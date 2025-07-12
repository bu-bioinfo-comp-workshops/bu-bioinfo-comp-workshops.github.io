from llama_index.core import StorageContext, load_index_from_storage
from llama_index.storage.docstore.dynamodb import DynamoDBDocumentStore
from llama_index.storage.index_store.dynamodb import DynamoDBIndexStore
from llama_index.vector_stores.dynamodb import DynamoDBVectorStore

# Ensure AWS credentials are set in your environment or ~/.aws/credentials
TABLE_NAME = "llamaindex_scc"

def query_index(query, top_k=5):
    storage_context = StorageContext.from_defaults(
        docstore=DynamoDBDocumentStore.from_table_name(table_name=TABLE_NAME),
        index_store=DynamoDBIndexStore.from_table_name(table_name=TABLE_NAME),
        vector_store=DynamoDBVectorStore.from_table_name(table_name=TABLE_NAME)
    )
    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine(similarity_top_k=top_k)
    response = query_engine.query(query)
    return response

if __name__ == "__main__":
    query = "Describe the main computational resources available at the BU SCC."
    result = query_index(query)
    print("Query:", query)
    print("Response:", result)
