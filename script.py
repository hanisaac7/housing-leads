from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
import time

edge_options = EdgeOptions()
edge_options.use_chromium = True
edge_options.add_argument('--headless')

edge_driver_path = "./msedgedriver"
edge_driver = webdriver.Edge(options=edge_options)
edge_driver.get("https://orangecounty.craigslist.org/search/apa?max_price=1500#search=1~gallery~0~0")

edge_driver.implicitly_wait(10)

print(edge_driver.title)

rentals = edge_driver.find_elements('xpath', '//li[contains(@class, "cl-search-result") and contains (@class, "cl-search-view-mode-gallery")]')
for rental in rentals:
    print(rental.text)

edge_driver.quit()

