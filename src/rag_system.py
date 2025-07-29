# import os
# from dotenv import load_dotenv
# from neo4j import GraphDatabase
# from langchain_openai import ChatOpenAI  # Updated import
# from langchain.prompts import ChatPromptTemplate

# # Load environment variables
# load_dotenv()

# # Get API key from environment
# openai_api_key = os.getenv('open_router_api')  # Make sure this matches your .env variable name

# if not openai_api_key:
#     raise ValueError("OpenAI API key not found. Check your .env file.")

# # Neo4j connection parameters
# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = os.getenv('NEO4J_PASSWORD', '12345678')

# def retrieve_from_neo4j(question):
#     """Retrieve product information from Neo4j database"""
#     try:
#         driver = GraphDatabase.driver(uri, auth=(user, password))
#         query = """
#         MATCH (p:Product)
#         WHERE toLower($question) CONTAINS toLower(p.name)
#         RETURN p.name AS name, p.description AS description, p.pdf_path AS pdf LIMIT 1
#         """
#         with driver.session() as session:
#             result = session.run(query, question=question).data()
#         driver.close()
#         return result[0] if result else None
#     except Exception as e:
#         print(f"Error connecting to Neo4j: {e}")
#         return None

# def generate_response(question, context):
#     """Generate response using LangChain and OpenAI"""
#     try:
#         # Updated to use the correct import
#         llm = ChatOpenAI(openai_api_key=openai_api_key, model="mistralai/mistral-7b-instruct")
#         # Changed parameter name to api_key
        
#         template = """
#         Answer based only on the context provided:
        
#         Product: {name}
#         Description: {description}
#         PDF Path: {pdf}
        
#         Question: {question}
#         Answer:
#         """
#         prompt = ChatPromptTemplate.from_template(template)
#         formatted_prompt = prompt.format(
#             name=context["name"],
#             description=context["description"],
#             pdf=context["pdf"],
#             question=question
#         )
#         response = llm.invoke(formatted_prompt)
#         return response.content
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     user_question = input("Enter your question: ")
#     context = retrieve_from_neo4j(user_question)
    
#     if context:
#         try:
#             answer = generate_response(user_question, context)
#             print("Answer:", answer)
#         except Exception as e:
#             print(f"Error: {e}")
#     else:
#         print("No data found for this question.")

# import os
# from dotenv import load_dotenv
# from neo4j import GraphDatabase
# from langchain_community.chat_models import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate

# # Load environment variables
# load_dotenv()

# # Get OpenRouter API key from environment
# open_router_api = os.getenv('open_router_api')

# if not open_router_api:
#     raise ValueError("OpenRouter API key not found. Check your .env file for 'open_router_api'.")

# # Neo4j connection parameters
# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = os.getenv('NEO4J_PASSWORD', '12345678')

# def retrieve_from_neo4j(question):
#     """Retrieve product information from Neo4j database"""
#     try:
#         driver = GraphDatabase.driver(uri, auth=(user, password))
#         query = """
#         MATCH (p:Product)
#         WHERE toLower($question) CONTAINS toLower(p.name)
#         RETURN p.name AS name, p.description AS description, p.pdf_path AS pdf LIMIT 1
#         """
#         with driver.session() as session:
#             result = session.run(query, question=question).data()
#         driver.close()
#         return result[0] if result else None
#     except Exception as e:
#         print(f"Error connecting to Neo4j: {e}")
#         return None

# def generate_response(question, context):
#     """Generate response using LangChain and OpenRouter"""
#     try:
#         # Configure ChatOpenAI to use OpenRouter
#         llm = ChatOpenAI(
#             openai_api_base="https://openrouter.ai/api/v1",
#             openai_api_key=open_router_api,
#             model="mistralai/mistral-7b-instruct" # You can change this to any model supported by OpenRouter
#         )
        
#         template = """
#         Answer based only on the context provided:
        
