# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 09:20:24 2023

@author: Admin
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(open("D:/Data Science/11-web scrapping/sample_doc.html"),'html.parser')
print(soup)
#It is going to show all the html contents extracted
soup.text
#It will show only text
soup.contents
#It is going to show all html contents exptracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table
for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)

#It will show all the row except first row
#Now we want to disply M.tech wjhich is located in third row and second crowdy text
table.find_all('tr')[3].find_all('td')[3]
