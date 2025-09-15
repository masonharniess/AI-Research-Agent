from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic

load_dotenv() # load .env file to obtain credentials

llmOpenAI = ChatOpenAI(model="gpt-4o-mini")
llmAnthropic = ChatAnthropic(model="claude-3-5-sonnet-20241022")

response = llmOpenAI.invoke("What is the meaning of life?")
print(response)