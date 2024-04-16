import requests
import json
from ScraperClassFile_file import ScraperClass


def get_ids(json_name):
    # read the json file
    with open(json_name, "r", encoding="utf-8") as file:
        data = json.load(file)
    # return all ids
    return [region["id"] for region in data["regions"]]


def construct_url(id):
    base_url = "https://www.vivino.com/BE/en/w/"
    full_url = str(base_url) + str(id)
    return full_url


# Create an instance of ScraperClass
vivino = ScraperClass(headless=True)

# Get all ids from the json file
ids = get_ids("wine.json")

# Loop over all ids
for id in ids:
    url = construct_url(id)
    print(url)
    # Now call the scrape method
    scraped_object = vivino.scrape(url)
    print(scraped_object)

# Quit the driver after all URLs have been scraped
vivino.quit_driver()
