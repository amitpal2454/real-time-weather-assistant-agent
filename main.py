from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
import os
load_dotenv()
print(os.environ.get("OPENAI_API_KEY"))
llm=ChatOpenAI(model="gpt-4.1-mini",api_key=os.environ.get("OPENAI_API_KEY"))
#llm_2=ChatAnthropic(model="claude-3-5-sonnet-20241022",api_key=os.environ.get("ANTHROPIC_API_KEY"))
resposne=llm.invoke("what is the capital of australia")

print(resposne.content)
