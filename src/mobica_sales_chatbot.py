import os
import random
import streamlit as st
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
    st.error("OpenRouter API key not found. Check your .env file for 'open_router_api'.")
    st.stop()

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
        st.error(f"Error connecting to Neo4j: {e}")
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
        st.error(f"Error generating response: {e}")
        return f"An error occurred: {str(e)}"

# Streamlit UI
st.title("💬 Mobica Sales Chatbot")
user_question = st.text_input("Ask me anything about Mobica's products:")
if st.button("Get Answer"):
    if user_question:
        query_type, language = classify_question_with_llm(user_question)
        context = retrieve_from_neo4j()
        answer = generate_response(user_question, context if query_type == "specific" else None, query_type, language)
        st.write("### Response:")
        st.write(answer)
    else:
        st.warning("Please enter a question!")
