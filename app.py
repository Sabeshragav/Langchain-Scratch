import getpass
import os

from dotenv import load_dotenv
load_dotenv()

if not os.getenv("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("openai/gpt-oss-120b", model_provider="groq")

response = model.invoke("Whats the capital of Tamil Nadu")

print(response)