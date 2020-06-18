from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


df = pd.read_csv("new_knowhere.csv", index_col=[0])
driver = webdriver.Chrome('/usr/local/share/chromedriver')

i = 0
for title, link, source, label in zip(df["Titles"], df["Links"], df["Source"], df["Labels"]):
	try:
		driver.get(link)
		# driver.get("https://knowherenews.com/event/2b612dad-a026-45ad-9733-dec7f529b5d7")
		# element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "BreakdownEvent_sentence__28gU_")))
		# sentences = driver.find_elements_by_class_name('BreakdownEvent_sentence__28gU_')
		element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "Body_Body__26E4G")))
		body = driver.find_element_by_class_name('Body_Body__26E4G')
		sentences = body.find_elements_by_tag_name("p")

		if sentences:
			para = ""
			for sentence in sentences:
				para += sentence.text
			print(para)
			csv_dic = {"Titles": [title], "Links": [link], "Source": ["Knowhere"], "Articles": [para], "Labels": ["Center"]}
			df = pd.DataFrame(csv_dic)
			df.to_csv("new_knowhere2.csv")

			df1 = pd.read_csv("new_knowhere_all.csv", index_col=[0])
			df2 = pd.read_csv("new_knowhere2.csv", index_col=[0])
			out = df1.append(df2, ignore_index = True)
			out.to_csv("new_knowhere_all.csv")
	except:
		continue
print(i, end=",")
i += 1