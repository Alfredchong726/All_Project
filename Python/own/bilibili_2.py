import os
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

url = "http://www.kakadm.com/anime/2417"

response = requests.get(url, headers=header)
html = response.text

soup = BeautifulSoup(html, "html.parser")
urls = soup.find("div", class_="movurl").find_all("a")
print(urls)
