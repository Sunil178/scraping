import pandas as pd
import numpy as np
from selenium import webdriver
##1)FIRST WAY TO DO IT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome('/usr/local/share/chromedriver', options=chrome_options)
page_num = 300
Title=[]
Link=[]
Body=[]
Source=[]
Label=[]
for i in range(52,301):
    url = f"https://nypost.com/opinion/page/{i}/"
    driver.get(url)
    div = driver.find_elements_by_class_name("article-loop__article")
    i=0
    for a in div:
        ##Scrap the title
        title=a.find_elements_by_class_name("entry-heading")
        Title.append(title[0].text)
        # print(title[0].text)
        ##Scrap the link
        link=a.find_element_by_css_selector('a').get_attribute('href')
        Link.append(link)
        # print(link)
        # print("--"*50)
        print(i, end=",")
        i+=1
    page_articles=len(Title)
    # print("link: ",len(Link))
    ##Scrap the body
    for i in range(page_articles):
        driver.get(Link[i])
        body=driver.find_elements_by_class_name("entry-content")
        # print(body[0].text)
        if body != []:
        	Body.append(body[0].text)
        else:
        	Body.append([""])
        Label.append('Right')
        Source.append('New York Post')
        # print("-"*85)
    # print("-"*85)
    # print("-"*85)
    # print("-"*85)
    data={'Titles':Title, 'Links':Link, 'Articles':Body, 'Source':Source, 'Labels':Label}
    #print(data.values())
    df = pd.DataFrame(data)
    #Comment
    #df.to_csv('New_York_Post.csv',header=True)
    df.to_csv("breitbart.csv",mode='a',header=False)
    Title=[]
    Link=[]
    Body=[]
    Source=[]
    Label=[]
    print(len(Title))
    # driver.close()
