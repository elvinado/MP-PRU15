from concurrent.futures import ThreadPoolExecutor
import pandas as pd
from newspaper import fulltext
import requests
# import pickle
import json

def write_data(file,data):
    with open(file,"w",encoding='utf-8') as f:
        json.dump(data,f, indent=4)
        
def texts_from_url(url):
    print(f"Downloading:{url}")
    return fulltext(requests.get(url).text)

news_df = pd.read_pickle("data/20221206_news_df_with links.pkl")
start, end = 0,news_df.shape[0]
ids = range(start,end)
urls = news_df[start:end]['url'].tolist()

if __name__ == '__main__':
  with ThreadPoolExecutor(max_workers = 64) as executor:
      thread1 = executor.map(texts_from_url, urls)
  
  final_dict = {"id":list(range(start,end)),
                "text":list(thread1)}

  write_data(f"corpus/fulltexts_{start}_{end}.json",
              final_dict)