#         Product: {name}
#         Description: {description}
#         PDF Path: {pdf}
        
#         Question: {question}
#         Answer:
#         """
#         prompt = ChatPromptTemplate.from_template(template)
#         formatted_prompt = prompt.format(
#             name=context["name"],
#             description=context["description"],
#             pdf=context["pdf"],
#             question=question
#         )
#         response = llm.invoke(formatted_prompt)
#         return response.content
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     user_question = input("Enter your question: ")
#     context = retrieve_from_neo4j(user_question)
    
#     if context:
#         try:
#             answer = generate_response(user_question, context)
#             print("Answer:", answer)
#         except Exception as e:
#             print(f"Error: {e}")
#     else:
#         print("No data found for this question.")

# import os
# from dotenv import load_dotenv
# from neo4j import GraphDatabase
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate

# # Load environment variables
# load_dotenv()

# # Get OpenRouter API key from environment
# open_router_api = os.getenv('open_router_api')

# if not open_router_api:
#     raise ValueError("OpenRouter API key not found. Check your .env file for 'open_router_api'.")

# # Neo4j connection parameters
# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = os.getenv('NEO4J_PASSWORD', '12345678')

# def retrieve_from_neo4j(question):
#     """Retrieve product information from Neo4j database"""
#     try:
#         driver = GraphDatabase.driver(uri, auth=(user, password))
#         query = """
#         MATCH (p:Product)
#         WHERE toLower($question) CONTAINS toLower(p.name)
#         RETURN p.name AS name, p.description AS description, p.pdf_path AS pdf LIMIT 1
#         """
#         with driver.session() as session:
#             result = session.run(query, question=question).data()
#         driver.close()
#         return result[0] if result else None
#     except Exception as e:
#         print(f"Error connecting to Neo4j: {e}")
#         return None

# def generate_response(question, context):
#     """Generate response using LangChain and OpenRouter"""
#     try:
#         # Configure ChatOpenAI to use OpenRouter
#         llm = ChatOpenAI(
#             openai_api_base="https://openrouter.ai/api/v1",
#             openai_api_key=open_router_api,
#             model="mistralai/mistral-7b-instruct" # You can change this to any model supported by OpenRouter
#         )
        
#         template = """
#         Answer based only on the context provided:
        
#         Product: {name}
#         Description: {description}
#         PDF Path: {pdf}
        
#         Question: {question}
#         Answer:
#         """
#         prompt = ChatPromptTemplate.from_template(template)
#         formatted_prompt = prompt.format(
#             name=context["name"],
#             description=context["description"],
#             pdf=context["pdf"],
#             question=question
#         )
#         response = llm.invoke(formatted_prompt)
#         return response.content
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     user_question = input("Enter your question: ")
#     context = retrieve_from_neo4j(user_question)
    
#     if context:
#         try:
#             answer = generate_response(user_question, context)
#             print("Answer:", answer)
#         except Exception as e:
#             print(f"Error: {e}")
#     else:
#         print("No data found for this question.")
# import os
# from dotenv import load_dotenv
# from neo4j import GraphDatabase
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# import re

# # Load environment variables
# load_dotenv()

# # Get OpenRouter API key from environment
# open_router_api = os.getenv('open_router_api')

# if not open_router_api:
#     raise ValueError("OpenRouter API key not found. Check your .env file for 'open_router_api'.")

# # Neo4j connection parameters
# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = os.getenv('NEO4J_PASSWORD', '12345678')

# # List of generic question patterns
# generic_patterns = [
#     r"what products does mobica offer", r"details about mobica", r"furniture solutions",
#     r"do you offer", r"price range", r"can i get a discount", r"do you ship", r"compare to ikea",
#     r"recommend", r"durable", r"sustainable", r"eco-friendly", r"warranty policy",
#     r"payment options", r"custom color", r"delivery time", r"assembly and installation",
#     r"reseller", r"best furniture solutions", r"home office", r"conference room"
# ]

