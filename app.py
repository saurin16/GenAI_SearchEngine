import streamlit as st
from langchain.agents import initialize_agent, AgentType, load_tools
from langchain.agents import tool
from langchain.agents import AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the SerpAPI key from environment variables
serpapi_api_key = os.getenv("SERPAPI_API_KEY")

# If you don't have the environment variable set, you can set it manually for testing
if not serpapi_api_key:
    serpapi_api_key = ""  # Fallback if the env variable is not set

# Initialize Arxiv and Wikipedia Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=600)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=600)
wiki = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Load SerpAPI tool using the API key
tools = load_tools(["serpapi"], serpapi_api_key=serpapi_api_key)

# Streamlit UI
st.title("🔎 LangChain - Dynamic Chatbot with Search")

"""
This chatbot integrates Wikipedia, Arxiv, and SerpAPI to fetch the latest information dynamically.
Try asking anything and I'll search for the most relevant information!
"""

# Sidebar Settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:", type="password")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a chatbot who can search the web. How can I help you?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User Input
if prompt := st.chat_input(placeholder="Ask me anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Initialize LLM
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)

    # Add tools to list (including SerpAPI, Arxiv, and Wikipedia)
    active_tools = tools + [arxiv, wiki]

    # Initialize LangChain agent with a single attempt per tool
    search_agent = initialize_agent(
        active_tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,  # Add this to handle output parsing errors
        max_iterations=3 # Limit to only one attempt per tool
    )

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])

        # If the response is empty or non-specific, provide a general fallback
        if not response not in response.lower():
            response = "I'm sorry, I couldn't find relevant information. Can you try asking in a different way?"

        # Store response in session
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)
