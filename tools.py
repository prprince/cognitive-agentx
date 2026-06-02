import requests
from bs4 import BeautifulSoup

def scrape_market_news(topic):
    """Fetches real-time market updates and news headlines."""
    url = f"https://news.google.com/rss/search?q={topic}&hl=en-IN&gl=IN&ceid=IN:en"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    
    items = soup.find_all('item')
    news_data = []
    
    for item in items[:10]:
        news_data.append(item.title.text)
        
    return " | ".join(news_data)