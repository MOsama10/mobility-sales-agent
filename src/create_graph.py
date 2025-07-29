# from neo4j import GraphDatabase
# import json

# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = "12345678"

# driver = GraphDatabase.driver(uri, auth=(user, password))

# def create_graph(tx, product):
#     tx.run("""
#         MERGE (p:Product {name: $product_name, description: $description, pdf_path: $pdf_path})
#         MERGE (c:Category {name: $category})
#         MERGE (s:Section {name: $section})
#         MERGE (p)-[:BELONGS_TO]->(c)
#         MERGE (c)-[:PART_OF]->(s)
#         """, product_name=product["product_name"],
#         description=product["description"],
#         pdf_path=product["pdf_path"],
#         category=product["category"],
#         section=product["section"])

# with open('data.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)

# with driver.session() as session:
#     for product in data:
#         session.execute_write(create_graph, product)

# driver.close()
import os
import json
from dotenv import load_dotenv
from neo4j import GraphDatabase

# Load environment variables
load_dotenv()

# Neo4j connection parameters
uri = "bolt://localhost:7687"
user = "neo4j"
password = os.getenv('NEO4J_PASSWORD', '12345678')

# Load the merged data file
file_path = "merged.json"
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

def create_graph(tx, product):
    """Create product nodes with relevant properties in Neo4j"""
    query = """
    MERGE (p:Product {name: $name})
    SET p.alternative_name = $alt_name,
        p.description = $description,
        p.finishes = $finishes,
        p.dimensions = $dimensions,
        p.image_paths = $images
    """
    tx.run(query, 
           name=product["Product Name"],
           alt_name=product.get("Second Name", ""),
           description=json.dumps(product.get("Description", {})),
           finishes=json.dumps(product.get("Finishes", [])),
           dimensions=json.dumps(product.get("Dimensions", [])),
           images=json.dumps(product.get("Image Paths", [])))

# Connect to Neo4j and insert data
driver = GraphDatabase.driver(uri, auth=(user, password))

with driver.session() as session:
    for product in data:
        session.execute_write(create_graph, product)

print("Data successfully inserted into Neo4j!")

driver.close()