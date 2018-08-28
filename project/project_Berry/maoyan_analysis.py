# -*- coding: utf-8 -*-
#https://movie.douban.com/subject/26636712/reviews?sort=time

import os
from bs4 import BeautifulSoup
import urllib.request

# if os.path.exists('./douban.txt'):
#     fileLoc=open('./douban.txt','r',encoding='utf-8')
#     txt = fileLoc.readlines()
#     fileLoc.close()

page = urllib.request.urlopen('https://movie.douban.com/subject/26636712/reviews?sort=time')
htmlcode=page.read()
# htmlcode=txt

# print(htmlcode)
bssoup = BeautifulSoup(htmlcode,features='html.parser')
bspret = bssoup.prettify()
# print(bspret)
result = bssoup.find_all(attrs={'class':'review-list'})
#bs4.element.ResultSet
print(type(result),len(result))#,result)
# print(result[0].text)
d2 = result[0].contents
for item in d2:
    if type(item)==bs4.element.Tag):
        print(item.text)

if not os.path.exists('./douban.txt'):
    fileLoc=open('./douban.txt','wb')
    fileLoc.write(htmlcode)
    fileLoc.close()
else:
    print('file is exists!!!')