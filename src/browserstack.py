from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.constants import BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY

def setup_browserstack():
    """Set up BrowserStack capabilities."""
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities["browserstack.user"] = BROWSERSTACK_USERNAME
    capabilities["browserstack.key"] = BROWSERSTACK_ACCESS_KEY
    capabilities["browser"] = "Chrome"
    capabilities["os"] = "Windows"
    capabilities["os_version"] = "10"
    return capabilities

def run_on_browserstack(scrape_function):
    """Run the scraping function on BrowserStack."""
    driver = Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        desired_capabilities=setup_browserstack()
    )
    try:
        return scrape_function(driver)
    finally:
        driver.quit()
