from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def scrape_housing_data(url):
    # Set up the GeckoDriver and start a Firefox browser session
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)

    # Open the webpage
    driver.get(url)

    # Wait for the page to load or for specific elements to be loaded
    driver.implicitly_wait(10)  # Waits up to 10 seconds before throwing an exception if elements are not found

    # Find elements by their XPath, CSS selectors, etc.
    listings = driver.find_elements(By.CSS_SELECTOR, '.listing-title')  # Adjust the selector based on the webpage

    # Extract and print the text from each listing
    for listing in listings:
        print(listing.text)

    # Close the browser
    driver.quit()

# Example URL - replace with the actual URL of the housing market site you are interested in
url = 'https://example.com/housing'
scrape_housing_data(url)
