# Web Scraping and Translation Service

This project scrapes articles, translates the article titles using the RapidAPI translation service, analyzes the titles for repeated words, and saves the results to a JSON file. Additionally, it provides an automated cross-browser testing environment using BrowserStack.

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Usage](#usage)
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
1.**Setting Up BrowserStack Credentials**

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

2. **Install the BrowserStack SDK**
   