# def classify_question(question):
#     """Classify question as generic or specific based on patterns."""
#     for pattern in generic_patterns:
#         if re.search(pattern, question, re.IGNORECASE):
#             return "generic"
#     return "specific"

# def retrieve_from_neo4j(question):
#     """Retrieve product information from Neo4j database for specific queries"""
#     try:
#         driver = GraphDatabase.driver(uri, auth=(user, password))
#         query = """
#         MATCH (p:Product)
#         WHERE toLower($question) CONTAINS toLower(p.name)
#         RETURN p.name AS name, p.description AS description, p.pdf_path AS pdf LIMIT 1
#         """
#         with driver.session() as session:
#             result = session.run(query, question=question).data()
#         driver.close()
#         return result[0] if result else None
#     except Exception as e:
#         print(f"Error connecting to Neo4j: {e}")
#         return None

# def generate_response(question, context, query_type):
#     """Generate response using LangChain and OpenRouter"""
#     try:
#         # Configure ChatOpenAI to use OpenRouter
#         llm = ChatOpenAI(
#             openai_api_base="https://openrouter.ai/api/v1",
#             openai_api_key=open_router_api,
#             model="mistralai/mistral-7b-instruct"
#         )
        
#         if query_type == "specific":
#             template = """
#             You are a knowledgeable and persuasive sales agent. Provide detailed, accurate, and engaging responses about the customer's specific product inquiry.
            
#             Context:
#             Product: {name}
#             Description: {description}
#             PDF Path: {pdf}
            
#             Customer Question: {question}
            
#             Your Response:
#             - Give precise details about the product.
#             - Highlight key features and benefits.
#             - If applicable, suggest related products.
#             - Offer additional assistance if needed.
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 name=context["name"],
#                 description=context["description"],
#                 pdf=context["pdf"],
#                 question=question
#             )
#         else:
#             template = """
#             You are an expert sales agent at Mobica, a premium furniture company. Answer customer inquiries about Mobica's products and services.
            
#             Customer Question: {question}
            
#             Your Response:
#             - Provide a comprehensive overview of Mobica's furniture solutions.
#             - Highlight the key benefits and best-selling products.
#             - Mention any available offers, bulk discounts, and shipping options.
#             - Offer guidance on choosing the best furniture for different needs (offices, hotels, home offices, etc.).
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 question=question
#             )
        
#         response = llm.invoke(formatted_prompt)
#         return response.content
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     user_question = input("Enter your question: ")
#     query_type = classify_question(user_question)
    
#     if query_type == "specific":
#         context = retrieve_from_neo4j(user_question)
#         if context:
#             answer = generate_response(user_question, context, query_type)
#         else:
#             answer = "No data found for this specific product. Can I help you with something else?"
#     else:
#         answer = generate_response(user_question, None, query_type)
    
#     print("Answer:", answer)

# import os
# from dotenv import load_dotenv
# from neo4j import GraphDatabase
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# import re

# # Load environment variables
# load_dotenv()

# # Get OpenRouter API key from environment
# open_router_api = os.getenv('open_router_api')

# if not open_router_api:
#     raise ValueError("OpenRouter API key not found. Check your .env file for 'open_router_api'.")

# # Neo4j connection parameters
# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = os.getenv('NEO4J_PASSWORD', '12345678')

# # List of generic question patterns
# generic_patterns = [
#     r"what products does mobica offer", r"details about mobica", r"furniture solutions",
#     r"do you offer", r"price range", r"can i get a discount", r"do you ship", r"compare to ikea",
#     r"recommend", r"durable", r"sustainable", r"eco-friendly", r"warranty policy",
#     r"payment options", r"custom color", r"delivery time", r"assembly and installation",
#     r"reseller", r"best furniture solutions", r"home office", r"conference room"
# ]

