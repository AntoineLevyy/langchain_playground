# langchain_playground
Exploring langchain

# Components
-chatbots:
  - conversations_langchain.py contains the functions to open conversations with various models (currently OpenAI's GPT3, Facebook's LLama 2, Google's Gemini, Google's Palm2)
  NB: API keys or service accounts (Google Palm2) are required.
  - notebook shows an example of a short conversation with Llama2.

-web_scraping:
  - web_scraping.py contains functions to conduct usual web scraping facilitated by langchain. 
  - notebooks shows an example of transforming urls to content DataFrame.

# Benefits
- Contrary to using API's in isolation, langchain built a framework to allow for (system memory)[https://python.langchain.com/docs/modules/memory/]. Allowing to bounce back on models responses as one would in UI's.
