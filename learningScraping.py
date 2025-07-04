from urllib.request import urlopen as u
import requests
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/p/pl?d=graphic+cards"
request = requests.get(my_url, headers={'User-Agent': 'Mozilla/5.0'})
print(my_url)