# def classify_question(question):
#     """Classify question as generic or specific based on patterns."""
#     for pattern in generic_patterns:
#         if re.search(pattern, question, re.IGNORECASE):
#             return "generic"
#     return "specific"

# def retrieve_from_neo4j(question):
#     """Retrieve product information from Neo4j database for specific queries"""
#     try:
#         driver = GraphDatabase.driver(uri, auth=(user, password))
#         query = """
#         MATCH (p:Product)
#         WHERE toLower($question) CONTAINS toLower(p.name)
#         RETURN p.name AS name, p.description AS description, p.pdf_path AS pdf LIMIT 1
#         """
#         with driver.session() as session:
#             result = session.run(query, question=question).data()
#         driver.close()
#         return result[0] if result else None
#     except Exception as e:
#         print(f"Error connecting to Neo4j: {e}")
#         return None

# def generate_response(question, context, query_type):
#     """Generate response using LangChain and OpenRouter"""
#     try:
#         # Configure ChatOpenAI to use OpenRouter
#         llm = ChatOpenAI(
#             openai_api_base="https://openrouter.ai/api/v1",
#             openai_api_key=open_router_api,
#             model="mistralai/mistral-7b-instruct"
#         )
        
#         if query_type == "specific":
#             template = """
#             You are a friendly and knowledgeable sales agent, providing clear and engaging responses.
#             Speak naturally, as if you're talking to a customer in person.
            
#             Customer Question: {question}
            
#             Here's what you should do:
#             - Greet the customer in a warm and engaging way.
#             - Provide clear and helpful details about the product.
#             - Highlight key benefits and practical uses.
#             - If applicable, suggest related products in a helpful manner.
#             - Close the conversation in a friendly way, offering further assistance.
            
#             Product Name: {name}
#             Description: {description}
#             PDF Link: {pdf}
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 name=context["name"],
#                 description=context["description"],
#                 pdf=context["pdf"],
#                 question=question
#             )
#         else:
#             template = """
#             You are an experienced sales agent at Mobica, guiding customers to find the best furniture for their needs.
#             Respond conversationally and naturally, adjusting to their specific inquiry.
            
#             Customer Question: {question}
            
#             Here's what you should do:
#             - Start with a friendly greeting that fits the context.
#             - Provide useful and engaging information tailored to the customer's request.
#             - If applicable, mention any promotions, discounts, or additional benefits.
#             - Offer personalized recommendations based on their needs (office, hotel, home, etc.).
#             - Keep it natural and conversational, like a real sales chat.
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 question=question
#             )
        
#         response = llm.invoke(formatted_prompt)
#         return response.content
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     user_question = input("Enter your question: ")
#     query_type = classify_question(user_question)
    
#     if query_type == "specific":
#         context = retrieve_from_neo4j(user_question)
#         if context:
#             answer = generate_response(user_question, context, query_type)
#         else:
#             answer = "No data found for this specific product. Can I help you with something else?"
#     else:
#         answer = generate_response(user_question, None, query_type)
    
#     print("Answer:", answer)
# import os
# from dotenv import load_dotenv
# from neo4j import GraphDatabase
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# import re
# import json

# # Load environment variables
# load_dotenv()

# # Get OpenRouter API key from environment
# open_router_api = os.getenv('open_router_api')

# if not open_router_api:
#     raise ValueError("OpenRouter API key not found. Check your .env file for 'open_router_api'.")

# # Neo4j connection parameters
# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = os.getenv('NEO4J_PASSWORD', '12345678')

# # List of generic question patterns
# generic_patterns = [
#     r"what products does mobica offer", r"details about mobica", r"furniture solutions",
#     r"do you offer", r"price range", r"can i get a discount", r"do you ship", r"compare to ikea",
#     r"recommend", r"durable", r"sustainable", r"eco-friendly", r"warranty policy",
#     r"payment options", r"custom color", r"delivery time", r"assembly and installation",
#     r"reseller", r"best furniture solutions", r"home office", r"conference room",
#     r"I run a .*? office", r"We need .*? chairs", r"What are your suggestions", r"collaborative workspaces"
# ]

