from urllib.request import urlopen as u
from selenium import webdriver
import requests
from bs4 import BeautifulSoup as soup
import time

# Set up browser
driver = webdriver.Chrome(executable_path = r"C:\Users\khait\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # You must have ChromeDriver installed

# Load page
driver.get("https://www.newegg.com/p/pl?d=graphic+cards")
time.sleep(5)  # Wait for JavaScript to load

# Get rendered HTML
html = driver.page_source
driver.quit()

# Parse it with BeautifulSoup
Soup = soup(html, 'html.parser')

# Print title or heading
print(Soup.h1.text.strip() if Soup.h1 else "No <h1> found")
