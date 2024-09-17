from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

app = FastAPI()

# List of common country names
countries = [
    "United States", "China", "India", "Russia", "Brazil", "Japan", "Germany", 
    "United Kingdom", "France", "Italy", "Canada", "Australia", "Spain", "Mexico",
    "Indonesia", "Netherlands", "Saudi Arabia", "Turkey", "Switzerland", "Poland",
    "Sweden", "Belgium", "Argentina", "Norway", "Austria", "United Arab Emirates",
    "Nigeria", "Israel", "Hong Kong", "Singapore", "Malaysia", "Denmark", "Ireland",
    "Pakistan", "Thailand", "Taiwan", "Philippines", "Vietnam", "South Africa", "Colombia"
]

@app.get("/")
async def root():
    return {"message": "Welcome to News API"}

@app.get("/countries/top")
async def get_top_countries(num_countries: int = 10):
    try:
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
        country_list = [{"country": country, "count": count} for country, count in top_countries]
        
        return JSONResponse(content={"top_countries": country_list})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/countries/{country}")
async def get_country(country: str):
    try:
        # Placeholder for fetchNewsArticle function
        news_article = f"News for {country}"
        return JSONResponse(content={"news": news_article})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