# def classify_question(question):
#     """Classify question as generic or specific based on patterns."""
#     for pattern in generic_patterns:
#         if re.search(pattern, question, re.IGNORECASE):
#             return "generic"
#     return "specific"

# def retrieve_from_neo4j():
#     """Retrieve workspace solutions for general inquiries"""
#     try:
#         driver = GraphDatabase.driver(uri, auth=(user, password))
#         query = """
#         MATCH (p:Product)
#         WHERE p.name CONTAINS 'workspace' OR p.description CONTAINS 'workspace'
#         RETURN p.name AS name, p.description AS description, p.finishes AS finishes,
#                p.dimensions AS dimensions, p.image_paths AS images LIMIT 5
#         """
#         with driver.session() as session:
#             results = session.run(query).data()
#         driver.close()
#         return results
#     except Exception as e:
#         print(f"Error connecting to Neo4j: {e}")
#         return None

# def ensure_list(value):
#     """Ensure that a retrieved value is always a list"""
#     if isinstance(value, list):
#         return value
#     if isinstance(value, str):
#         return [value]  # Convert single string to list
#     return []  # Default empty list

# def generate_response(question, context, query_type):
#     """Generate response using LangChain and OpenRouter"""
#     try:
#         # Configure ChatOpenAI to use OpenRouter
#         llm = ChatOpenAI(
#             openai_api_base="https://openrouter.ai/api/v1",
#             openai_api_key=open_router_api,
#             model="mistralai/mistral-7b-instruct"
#         )
        
#         if query_type == "specific":
#             template = """
#             You are a friendly and knowledgeable sales agent, providing clear and engaging responses.
#             Speak naturally, as if you're talking to a customer in person.
            
#             Customer Question: {question}
            
#             Here's what you should do:
#             - Greet the customer in a warm and engaging way.
#             - Provide clear and helpful details about the product.
#             - Highlight key benefits and practical uses.
#             - Mention available finishes and dimensions.
#             - Show the product images to help the customer visualize it.
#             - If applicable, suggest related products in a helpful manner.
#             - Close the conversation in a friendly way, offering further assistance.
            
#             Product Name: {name}
#             Description: {description}
#             Finishes: {finishes}
#             Dimensions: {dimensions}
#             Image Paths: {images}
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 name=context.get("name", "Unknown Product"),
#                 description=context.get("description", "No description available"),
#                 finishes=', '.join(ensure_list(context.get("finishes", []))),
#                 dimensions=', '.join(ensure_list(context.get("dimensions", []))),
#                 images='\n'.join(ensure_list(context.get("images", []))),
#                 question=question
#             )
#         else:
#             workspace_products = retrieve_from_neo4j()
#             product_info = "\n\n".join([
#                 f"- **{prod['name']}**\n  *Description:* {prod.get('description', 'No description available')}\n  *Finishes:* {', '.join(ensure_list(prod.get('finishes', [])))}\n  *Dimensions:* {', '.join(ensure_list(prod.get('dimensions', [])))}\n  *Images:* {', '.join(ensure_list(prod.get('images', [])))}" 
#                 for prod in workspace_products]) if workspace_products else ""
            
#             template = """
#             You are an experienced sales agent at Mobica, guiding customers to find the best furniture for their needs.
#             Respond conversationally and naturally, adjusting to their specific inquiry.
            
#             Customer Question: {question}
            
#             Here's what you should do:
#             - Start with a friendly greeting that fits the context.
#             - Provide useful and engaging information tailored to the customer's request.
#             - Suggest relevant furniture solutions based on the customer's needs.
#             - Mention any promotions, discounts, or additional benefits if applicable.
#             - Keep it natural and conversational, like a real sales chat.
            
