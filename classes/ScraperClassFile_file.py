from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


class ScraperClass:
    def __init__(self, headless=False):
        # setup the selenium browser
        self.options = Options()
        self.options.headless = headless

        self.driver = webdriver.Firefox(options=self.options)

    def scrape(self, url):
        self.driver.get(url)
        self.accept_cookies()
        # self.infinite_scroll()
        winery = self.get_wine_info()
        self.driver.quit()
        return winery

    def accept_cookies(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "didomi-notice-agree-button"))
            )
            element.click()
        except TimeoutException:
            print("Accept cookies button not found")
            pass

    def infinite_scroll(self):
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            # Wait to load page
            time.sleep(3)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_winery(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "winery"))
            )
            return element.text
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_wine_info(self):
        try:
            # Wait until the table is present
            table = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "wineFacts__wineFacts--2Ih8B")
                )
            )

            # Initialize an empty dictionary to store the data
            wine_info = {}

            # Find all rows in the table
            rows = table.find_elements(By.TAG_NAME, "tr")

            # Iterate over each row
            for row in rows:
                # Find the key in the th element
                key_element = row.find_element(By.TAG_NAME, "th")
                key = key_element.text

                # Find the value in the td element
                value_element = row.find_element(By.TAG_NAME, "td")
                value = value_element.text

                # Add the key-value pair to the dictionary
                wine_info[key] = value

            return wine_info
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
