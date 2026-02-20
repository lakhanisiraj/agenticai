from dotenv import load_dotenv
import os
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from typing import List
from pydantic import BaseModel, Field
#from tavily import TavilyClient
from langchain_tavily import TavilySearch


class Source(BaseModel):
    """Schema for a source used by the agent"""
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the response of the agent"""
    sources: List[Source] = Field(description="List of sources used by the agent")
    answer: str = Field(description="The answer to the question")

# tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))

# @tool
# def search(query: str) -> str:
#     """Search the web for information"""
#     print(f"Searching the web for information: {query}")
#     return tavily_client.search(query)

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.environ.get("GOOGLE_API_KEY"))

#tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm,tools=tools,response_format=AgentResponse)


def main():
    print("Hello from lang-hello!")
    response = agent.invoke({"messages": [HumanMessage(content="Serach for 3 Job openings in the field of AI and Machine Learning from Linkedin?")]})    
    print(f"Response: {response}")
    
    # Extract structured response if available
    if 'structured_response' in response:
        structured = response['structured_response']
        if isinstance(structured, AgentResponse):
            print(f"Sources: {structured.sources}")
            print(f"Answer: {structured.answer}")
        else:
            print(f"Structured response: {structured}")
    else:
        # If no structured response, get the last message content
        messages = response.get('messages', [])
        if messages:
            last_message = messages[-1]
            print(f"Answer: {last_message.content}")
 
if __name__ == "__main__":
    main()
