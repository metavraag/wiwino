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
        self.infinite_scroll()
        time.sleep(5)
        self.driver.quit()

    def accept_cookies(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button'))
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
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(2)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height