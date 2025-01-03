import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from src.scraper import scrape_articles
from src.translator import translate_rapidapi
from src.analyzer import analyze_headers
from utils.logger import setup_logger
from utils.json_saver import save_to_json
from multiprocessing.dummy import Pool  # ThreadPool instead of Pool

logger = setup_logger()

# Function to execute tests on BrowserStack
def run_browserstack_test(capability):
    """Runs a test session on BrowserStack."""
    driver = None  # Initialize driver variable here to handle in exception block
    try:
        # Setup the WebDriver for BrowserStack
        driver = webdriver.Remote(
            command_executor=f"https://{os.getenv('BROWSERSTACK_USERNAME')}:{os.getenv('BROWSERSTACK_ACCESS_KEY')}@hub.browserstack.com/wd/hub",
            desired_capabilities=capability
        )

        # Log starting the scraping process
        logger.info(f"Scraping articles on {capability['os']} {capability['browserName']}...")

        # Scrape articles using the WebDriver
        articles = scrape_articles(driver)

        # Translate article titles
        translated_titles = []
        for article in articles:
            title = article["title"]
            logger.info(f"Translating title: {title}")
            translated_title = translate_rapidapi(title)  # Ensure this translates into English
            logger.info(f"Translated title: {translated_title}")
            translated_titles.append(translated_title)

        # Analyze the translated titles
        logger.info("Analyzing translated titles...")
        repeated_words = analyze_headers(translated_titles)

        # Save results to JSON
        logger.info("Saving data to JSON...")
        save_to_json({
            "articles": articles,
            "translated_titles": translated_titles,
            "repeated_words": repeated_words,
        })

    except Exception as e:
        logger.exception(f"Error occurred during BrowserStack test: {e}")

    finally:
        # Quit the WebDriver session if it was created
        if driver:
            driver.quit()

# List of BrowserStack capabilities for multiple platforms
BROWSERSTACK_CAPABILITIES = [
    {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Chrome',
        'browserVersion': 'latest',
        'buildName': 'bstack-demo',
        'projectName': 'Web Scraping Project',
        'debug': True,
        'networkLogs': True,
        'consoleLogs': 'info',
    },
    {
        'os': 'Windows',
        'osVersion': '10',
        'browserName': 'Firefox',
        'browserVersion': 'latest',
        'buildName': 'bstack-demo',
        'projectName': 'Web Scraping Project',
        'debug': True,
        'networkLogs': True,
        'consoleLogs': 'info',
    },
    {
        'os': 'OS X',
        'osVersion': 'Monterey',
        'browserName': 'Safari',
        'browserVersion': 'latest',
        'buildName': 'bstack-demo',
        'projectName': 'Web Scraping Project',
        'debug': True,
        'networkLogs': True,
        'consoleLogs': 'info',
    },
    {
        'deviceName': 'iPhone 13',
        'osVersion': '15',
        'browserName': 'Safari',
        'deviceOrientation': 'portrait',
        'buildName': 'bstack-demo',
        'projectName': 'Web Scraping Project',
        'debug': True,
        'networkLogs': True,
        'consoleLogs': 'info',
    },
    {
        'deviceName': 'Samsung Galaxy S22',
        'osVersion': '12.0',
        'browserName': 'Chrome',
        'buildName': 'bstack-demo',
        'projectName': 'Web Scraping Project',
        'debug': True,
        'networkLogs': True,
        'consoleLogs': 'info',
    }
]

# Function to run tests on multiple platforms in parallel
if __name__ == "__main__":
    # Run the tests in parallel using a ThreadPool of workers
    with Pool(len(BROWSERSTACK_CAPABILITIES)) as pool:
        pool.map(run_browserstack_test, BROWSERSTACK_CAPABILITIES)
