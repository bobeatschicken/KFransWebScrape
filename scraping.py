import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import urllib.request

posts_list = []
postsLinks_list = []
postsDates_list = []
postsType_list = []
postsType_list_UPDATED = []

#Page 1

sock1 = urllib.request.urlopen("http://kvfrans.com/")
htmlSource1 = sock1.read()
sock1.close()
soup1 = BeautifulSoup(htmlSource1, "html.parser")

#Extract the blog post titles and links
for article in soup1.find_all('h2', class_='post-title'):
    posts_list.append(article.string)
    postsLinks_list.append(article.a.get("href"))

#Extract the blog post publication dates
for date in soup1.find_all('footer', class_='post-meta'):
    postsDates_list.append(date.time.string)

#Extract the blog post type (research, games, miscellaneous)
for date in soup1.find_all('article'):
    postsType_list.append(date.get("class")[-1])

#Page 2
sock2 = urllib.request.urlopen("http://kvfrans.com/page/2/")
htmlSource2 = sock2.read()
sock2.close()
soup2 = BeautifulSoup(htmlSource2, "html.parser")

#Extract the blog post titles and links
for article in soup2.find_all('h2', class_='post-title'):
    posts_list.append(article.string)
    postsLinks_list.append(article.a.get("href"))

#Extract the blog post publication dates
for date in soup2.find_all('footer', class_='post-meta'):
    postsDates_list.append(date.time.string)

#Extract the blog post type (research, games, miscellaneous)
for date in soup2.find_all('article'):
    postsType_list.append(date.get("class")[-1])

#Edit the postsType_list
for post in postsType_list:
    if post == "tag-research":
        postsType_list_UPDATED.append('Research')
    elif post == "tag-games":
        postsType_list_UPDATED.append('Games')
    else:
        postsType_list_UPDATED.append("Miscellaneous")

#Create the dictionary
links_iter = iter(postsLinks_list)
dates_iter = iter(postsDates_list)
type_iter = iter(postsType_list_UPDATED)
df_dict = {}
for article in posts_list:
    df_dict[article] = {'Category': '','Link': '', 'Publication Date': ''}
for key in df_dict.keys():
    df_dict[key]['Link'] = next(links_iter)
    df_dict[key]['Publication Date'] = next(dates_iter)
    df_dict[key]['Category'] = next(type_iter)
articles_df = pd.DataFrame(df_dict)
articles_df = articles_df.transpose()
print(articles_df)
print(articles_df[np.logical_not(articles_df['Category'] == 'Research')])
