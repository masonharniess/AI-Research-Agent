from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv() # load .env file to obtain credentials

class ResearchResponse(BaseModel):
  topic: str
  summary: str
  sources: list[str]
  tools_used: list[str]

llmOpenAI = ChatOpenAI(model="gpt-4o-mini")

# llmAnthropic = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# response = llmOpenAI.invoke("What is the meaning of life?")
# print(response)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
  [
    (
      "system",
      """
      You are a research assistant that will help generate a research paper. 
      Answer the user query and use the necessary tools.
      Wrap the output in this format and provide no other text.
      \n{format_instructions}
      """,
    ),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
  ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
  llm=llmOpenAI,
  prompt=prompt,
  tools=[]
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=False)
raw_response = agent_executor.invoke({"query": "What is the capital of France?"})

# print(raw_response)

output = raw_response.get("output")

structured_response = parser.parse(raw_response.get("output"))

print(structured_response)