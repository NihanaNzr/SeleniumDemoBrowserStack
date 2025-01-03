import os
import requests
from utils.constants import IMAGE_DOWNLOAD_FOLDER

# Ensure image folder exists
os.makedirs(IMAGE_DOWNLOAD_FOLDER, exist_ok=True)

def download_image(image_url, filename):
    """Download an image and save it locally."""
    if image_url:
        response = requests.get(image_url)
        filepath = os.path.join(IMAGE_DOWNLOAD_FOLDER, filename)
        with open(filepath, "wb") as file:
            file.write(response.content)
        return filepath
    return None
