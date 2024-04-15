from selenium import webdriver
from selenium.webdriver.common.by import By
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