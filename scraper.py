import feedparser
import requests
from bs4 import BeautifulSoup
import json

FEED_URL = "https://www.hodinkee.com/rss"

def parse_feed(url):
    feed = feedparser.parse(url)
    return [{
        "title": entry.title,
        "link": entry.link,
        "published": entry.get("published", "")
    } for entry in feed.entries]

def scrape_if_needed(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.title.string
    except:
        return "Failed to scrape"

if __name__ == "__main__":
    items = parse_feed(FEED_URL)
    with open("data.json", "w") as f:
        json.dump(items, f, indent=2)
    print("✅ Fetched and saved feed.")
