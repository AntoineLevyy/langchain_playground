import pandas as pd

from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer
import nest_asyncio


def extract_url_content_df(url_list):
   """
   extracts url content for a list of 1 url and turns it to a df
   """
   html = html_retriever(url_list)
   content = doc_transformer(html)

   url_df = pd.DataFrame(columns = ["URL", "Content"])

   url_df["URL"] = url_list
   url_df["Content"] = content
       
   return url_df

      
def html_retriever(url_list):
  
  """
  function that intakes a list of urls and returns 
  the html for them. Using langchain's doc loaders and bs libraries.
  """
  nest_asyncio.apply()
  html = load_html(url_list)

  return html

def load_html(url_list):
    loader = AsyncChromiumLoader(url_list)
    html = loader.load()
    return html

def doc_transformer(html):
  bs_transformer = BeautifulSoupTransformer()
  docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["span"])
  content = docs_transformed[0].page_content
  return content
 

