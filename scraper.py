import requests
from bs4 import BeautifulSoup
import time
import random

class FragranceScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

    def fetch_page(self, url):
        try:
            # Introduce explicit variable jitter delays to bypass basic automated anti-bot detection
            time.sleep(random.uniform(2, 5))
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return BeautifulSoup(response.text, 'html.parser')
            return None
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def scrape_fragrance_profile(self, url):
        soup = self.fetch_page(url)
        if not soup:
            return None
            
        # These selectors are structural examples; modern high-protection sites update classes frequently
        try:
            name = soup.find("h1").text.strip() if soup.find("h1") else "Unknown"
            notes_elements = soup.select(".notes-class-selector")
            notes = [el.text.strip() for el in notes_elements]
            
            return {
                "name": name,
                "notes": ", ".join(notes),
                "source_url": url
            }
        except Exception as e:
            print(f"Parsing error: {e}")
            return None

if __name__ == "__main__":
    scraper = FragranceScraper()
    print("Scraper initialized. Ready to loop target URLs dynamically.")