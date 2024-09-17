from newspaper import Article
from bs4 import BeautifulSoup
from collections import Counter
import re
import requests
from country_list import countries

# def getCountryMention(url):
#   country = ''
#   url = "https://edition.cnn.com/2024/08/07/politics/video/kamala-harris-hecklers-interrupts-speech-digvid"
#   url2 = "https://www.aljazeera.com/news/2024/8/8/harris-campaign-denies-support-for-cutting-off-weapons-transfers-to-israel"
#   article = Article(url)
#   article.download()  
#   article.parse()

#   # print(article.text)
#   article.nlp()
#   print(article.keywords)
  
#   article = Article(url)
#   return country
  
# getCountryMention('hello')

async def getTopCountries(num_countries=10):
  response = requests.get("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen")
  soup = BeautifulSoup(response.content, 'html.parser')
  text = soup.get_text()
  
  found_countries = []
  
  for country in countries:
    count = len(re.findall(r'\b' + re.escape(country) + r'\b', text, re.IGNORECASE))
    if count > 0:
      found_countries.extend([country] * count)
    
  country_counts = Counter(found_countries)
  top_countries = country_counts.most_common(num_countries)
  country_list = {country for country,count in top_countries}

  return country_list

# url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"
# print(getTopCountries())

# print("Top 10 mentioned countries:")
# for country, count in top_10_countries:
#     print(f"{country}: {count}")
