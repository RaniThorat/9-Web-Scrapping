# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 09:36:16 2023

@author: Admin
"""

from bs4 import BeautifulSoup as bs
import requests
link="https://www.amazon.in/Amrutam-Fab-Georgette-AF-11-1_White-Pink_Free/dp/B0B6PPQLGC/?_encoding=UTF8&pd_rd_w=K058H&content-id=amzn1.sym.523d54b6-5e5c-494d-84b4-ef78b981528e&pf_rd_p=523d54b6-5e5c-494d-84b4-ef78b981528e&pf_rd_r=H257Y23RT9HHWTXQVDNQ&pd_rd_wg=9CN8v&pd_rd_r=ac2b4076-5cf2-4fb0-bba8-354c691b9ed6&ref_=pd_gw_deals_4s_t1&th=1&psc=1"
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
title=soup.find_all('div',class_="a-letter-space")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)
