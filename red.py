from classes.DatabaseManager_file import DatabaseManager
from classes.ScraperClassFile_file import ScraperClass
db = DatabaseManager('wine.db')
scraper = ScraperClass()
url_red = "https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1NTBQS660dXJVS7Z1DQ1SKwDKpqfZliUWZaaWJOao5Rel2KakFier5SdV2ialFpfEF2QmZxerlZdEx9oaAgC5yxm5"

db.create_table_links('red_links')
# scraper.scrape(url_red)
