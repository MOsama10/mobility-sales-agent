

✅ mobility-sales-agent
------------------------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Mobility Sales Agent  An intelligent, English-speaking sales assistant for mobility products (e.g., wheelchairs, scooters), powered by a knowledge graph and retrieval-augmented generation (RAG). This system is designed to assist users in finding the right product by providing accurate, context-aware responses based on structured domain knowledge.  ---  ## 🚀 Features  - ✅ Knowledge graph construction from structured data.  - ✅ Contextual question answering using RAG techniques.  - ✅ Modular Python codebase with clear separation between components.  - ✅ Easily extendable to other domains or product categories.  ---  ## 🗂️ Project Structure   `

mobility-sales-agent/│├── data/ # Contains raw and intermediate data│ ├── raw/ # Manually curated raw datasets (JSON, CSV, etc.)│├── src/ # Source code modules│ ├── create\_graph.py # Builds the knowledge graph from raw data│ ├── extract\_data.py # Extracts entities and relations from sources│ ├── rag\_system.py # Main agent logic using RAG│ └── utils.py # Helper functions (formerly ddd.py)│├── tests/ # Unit tests for agent components│ └── test\_openrouter.py│├── requirements.txt # Python dependencies├── .env # Environment variables (excluded from Git)├── .gitignore # Git ignore rules└── README.md # Project documentation

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   ---  ## 📦 Setup  ### 1. Clone the repo  ```bash  git clone https://github.com/MOsama10/mobility-sales-agent.git  cd mobility-sales-agent   `

### 2\. Create virtual environment (optional but recommended)

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m venv .venv  .\.venv\Scripts\activate   # On Windows   `

### 3\. Install dependencies

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

⚙️ Usage
--------

> Make sure you have your .env file configured with the necessary keys (e.g., OpenAI, Neo4j, etc.).

### Build the knowledge graph

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python src/create_graph.py   `

### Run the RAG-based sales agent

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python src/rag_system.py   `

🧠 Example Use Cases
--------------------

*   Assisting customers in choosing the best wheelchair based on budget and features.
    
*   Answering product questions using structured knowledge instead of static FAQs.
    
*   Deployable in online stores, kiosks, or support chatbots.
    

🤝 Contributing
---------------

Feel free to fork the repo, suggest improvements, or open issues. Pull requests are welcome.

📄 License
----------

This project is open-source and available under the [MIT License](https://chatgpt.com/c/LICENSE).

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML``   ---  ### ✅ What to do next:  1. Copy this into your `README.md` in the root of the project.  2. Make sure you rename `ddd.py` to `utils.py` (or something clearer) if not already done.  3. Add a license file (optional but recommended): I can help generate MIT, Apache, etc.  هل تحب نضيف شارة GitHub Actions أو نسخة عربية مختصرة؟   ``
