import time
import requests
from utils.logger import setup_logger
import os
from utils.constants import RAPIDAPI_KEY, RAPIDAPI_HOST

logger = setup_logger()

def translate_rapidapi(title):
    url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"
    headers = {
        "Content-Type": "application/json",
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY,
    }

    # Data to be sent in the request body
    data = {
        "from": "es",  # Assuming Spanish is the original language
        "to": "en",    # Translate to English
        "q": title     # The text you want to translate
    }

    retries = 5
    for attempt in range(retries):
        try:
            response = requests.post(url, headers=headers, json=data)  # Use POST and pass data as JSON
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            translation = response.json()[0]  # Get the translation from the response
            logger.info(f"Translation successful: {translation}")
            return translation
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                # Rate limit exceeded, wait and try again
                logger.error("Rate limit exceeded. Retrying in 5 seconds...")
                time.sleep(5)
            elif response.status_code == 404:
                logger.error("API endpoint not found. Please check the URL or the API availability.")
                break
            else:
                logger.error(f"HTTP Error occurred: {e}")
                break
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            break

    return ""