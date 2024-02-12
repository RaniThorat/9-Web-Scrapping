# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:45:49 2023

@author: Admin
"""

from bs4 import BeautifulSoup as bs
import requests
link="https://www.flipkart.com/canon-eos-m50-mark-ii-mirrorless-camera-ef-m15-45mm-stm-lens/p/itm7a4f536cb1255?pid=DLLGFY7XYG8YFMQT&lid=LSTDLLGFY7XYG8YFMQTSG43XC&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&fm=organic&iid=1d97eeeb-ef47-42d3-849c-46a8a4d69f51.DLLGFY7XYG8YFMQT.SEARCH&ppt=None&ppn=None&ssid=4c3kbq7zs00000001701746883938"
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
title=soup.find_all('p',class_="_2-N8zT")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)
#wWe get 10 review title 
####################################################

#For rating 
rating=soup.find_all('div',class_="_3LWZlK _1BLPMq")
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
len(rate)



#######################################################
#For extracting the text 
text=soup.find_all('div',class_="t-ZTKy")
text
text_p=[]
for i in range(0,len(text)):
    text_p.append(text[i].get_text())
text_p
len(text_p)




#########################################################
import pandas as pd
df=pd.DataFrame()
df['Review Title']=review_title
df['Rating']=rate
df['Review']=text_p
df



#####################################################
#To create csv file
df.to_csv("D:/Data Science/11-web scrapping/flipkart_reviews.csv",index=True)

####################################################3
#Sentiment Analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol
df=pd.read_csv("D:/Data Science/11-web scrapping/flipkart_reviews.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
