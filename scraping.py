import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import urllib.request

articles_list = []
articleLinks_list = []
articleDates_list = []

#Page 1

sock1 = urllib.request.urlopen("http://kvfrans.com/")
htmlSource1 = sock1.read()
sock1.close()
soup1 = BeautifulSoup(htmlSource1, "html.parser")

#Extract the research article titles and links
for article in soup1.find_all('h2', class_='post-title'):
    articles_list.append(article.string)
    articleLinks_list.append(article.a.get("href"))

#Extract the research article publication dates
for date in soup1.find_all('footer', class_='post-meta'):
    articleDates_list.append(date.time.get("datetime"))

#Page 2
sock2 = urllib.request.urlopen("http://kvfrans.com/page/2/")
htmlSource2 = sock2.read()
sock2.close()
soup2 = BeautifulSoup(htmlSource2, "html.parser")

#Extract the research article titles and links
for article in soup2.find_all('h2', class_='post-title'):
    articles_list.append(article.string)
    articleLinks_list.append(article.a.get("href"))

#Extract the research artice publication dates
for date in soup2.find_all('footer', class_='post-meta'):
    articleDates_list.append(date.time.get("datetime"))

#Extract the research article publication dates
for date in soup2.find_all('footer', class_='post-meta'):
    articleDates_list.append(date.time.get('datetime'))

#Create the dictionary
articles_iter = iter(articles_list)
links_iter = iter(articleLinks_list)
dates_iter = iter(articleDates_list)
europe = { 'spain': { 'capital':'madrid', 'population':46.77 }, 'france': { 'capital':'paris', 'population':66.03 },'germany': { 'capital':'berlin', 'population':80.62 },'norway': { 'capital':'oslo', 'population':5.084 } }
df = pd.DataFrame(europe)
df = df.transpose()
df_dict = {}

print(articles_list)
print(articleLinks_list)
print(articleDates_list)
print(df)