#             Here are some recommendations:
#             {product_info}
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 question=question,
#                 product_info=product_info
#             )
        
#         response = llm.invoke(formatted_prompt)
#         return response.content
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     user_question = input("Enter your question: ")
#     query_type = classify_question(user_question)
    
#     if query_type == "specific":
#         context = retrieve_from_neo4j()
#         if context:
#             answer = generate_response(user_question, context, query_type)
#         else:
#             answer = "No data found for this specific product. Can I help you with something else?"
#     else:
#         answer = generate_response(user_question, None, query_type)
    
#     print("Answer:", answer)

#### best 
# import os
# import random
# from dotenv import load_dotenv
# from neo4j import GraphDatabase
# from langchain_openai import ChatOpenAI
# from langchain.prompts import ChatPromptTemplate
# import json

# # Load environment variables
# load_dotenv()

# # Get OpenRouter API key from environment
# open_router_api = os.getenv('open_router_api')

# if not open_router_api:
#     raise ValueError("OpenRouter API key not found. Check your .env file for 'open_router_api'.")

# # Neo4j connection parameters
# uri = "bolt://localhost:7687"
# user = "neo4j"
# password = os.getenv('NEO4J_PASSWORD', '12345678')

# def classify_question_with_llm(question):
#     """Use LLM to classify whether a question is specific or general."""
#     llm = ChatOpenAI(
#         openai_api_base="https://openrouter.ai/api/v1",
#         openai_api_key=open_router_api,
#         model="mistralai/mistral-7b-instruct"
#     )
    
#     prompt = """
#     Classify the following customer question as either 'specific' (if it is asking about a specific product) 
#     or 'generic' (if it is a general inquiry about furniture solutions, pricing, availability, etc.).
    
#     Question: {question}
    
#     Answer only with 'specific' or 'generic'.
#     """
#     formatted_prompt = ChatPromptTemplate.from_template(prompt).format(question=question)
#     response = llm.invoke(formatted_prompt)
    
#     return response.content.strip().lower()

# def retrieve_from_neo4j():
#     """Retrieve workspace solutions for general inquiries"""
#     try:
#         driver = GraphDatabase.driver(uri, auth=(user, password))
#         query = """
#         MATCH (p:Product)
#         RETURN p.name AS name, p.description AS description, p.finishes AS finishes,
#                p.dimensions AS dimensions, p.image_paths AS images LIMIT 5
#         """
#         with driver.session() as session:
#             results = session.run(query).data()
#         driver.close()
#         return results if results else None
#     except Exception as e:
#         print(f"Error connecting to Neo4j: {e}")
#         return None

# def ensure_list(value):
#     """Ensure that a retrieved value is always a list"""
#     if isinstance(value, list):
#         return value
#     if isinstance(value, str):
#         return [value]  # Convert single string to list
#     return []  # Default empty list

# def generate_response(question, context, query_type):
#     """Generate response using LangChain and OpenRouter"""
#     try:
#         llm = ChatOpenAI(
#             openai_api_base="https://openrouter.ai/api/v1",
#             openai_api_key=open_router_api,
#             model="mistralai/mistral-7b-instruct"
#         )
        
#         if query_type == "specific":
#             if isinstance(context, list):
#                 context = random.choice(context) if context else {}
            
#             template = """
#             You are a friendly and knowledgeable sales agent, providing clear and engaging responses.
#             Speak naturally, as if you're talking to a customer in person.
            
#             Customer Question: {question}
            
#             Here's what you should do:
#             - Greet the customer in a warm and engaging way.
#             - Provide clear and helpful details about the product.
#             - Highlight key benefits and practical uses.
#             - Mention available finishes and dimensions.
#             - Show the product images to help the customer visualize it.
#             - If applicable, suggest related products in a helpful manner.
#             - Close the conversation in a friendly way, offering further assistance.
            
