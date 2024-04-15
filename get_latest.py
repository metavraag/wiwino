from classes.DatabaseManager_file import DatabaseManager
from classes.ScraperClassFile_file import ScraperClass
db = DatabaseManager('wine.db')
scraper = ScraperClass()

scraper.scrape("https://www.vivino.com/explore?e=eJzLLbI11rNQy83MszVXy02ssDU2UEuutHVyVUu2dQ0NUiuwNVRLT7MtSyzKTC1JzFHLL0qxTUktTlbLT6q0TUotLokvyEzOLlYrL4mOBSoFU0YAijkcLg%3D%3D")