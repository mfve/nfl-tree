from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd 

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
coaches = [] # Map of coaches to links

driver.get("https://en.wikipedia.org/wiki/List_of_current_National_Football_League_head_coaches")


def retrieve_source(driver, url):
    driver.get(url)
    driver.find("table")