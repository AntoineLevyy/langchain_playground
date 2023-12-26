import os
from dotenv import load_dotenv

from google.oauth2 import service_account


from langchain.chat_models import ChatOpenAI, ChatAnthropic, ChatVertexAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_experimental.llms import ChatLlamaAPI
from llamaapi import LlamaAPI


from langchain.schema import HumanMessage, SystemMessage
from langchain.chains import ConversationChain



# Open AI // GPT 3
def start_conversation_openai():
  openai_api_key = os.getenv("openai_api_key")
  chat_openai = ChatOpenAI(openai_api_key=openai_api_key)
  conversation_openai = ConversationChain(llm=chat_openai)

  return conversation_openai


# Google // Gemini (limited regions)
def start_conversation_gemini():
  google_api_key = os.getenv("google_api_key")
  chat_gemini = ChatGoogleGenerativeAI(model="gemini_pro" ,google_api_key = google_api_key)
  conversation_gemini = ConversationChain(llm=chat_gemini)

# Google // Palm-2 (limite regions)
def start_conversation_palm2():
  GOOGLE_APPLICATION_CREDENTIALS = "ai-playground_service_account.json"
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS
  chat_palm_2 = ChatVertexAI()
  conversation_palm2 = ConversationChain(llm=chat_palm_2)

# Facebook // LLama 2
def start_conversation_llama2():
  llama_api_key = os.getenv("llama_api_key")
  llama = LlamaAPI(llama_api_key)
  chat_llama =  ChatLlamaAPI(client = llama)
  conversation_llama = ConversationChain(llm=chat_llama)
  
  return conversation_llama

# Sending a message, conversation specified needs to have been opened beforehand!
def send_message(conversation, message):
   print(conversation.run(message))