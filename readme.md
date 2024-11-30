# 🔎 LangChain - Chat with Search

This is a Streamlit-based application that integrates LangChain, Groq, and multiple search utilities to create an interactive chatbot capable of searching the web, querying Arxiv for academic papers, and fetching content from Wikipedia. The chatbot is powered by LangChain's agents and tools for natural language processing tasks.

---

## 🛠 Features
1. **Web Search**: Search the web using DuckDuckGo for quick and relevant answers.
2. **Arxiv Query**: Fetch academic paper summaries directly from Arxiv.
3. **Wikipedia Search**: Retrieve concise Wikipedia content based on your queries.
4. **Streamlined Conversation**: Interact with a chatbot that combines search tools to provide comprehensive answers.
5. **Error Handling**: Handles LLM output parsing errors gracefully, with fallback mechanisms for robustness.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/langchain-chat-search.git
cd langchain-chat-search
```

### 2. Set Up the Environment
Ensure you have Python 3.8+ installed.

1. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Add `.env` file**:
   Create a `.env` file in the project root and add your Groq API key:
   ```plaintext
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```

### 3. Run the Application
Start the Streamlit app:
```bash
streamlit run app.py
```

---

## 📖 How It Works

### **Tools Integrated**
1. **DuckDuckGo Search**:
   - Fetches search results for general queries.
   - Tool: `DuckDuckGoSearchRun`

2. **Arxiv Query**:
   - Retrieves academic paper summaries.
   - Tool: `ArxivAPIWrapper` and `ArxivQueryRun`

3. **Wikipedia Search**:
   - Fetches concise Wikipedia summaries.
   - Tool: `WikipediaAPIWrapper` and `WikipediaQueryRun`

### **Agent**
The app uses LangChain's `ZERO_SHOT_REACT_DESCRIPTION` agent type, which dynamically selects the appropriate tool based on user input.

---

## 🔧 Error Handling
- **Output Parsing Failures**: Handles unexpected responses from the LLM gracefully with retries or fallback messages.
- **Missing API Key**: Displays an error if the `.env` file is misconfigured or the Groq API key is missing.

---

## 🖼 App UI
### **Main Features**
- **Chat Interface**: Users can input questions and view responses in a conversational format.
- **Search and Retrieval**: Integrates with tools to provide accurate and concise answers.

### **Sidebar**
- Displays app settings and notifies users that the developer's Groq API key is being used.

---

## 📚 Dependencies
- `LangChain`
- `Streamlit`
- `langchain_groq`
- `python-dotenv`

Install them via the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

---

## 🐛 Troubleshooting
### Common Issues:
1. **ValueError: An output parsing error occurred**:
   - Ensure `handle_parsing_errors=True` is enabled in the agent initialization.
   - Check if the prompts are well-structured and explicit.

2. **Groq API Key Missing**:
   - Verify that the `.env` file contains the correct `GROQ_API_KEY`.

3. **Dependency Errors**:
   - Run `pip install --upgrade langchain langchain-core` to ensure you have the latest versions.

---

## 🙌 Contributing
Contributions are welcome! Feel free to submit issues or pull requests to improve this project.

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Enjoy exploring the web with your personalized chatbot! 😊