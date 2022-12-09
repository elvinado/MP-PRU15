from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from newspaper import fulltext
import requests
import spacy
import pickle

news_df = pd.read_pickle("data/20221206_news_df_with links.pkl")

#load spacy data model
NLP = spacy.load('en_core_web_lg')

def persons_from_url(idx,url):
    text = fulltext(requests.get(url).text)
    print(f"Downloaded: {url}")
    ner = NLP(text) 
    return idx, [p.text for p in ner.ents if p.label_=='PERSON']

start, end = 1000,1376
ids = range(start,end)
urls = news_df[start:end]['url'].tolist()

if __name__ == '__main__':
  with ThreadPoolExecutor(max_workers = 64) as executor:
      thread1 = executor.map(persons_from_url, ids, urls)
  
  with open(f"data/set_{start}_{end}.pkl","wb") as f:
    pickle.dump(list(thread1),f)
