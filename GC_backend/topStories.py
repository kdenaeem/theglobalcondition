import requests
from bs4 import BeautifulSoup
import json
import datetime
import pyshorteners
from country_list import countries
import time

def fetchNewsArticle(country):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding": "gzip",
        "Accept-Language": "en-GB,en;q=0.9,es;q=0.8",
        "Upgrade-Insecure-Requests": "1",
        "Referer": "https://www.google.com/"
    }
    cookies = {
        "CONSENT": f"YES+cb.{datetime.datetime.now().isoformat().split('T')[0].replace('-', '')}-04-p0.en-GB+FX+667"
    }
    # url = f"https://news.google.com/search?q={country}&hl=en-GB&gl=GB&ceid=GB%3Aen"
    url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKSFFpZ0FQAQ?hl=en-GB&gl=GB&ceid=GB%3Aen"
    response = requests.get(url, headers=headers, cookies=cookies)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    articles = soup.find_all('article')
    article_count = 0
    results = []

    for article in articles:
        if article_count >= 50:
            break
        if article_count > 3:
            title_element_div = article.find_all('a', {"class": 'gPFEn'})
            title = title_element_div[0].get_text() if title_element_div else None
            link_elements = article.find("a", class_="WwrzSb")
            article_link = link_elements['href']
            link = article_link.replace('./', 'http://news.google.com/') if article_link else None
            
            figure_element = article.find('figure')
            imgsrc = figure_element.find('img').get('srcset').split(' ') if figure_element and figure_element.find('img') else []
            image = imgsrc[-2] if imgsrc else figure_element.find('img').get('src') if figure_element and figure_element.find('img') else None
            if image and image.startswith('/'):
                image = f"https://news.google.com{image}"

            source_element = article.find('div', {'data-n-tid': True})
            source = source_element.text if source_element else None
            
            time_element = soup.find('time')
            publication_time = time_element['datetime']
            dt = datetime.datetime.fromisoformat(publication_time.replace('Z', '+00:00'))
            time_str = dt.strftime('%H:%M:%S')

            publication_datetime = datetime.datetime.fromisoformat(publication_time)
            
            mainArticle = {
                "country": country,
                "title": title,
                "link": link,
                "image": image,
                "source": source,
                "datetime": publication_datetime.isoformat(),
                "time": time_str
            }
            results.append(mainArticle)
        
        article_count += 1

    return json.dumps(results, indent=4)

print(fetchNewsArticle('country'))

# for country in countries:
#     time.sleep(3)
    
