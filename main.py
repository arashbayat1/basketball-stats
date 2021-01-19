import pandas as pd
from selenium import webdriver
from BeautifulSoup import BeautifulSoup

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

player = []
team = []
age = []
minutes = []
fg = []
fg % = []
threep = []
threep % = []
ftm = []
ft % = []
rb = []
ast = []
stl = []
blk = []
tov = []
pts = []
driver.get("<a href="https: // www.basketball-reference.com/leagues/NBA_2021_per_game.html">https://www.basketball-reference.com/leagues/NBA_2021_per_game.html")

content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('a')