#             Product Name: {name}
#             Description: {description}
#             Finishes: {finishes}
#             Dimensions: {dimensions}
#             Image Paths: {images}
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 name=context.get("name", "Unknown Product"),
#                 description=context.get("description", "No description available"),
#                 finishes=', '.join(ensure_list(context.get("finishes", []))),
#                 dimensions=', '.join(ensure_list(context.get("dimensions", []))),
#                 images='\n'.join(ensure_list(context.get("images", []))),
#                 question=question
#             )
#         else:
#             workspace_products = retrieve_from_neo4j()
#             if workspace_products:
#                 selected_products = random.sample(workspace_products, min(3, len(workspace_products)))
#                 product_info = "\n\n".join([
#                     f"- **{prod['name']}**\n  *Description:* {prod.get('description', 'No description available')}\n  *Finishes:* {', '.join(ensure_list(prod.get('finishes', [])))}\n  *Dimensions:* {', '.join(ensure_list(prod.get('dimensions', [])))}\n  *Images:* {', '.join(ensure_list(prod.get('images', [])))}" 
#                     for prod in selected_products])
#             else:
#                 product_info = "No relevant products found."
            
#             template = """
#             You are an experienced sales agent at Mobica, guiding customers to find the best furniture for their needs.
#             Respond conversationally and naturally, adjusting to their specific inquiry.
            
#             Customer Question: {question}
            
#             Here's what you should do:
#             - Start with a friendly greeting that fits the context.
#             - Provide useful and engaging information tailored to the customer's request.
#             - Suggest relevant furniture solutions based on the customer's needs.
#             - Mention any promotions, discounts, or additional benefits if applicable.
#             - Keep it natural and conversational, like a real sales chat.
            
#             Here are some recommendations:
#             {product_info}
#             """
#             formatted_prompt = ChatPromptTemplate.from_template(template).format(
#                 question=question,
#                 product_info=product_info
#             )
        
#         response = llm.invoke(formatted_prompt)
#         return response.content
#     except Exception as e:
#         print(f"Error generating response: {e}")
#         return f"An error occurred: {str(e)}"

# if __name__ == "__main__":
#     user_question = input("Enter your question: ")
#     query_type = classify_question_with_llm(user_question)
    
#     context = retrieve_from_neo4j()
#     if query_type == "specific" and context:
#         answer = generate_response(user_question, context, query_type)
#     else:
#         answer = generate_response(user_question, None, query_type)
    
#     print("Answer:", answer)
import os
import random
from dotenv import load_dotenv
from neo4j import GraphDatabase
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
import json

# Load environment variables
load_dotenv()

# Get OpenRouter API key from environment
open_router_api = os.getenv('open_router_api')

if not open_router_api:
    raise ValueError("OpenRouter API key not found. Check your .env file for 'open_router_api'.")

# Neo4j connection parameters
uri = "bolt://localhost:7687"
user = "neo4j"
password = os.getenv('NEO4J_PASSWORD', '12345678')

def classify_question_with_llm(question):
    """Use LLM to classify whether a question is specific or general and detect the language."""
    llm = ChatOpenAI(
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=open_router_api,
        model="mistralai/mistral-7b-instruct"
    )
    
    prompt = """
    Classify the following customer question by determining:
    - Whether it is 'specific' (about a particular product) or 'generic' (general inquiry about furniture solutions, pricing, availability, etc.).
    - The language of the question (English or Arabic).
    
    Question: {question}
    
    Answer only in this format: "category: [specific/generic], language: [English/Arabic]".
    """
    formatted_prompt = ChatPromptTemplate.from_template(prompt).format(question=question)
    response = llm.invoke(formatted_prompt).content.strip().lower()
    
    category, language = response.split(", ")
    return category.split(": ")[1], language.split(": ")[1]

