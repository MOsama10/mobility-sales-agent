Mobility Sales Agent
An intelligent, English-speaking sales assistant for mobility products (e.g., wheelchairs, scooters), powered by a knowledge graph and retrieval-augmented generation (RAG). This system assists users in selecting the right product by delivering accurate, context-aware responses based on structured domain knowledge.

🚀 Features

Knowledge Graph Construction: Builds a knowledge graph from structured data for robust product information management.
Contextual Question Answering: Utilizes RAG techniques to provide precise and relevant responses to user queries.
Modular Codebase: Organized Python codebase with clear separation of concerns for maintainability and scalability.
Extensible Design: Easily adaptable to other domains or product categories beyond mobility products.


🗂️ Project Structure
'''
mobility-sales-agent/
│
├── data/                    # Contains raw and intermediate data
│   ├── raw/                 # Manually curated datasets (JSON, CSV, etc.)
│
├── src/                     # Source code modules
│   ├── create_graph.py      # Builds the knowledge graph from raw data
│   ├── extract_data.py      # Extracts entities and relations from sources
│   ├── rag_system.py        # Main agent logic using RAG
│   └── utils.py             # Helper functions
│
├── tests/                   # Unit tests for agent components
│   └── test_openrouter.py
│
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (excluded from Git)
├── .gitignore               # Git ignore rules
└── README.md                # Project documentation
'''

📦 Setup
1. Clone the Repository
git clone https://github.com/MOsama10/mobility-sales-agent.git
cd mobility-sales-agent

2. Create a Virtual Environment (Optional but Recommended)
python -m venv .venv
.\.venv\Scripts\activate  # On Windows
source .venv/bin/activate # On macOS/Linux

3. Install Dependencies
pip install -r requirements.txt


⚙️ Usage

Note: Ensure the .env file is configured with required keys (e.g., OpenAI, Neo4j credentials) before proceeding.

Build the Knowledge Graph
python src/create_graph.py

Run the RAG-Based Sales Agent
python src/rag_system.py


🧠 Example Use Cases

Assist customers in selecting the optimal wheelchair based on budget, features, and specific needs.
Provide accurate answers to product-related questions using structured knowledge, surpassing static FAQs.
Deploy as part of online stores, kiosks, or customer support chatbots for enhanced user experience.


🤝 Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Submit a pull request with a clear description of your changes.

Please report issues or suggest improvements via the GitHub Issues page.
