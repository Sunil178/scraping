from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import pandas as pd

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options = chrome_options)

df = pd.read_csv("foxnews_init.csv", index_col=[0])

for title, link in zip(df['Titles'], df['Links']):
	driver.get(link)
	element = wait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "article-body")))
        
	sentences = driver.find_elements_by_xpath("//div[@class='article-body']/p | //div[@class='article-body']/blockquote")
	body = ""
	for sentence in sentences:
	    if not sentence.find_elements_by_tag_name("strong"):
	        body += sentence.text


	data = {'Titles': [title], 'Links': [link], "Articles": [body], "Source": ["Fox News"], "Labels": ["Right"]}
	df = pd.DataFrame(data)
	# df.to_csv('foxnews_init.csv', header = True)
	df.to_csv("foxnews.csv", mode = 'a', header = False)
