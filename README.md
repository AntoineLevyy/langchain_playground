# langchain_playground
Exploring langchain


# Components
- chatbots folder:
    - conversations_langchain.py contains the functions to open conversations with various models (currently OpenAI's GPT3, Facebook's LLama 2, Google's Gemini, Google's Palm2)
    NB: API keys or service accounts (Google Palm2) are required.
    - notebook shows an example of a short conversation with Llama2.

- web_scraping folder:
    - web_scraping.py contains basic webscraping functions with langchain wrappers.
    - web_scraping.ipynb shows an example of creating a df with content from urls.

- tagging folder:
   - notebook using scraping functions from web_scraping and giving doubtful results for a summary and a sentiment of a review of "anatomy of a fall."

# Benefits
- Contrary to using API's in isolation, langchain built a framework to allow for (system memory)[https://python.langchain.com/docs/modules/memory/]. Allowing to bounce back on models responses as one would in UI's.
