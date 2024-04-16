import requests
import json
from ScraperClassFile_file import ScraperClass


def get_id(json_name):
    # read the json file
    with open(json_name, "r") as file:
        data = json.load(file)
    return data["regions"][0]["id"]


def construct_url(id):
    base_url = "https://www.vivino.com/BE/en/w/"
    full_url = str(base_url) + str(id)
    return full_url


url1 = construct_url(2978)
url2 = construct_url(1606)

print(url1)
print(url2)

# Create an instance of ScraperClass
vivino = ScraperClass()

# Now call the scrape method
scraped_object = vivino.scrape(url1)
print(scraped_object)
