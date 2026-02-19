from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import GoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage



@tool
def search(query: str) -> str:
    """Search the web for information"""
    return "I found this information: " + query

llm = GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ.get("GOOGLE_API_KEY"))

tools = [search]
agent = create_agent(model=llm,tools=tools)


def main():
    print("Hello from lang-hello!")
    response = agent.invoke({"messages": [HumanMessage(content="What is the capital of India?")]})
    print(response)
 
if __name__ == "__main__":
    main()