def retrieve_from_neo4j():
    """Retrieve workspace solutions for general inquiries"""
    try:
        driver = GraphDatabase.driver(uri, auth=(user, password))
        query = """
        MATCH (p:Product)
        RETURN p.name AS name, p.description AS description, p.finishes AS finishes,
               p.dimensions AS dimensions, p.image_paths AS images LIMIT 5
        """
        with driver.session() as session:
            results = session.run(query).data()
        driver.close()
        return results if results else None
    except Exception as e:
        print(f"Error connecting to Neo4j: {e}")
        return None

def ensure_list(value):
    """Ensure that a retrieved value is always a list"""
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [value]  # Convert single string to list
    return []  # Default empty list

def generate_response(question, context, query_type, language):
    """Generate response using LangChain and OpenRouter"""
    try:
        llm = ChatOpenAI(
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=open_router_api,
            model="mistralai/mistral-7b-instruct"
        )
        
        if query_type == "specific":
            if isinstance(context, list):
                context = random.choice(context) if context else {}
            
            template = """
            You are a friendly and knowledgeable sales agent, providing clear and engaging responses.
            Speak naturally, as if you're talking to a customer in person.
            Answer in {language}.
            
            Customer Question: {question}
            
            Here's what you should do:
            - Greet the customer in a warm and engaging way.
            - Provide clear and helpful details about the product.
            - Highlight key benefits and practical uses.
            - Mention available finishes and dimensions.
            - Show the product images to help the customer visualize it.
            - If applicable, suggest related products in a helpful manner.
            - Close the conversation in a friendly way, offering further assistance.
            
            Product Name: {name}
            Description: {description}
            Finishes: {finishes}
            Dimensions: {dimensions}
            Image Paths: {images}
            """
            formatted_prompt = ChatPromptTemplate.from_template(template).format(
                name=context.get("name", "Unknown Product"),
                description=context.get("description", "No description available"),
                finishes=', '.join(ensure_list(context.get("finishes", []))),
                dimensions=', '.join(ensure_list(context.get("dimensions", []))),
                images='\n'.join(ensure_list(context.get("images", []))),
                question=question,
                language=language.capitalize()
            )
        else:
            workspace_products = retrieve_from_neo4j()
            if workspace_products:
                selected_products = random.sample(workspace_products, min(3, len(workspace_products)))
                product_info = "\n\n".join([
                    f"- **{prod['name']}**\n  *Description:* {prod.get('description', 'No description available')}\n  *Finishes:* {', '.join(ensure_list(prod.get('finishes', [])))}\n  *Dimensions:* {', '.join(ensure_list(prod.get('dimensions', [])))}\n  *Images:* {', '.join(ensure_list(prod.get('images', [])))}" 
                    for prod in selected_products])
            else:
                product_info = "No relevant products found."
            
            template = """
            You are an experienced sales agent at Mobica, guiding customers to find the best furniture for their needs.
            Respond conversationally and naturally, adjusting to their specific inquiry.
            Answer in {language}.
            
            Customer Question: {question}
            
            Here's what you should do:
            - Start with a friendly greeting that fits the context.
            - Provide useful and engaging information tailored to the customer's request.
            - Suggest relevant furniture solutions based on the customer's needs.
            - Mention any promotions, discounts, or additional benefits if applicable.
            - Keep it natural and conversational, like a real sales chat.
            
            Here are some recommendations:
            {product_info}
            """
            formatted_prompt = ChatPromptTemplate.from_template(template).format(
                question=question,
                product_info=product_info,
                language=language.capitalize()
            )
        
        response = llm.invoke(formatted_prompt)
        return response.content
    except Exception as e:
        print(f"Error generating response: {e}")
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    user_question = input("Enter your question: ")
    query_type, language = classify_question_with_llm(user_question)
    
    context = retrieve_from_neo4j()
    if query_type == "specific" and context:
        answer = generate_response(user_question, context, query_type, language)
    else:
        answer = generate_response(user_question, None, query_type, language)
    
    print("Answer:", answer)