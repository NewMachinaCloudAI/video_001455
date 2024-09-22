import time
from pinecone import Pinecone, ServerlessSpec

pc = Pinecone( api_key="YOUR-API-KEY" )

# Create Index if not already created
if 'my-index' not in pc.list_indexes().names():
    pc.create_index(
        name='my-index', 
        dimension=3, 
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )
     
    while not pc.describe_index('my-index').index.status['ready']:
        time.sleep(1)
    
    print("Pinecone Index provisioned")
else:
    print("Pinecone Index Already Provisioned")

