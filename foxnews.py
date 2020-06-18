from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from time import sleep
import pandas as pd
url = "https://www.foxnews.com/opinion/"

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get(url)
element = wait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, "article")))

for i in range(300):
	try:
		print(i, end=",")
		buttons = driver.find_elements_by_xpath("//div[@class='button load-more js-load-more']/a")
		sleep(5)
		buttons[0].click()
		buttons[1].click()
	except:
		continue

article_list = driver.find_elements_by_xpath("//div[@class='content article-list']/article[@class='article']/div[@class='info']/header[@class='info-header']/h4[@class='title']/a")
print(len(article_list))
article_titles = []
links = []
for article in article_list:
	try:
		if "https://video." not in article.get_attribute("href") and article.text not in article_titles and article.text and article.get_attribute("href"):
			article_titles.append(article.text)
			print(article.text)
			links.append(article.get_attribute("href"))
			print(article.get_attribute("href"))
			print("-"*40)
	except:
		continue

data={'Titles': article_titles, 'Links': links}
df = pd.DataFrame(data)
# df.to_csv('foxnews_init.csv', header = True)
df.to_csv("foxnews_init.csv", mode = 'a', header = False)


# driver.close()