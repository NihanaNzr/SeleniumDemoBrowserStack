from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from src.scraper import scrape_articles
from src.translator import translate_rapidapi
from src.analyzer import analyze_headers
from utils.logger import setup_logger
from utils.json_saver import save_to_json
from src.translator import translate_rapidapi
import urllib3
import logging

logging.getLogger('urllib3').setLevel(logging.CRITICAL)
logger = setup_logger()

def main():
    logger.info("Starting web scraping project...")
    
    # Set up the WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        logger.info("Scraping articles locally...")
        articles = scrape_articles(driver)
        

        translated_titles = []
        for article in articles:
            title = article["title"]
            logger.info(f"Translating title: {title}")
            translated_title = translate_rapidapi(title)  # Ensure this translates into English
            logger.info(f"Translated title: {translated_title}")
            translated_titles.append(translated_title)

        
        

        logger.info("Analyzing translated titles...")
        repeated_words = analyze_headers(translated_titles)  
        

        logger.info("Saving data to JSON...")
        save_to_json({
            "articles": articles,
            "translated_titles": translated_titles,
            "repeated_words": repeated_words,
        })

        #logger.info("Running on BrowserStack...")
        #run_on_browserstack(scrape_articles)

    except Exception as e:
        logger.exception("An error occurred: %s", e)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
