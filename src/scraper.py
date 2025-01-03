from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def scrape_articles(driver):
    """Scrape the first 5 articles from the Opinion section."""
    try:
        # Open the website
        driver.get("https://elpais.com/")
        driver.execute_script("document.documentElement.lang = 'es'")  # Set language to Spanish

        # Accept cookies if there's a cookie notice
        try:
            accept_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
            )
            accept_button.click()
        except:
            pass  # If no cookie banner appears, continue

        # Wait for the "Opinión" section to be clickable
        WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Opinión"))
        )
        
        # Click the "Opinión" section
        opinion_link = driver.find_element(By.LINK_TEXT, "Opinión")
        opinion_link.click()

        
        
        # Parse the page
        soup = BeautifulSoup(driver.page_source, "html.parser")
        articles = soup.find_all("article", limit=5)

        result = []
        for article in articles:
            title = article.find("h2").get_text(strip=True)
            link = article.find("a")["href"]
            content = scrape_content(link)
            image_url = article.find("img")["src"] if article.find("img") else None

            result.append({"title": title, "link": link, "content": content, "image_url": image_url})

        driver.quit()
        logger.info("Scraping completed successfully.")
        return result
    
    except Exception as e:
        logger.error(f"Error scraping articles: {e}")
        driver.quit()
        return []

def scrape_content(link):
    """Fetch the content of an article."""
    try:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        return " ".join(p.get_text(strip=True) for p in paragraphs)
    except Exception as e:
        logger.error(f"Error fetching article content: {e}")
        return ""
