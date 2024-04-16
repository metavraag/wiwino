from playwright.sync_api import sync_playwright
from playwright.sync_api import TimeoutError
from datetime import datetime
import time


class ScraperClass:
    def __init__(self, headless=False):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()  # Initialize a new page here

    def scrape(self, url):
        self.page.goto(url)
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
        self.page.close()
        self.browser.close()
        self.playwright.stop()

    def accept_cookies(self):
        try:
            self.page.click("#didomi-notice-agree-button")
        except Exception:
            print("Accept cookies button not found")
            pass

    def check_type_page(self):
        elements = [
            (
                ".purchaseAvailability__row--S-DoM.purchaseAvailability__prices--1WNrU",
                "promo",
            ),
            (".purchaseAvailabilityPPC__icon--3t84F", "average"),
            (
                ".purchaseAvailabilityPPC__betterValueSentence--3OMTX",
                "no price",
            ),
        ]

        for selector, page_type in elements:
            if self.page.query_selector(selector):
                return page_type

    def infinite_scroll(self):
        # Get scroll height
        last_height = self.page.evaluate("document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(3)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.page.evaluate("document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def get_winery(self):
        try:
            return self.page.inner_text(".winery")
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_wine_info(self):
        try:
            # Initialize an empty dictionary to store the data
            wine_info = {}

            # Find all rows in the table
            rows = self.page.query_selector_all(".wineFacts__wineFacts--2Ih8B tr")

            # Iterate over each row
            for row in rows:
                # Find the key and value in the th and td elements
                key = row.inner_text("th")
                value = row.inner_text("td")

                # Add the key-value pair to the dictionary
                wine_info[key] = value

            return wine_info
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_ratings(self):
        try:
            # Extract the review score and total reviews
            review_score = self.page.inner_text(
                ".vivinoRating_averageValue__uDdPM", timeout=5000
            )  # 5 seconds timeout
            total_reviews = self.page.inner_text(
                ".vivinoRating_caption__xL84P", timeout=5000
            )  # 5 seconds timeout

            # Initialize a dictionary to store the data
            ratings = {
                "review_score": float(review_score),
                "total_reviews": int(
                    total_reviews.split()[0]
                ),  # Extract the number from the string
            }

            return ratings
        except TimeoutError:
            print(
                "Timeout while trying to extract ratings. The element may not be present on the page."
            )
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_price_promo(self):
        try:
            # Extract the current price and normal_price
            current_price = self.page.inner_text(
                ".purchaseAvailability__currentPrice--3mO4u"
            )
            normal_price = self.page.inner_text(
                ".price_strike__mOVjZ.purchaseAvailability__retailPrice--xisuR"
            )

            # Initialize a dictionary to store the data
            price = {
                "current_price": float(current_price),
                "normal_price": float(normal_price),
            }

            return price
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
