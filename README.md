# Web Scraping and Translation Service - Automation

This project scrapes articles, translates the article titles using the RapidAPI translation service, analyzes the titles for repeated words, and saves the results to a JSON file. Additionally, it provides an automated cross-browser testing environment using BrowserStack.

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running Tests Locally ](#Running-Tests-Locally)
6. [Running Tests on BrowserStack](#running-tests-on-browserstack)
7. [Project Structure](#project-structure)
8. [Contributing](#contributing)
9. [License](#license)

## Features
- Web scraping of articles from a website.
- Translation of article titles using RapidAPI.
- Analysis of translated titles for repeated words.
- Saving results to a local JSON file.
- Running automated cross-browser tests using BrowserStack.

## Prerequisites

To run this project locally or on BrowserStack, ensure the following prerequisites are met:

- **Python 3.x** installed on your machine.
- **Pip** for installing Python packages.
- A valid [RapidAPI key](https://rapidapi.com/), specifically for the **Rapid Translate Multi Traduction** API.
- A valid [BrowserStack](https://www.browserstack.com/) account with credentials.
  
## Installation

1. **Clone the Repository:**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/yourusername/web-scraping-project.git
   cd web-scraping-project
   ```
2. **Install Dependencies:**
   Install all necessary Python packages from requirements.txt:

   ```bash
   pip install -r requirements.txt
    ```

## Configuration

1.**Setting Up the RapidAPI Key**

This project uses the RapidAPI translation service. To integrate this:

- Open the utils/constants.py file.
- Replace the RAPIDAPI_KEY placeholder with your actual API key.

  ```bash
  RAPIDAPI_KEY = 'your-rapidapi-key'
  RAPIDAPI_HOST = 'rapid-translate-multi-traduction.p.rapidapi.com'
   ```
2.**Setting Up BrowserStack Credentials**

For Windows Command Prompt:

```bash
  set BROWSERSTACK_USERNAME=your_browserstack_username
  set BROWSERSTACK_ACCESS_KEY=your_browserstack_access_key
```
For macOS or Linux:

```bash
  export BROWSERSTACK_USERNAME="your_browserstack_username"
  export BROWSERSTACK_ACCESS_KEY="your_browserstack_access_key"
```

3. **BrowserStack Configuration (Optional)**
   You can configure the desired browsers and devices in the browserstack.yml file to specify the environment for running tests.
   
## Running Tests Locally

1.**Run the Main Script Locally**
To run the project and perform scraping, translation, and data analysis, execute:

```bash
  python main.py
```
This will scrape articles, translate the titles, analyze repeated words, and save the results in data/output_data.json.

2. **Check the Output**
   The results of the scraping, translation, and analysis will be saved in the data/output_data.json file. The log of the process will be available in the web_scraper.log file.

## Running Tests on BrowserStack

1.**Execute the Test Script**
  To run the tests on BrowserStack using different browsers and configurations, execute the following command:
  ```bash
    python test_script.py
  ```

2.**Test Results**
  After running the tests, you can view the results on the BrowserStack dashboard, which will include logs, error messages, and video recordings of the test sessions.

## Project Structure
```plaintext
article_image/          # Directory to store article images
data/                   # Directory to store output JSON file
├── src/
│   ├── __init__.py
│   ├── scraper.py      # Web scraping logic
│   ├── translator.py   # Translation functionality
│   ├── analyzer.py     # Text analysis (finding repeated words)
├── utils/
│   ├── constants.py    # Stores API keys and other constants
│   ├── downloader.py   # Image downloader utility
│   ├── logger.py       # Logger setup
│   └── json_saver.py   # Saves results to JSON
├── requirements.txt    # List of dependencies
├── README.md           # This README file
├── main.py             # Main entry point for the application
├── browserstack.yml    # BrowserStack configuration
├── test_script.py      # Script to run parallel tests on BrowserStack
└── web_scraper.log     # Log file for tracking process
```
## License
This project is licensed under the MIT License.

## Contact
For further inquiries or support, please contact [Nihana Nizar/nihananizar17@gmail.com].

