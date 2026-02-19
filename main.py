from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
#from tavily import TavilyClient
from langchain_tavily import TavilySearch

# tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

# @tool
# def search(query: str) -> str:
#     """Search the web for information"""
#     print(f"Searching the web for information: {query}")
#     return tavily_client.search(query)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ.get("GOOGLE_API_KEY"))

#tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools)


def main():
    print("Hello from lang-hello!")
    response = agent.invoke({"messages": [HumanMessage(content="Serach for 3 Job openings in the field of AI and Machine Learning from Linkedin?")]})    
    print(f"Response: {response}")
 
if __name__ == "__main__":
    main()
