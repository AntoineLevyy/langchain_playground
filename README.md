# langchain_playground
Exploring langchain
# langchain_playground
Exploring langchain

# Components
- conversations_langchain.py contains the functions to open conversations with various models (currently OpenAI's GPT3, Facebook's LLama 2, Google's Gemini, Google's Palm2)
  NB: API keys or service accounts (Google Palm2) are required.
- notebook shows an example of a short conversation with Llama2.

# Benefits
- Contrary to using API's in isolation, langchain built a framework to allow for (system memory)[https://python.langchain.com/docs/modules/memory/]. Allowing to bounce back on models responses as one would in UI's.