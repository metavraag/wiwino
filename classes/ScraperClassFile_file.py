from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time


class ScraperClass:
    def __init__(self, headless=False):
        # setup the selenium browser
        self.options = Options()
        self.options.headless = headless

        try:
            # Make sure the path to your chromedriver is correct
            self.driver = webdriver.Chrome(options=self.options)
        except Exception as e:
            print(f"An error occurred while initializing the webdriver: {e}")
            raise e

    def scrape(self, url):
        self.driver.get(url)
        self.accept_cookies()
        page_type = self.check_type_page()

        if page_type == "promo":
            price = self.get_price_promo()
        elif page_type == "average":
            price = self.get_price_average()
        elif page_type == "no price":
            price = None
        else:
            print("Unknown page type")
            price = None

        wine_info = self.get_wine_info()
        ratings = self.get_ratings()

        result = {"price": price, "wine_info": wine_info, "ratings": ratings}

        return result

    def quit_driver(self):
        self.driver.quit()

    def accept_cookies(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
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
            table = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".wineFacts__wineFacts--2Ih8B")
                )
            )

            # Initialize an empty dictionary to store the data
            wine_info = {}

            # Find all rows in the table
            rows = table.find_elements(By.TAG_NAME, "tr")

            # Iterate over each row
            for row in rows:
                # Find the key and value in the th and td elements
                elements = row.find_elements(By.CSS_SELECTOR, "th, td")
                key = elements[0].text
                value = elements[1].text

                # Add the key-value pair to the dictionary
                wine_info[key] = value

            return wine_info
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_ratings(self):
        try:
            # Wait until the table is present
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".vivinoRating_vivinoRating__RbvjH")
                )
            )

            # Extract the review score and total reviews
            elements = self.driver.find_elements(
                By.CSS_SELECTOR,
                ".vivinoRating_averageValue__uDdPM, .vivinoRating_caption__xL84P",
            )
            review_score = elements[0].text
            total_reviews = elements[1].text

            # Initialize a dictionary to store the data
            ratings = {
                "review_score": float(review_score),
                "total_reviews": int(
                    total_reviews.split()[0]
                ),  # Extract the number from the string
            }

            return ratings
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def check_type_page(self):
        elements = [
            (
                By.CLASS_NAME,
                "purchaseAvailability__row--S-DoM purchaseAvailability__prices--1WNrU",
                "promo",
            ),
            (By.CLASS_NAME, "purchaseAvailabilityPPC__icon--3t84F", "average"),
            (
                By.CLASS_NAME,
                "purchaseAvailabilityPPC__betterValueSentence--3OMTX",
                "no price",
            ),
        ]

        for by, value, page_type in elements:
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((by, value))
                )
                return page_type
            except TimeoutException:
                pass

        return None

    def get_price_promo(self):
        try:
            # Check if this is a promo page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.CLASS_NAME,
                        "purchaseAvailability__row--S-DoM purchaseAvailability__prices--1WNrU",
                    )
                )
            )

            # Extract the current price and normal_price
            current_price = self.driver.find_element(
                By.CLASS_NAME, "purchaseAvailability__currentPrice--3mO4u"
            ).text
            normal_price = self.driver.find_element(
                By.CLASS_NAME,
                "price_strike__mOVjZ purchaseAvailability__retailPrice--xisuR",
            ).text

            # Initialize a dictionary to store the data
            price = {
                "current_price": float(current_price),
                "normal_price": float(normal_price),
            }

            return price
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_price_average(self):
        try:
            # Check if this is a average external prices page
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (
                        By.CLASS_NAME,
                        "purchaseAvailabilityPPC__icon--3t84F",
                    )
                )
            )

            # Extract the current price and normal_price
            average_price = self.driver.find_element(
                By.CLASS_NAME, "purchaseAvailabilityPPC__amount--2_4GT"
            ).text

            # Initialize a dictionary to store the data
            price = {
                "current_price": average_price,
            }

            return price
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
