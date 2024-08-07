import requests
import pandas as pd
import json
from GoogleNews import GoogleNews
from newspaper import Article
import pandas as pd

def get_articles(search_term, start_date, end_date):
    googlenews=GoogleNews(start='03/24/2024',end='03/23/2024')
    googlenews.search(search_term)
    result=googlenews.result()
    all_result = result
    
    for i in range(2, 20):
        googlenews.getpage(i)
        result = googlenews.result()
        all_result.extend(result)

    df = pd.DataFrame(all_result)    
    return df

def summarize_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return article.summary
    except Exception as e:
        return str(e)

df_russia = get_articles('Russia', '03/24/2024', '03/23/2024')
print("Russia Articles:")
print(df_russia.head())

df_russia['summary'] = df_russia['link'].apply(summarize_article)

print("Russia Articles with Summaries:")
print(df_russia[['title', 'summary']].head())
