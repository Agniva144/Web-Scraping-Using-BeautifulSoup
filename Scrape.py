from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

url = "https://www.amazon.in/s?k=shoes&ref=nb_sb_noss_2"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# Use Selenium to interact with the page
driver = webdriver.Chrome()
driver.get(url)

# Allow some time for the page to load dynamically
time.sleep(5)  # You may adjust this depending on the page load time

# Get the page source after dynamic content has loaded
page_source = driver.page_source
driver.quit()

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

# Extract data
data = {'title': [], 'price': []}
titles = soup.select("span.a-size-base-plus.a-color-base.a-text-normal")
prices = soup.select("span.a-price-whole")

for title, price in zip(titles, prices):
    data["title"].append(title.get_text(strip=True))
    data["price"].append(price.get_text(strip=True))

# Create a DataFrame and save to CSV
df = pd.DataFrame.from_dict(data)
df.to_csv("Scraping\BeautifulSoup\data2.csv", index=False)
