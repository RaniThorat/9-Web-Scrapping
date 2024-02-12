# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:36:10 2023

@author: Admin
"""

from bs4 import BeautifulSoup as bs
import requests
link="https://sanjivanicoe.org.in/index.php.contact"
page=requests.get(link)
page
#<Response [200]> it means connection is scuuessfully extablish
page.content
#you will get all html source conde byt very crowdy text
#Let us apply html parser
soup=bs(page.content,'html.parser')
soup
#Now the text is clean but not upto the expectations
print(soup.prettify())
#the textt is neat and clean
list(soup.children)
#Finding all content using lab
soup.find_all('p')
#suppose you want to exteact contents from
#first row 
soup.find_all('p')[1].get_text()
#Content from seonnd row
soup.find_all('p')[2].get_text()
#Finding text using class
soup.find_all('div',class_='table')
