# -*- coding: utf-8 -*-
#https://movie.douban.com/subject/26636712/reviews?sort=time

import time
import os
import bs4
from bs4 import BeautifulSoup
import urllib.request
import config.path

# if os.path.exists('./douban.txt'):
#     fileLoc=open('./douban.txt','r',encoding='utf-8')
#     txt = fileLoc.readlines()
#     fileLoc.close()

listContent=[]


urllib.request.urlretrieve("https://img3.doubanio.com/icon/u163051129-4.jpg",'1.jpg')

page = urllib.request.urlopen(config.path.doubanUrl)
htmlcode=page.read()
# htmlcode=txt

# print(htmlcode)
bssoup = BeautifulSoup(htmlcode,features='html.parser')
bspret = bssoup.prettify()
# print(bspret)
# result = bssoup.find_all(attrs={'class':'review-list'})
results = bssoup.find_all(attrs={'typeof':'v:Review'})
#bs4.element.ResultSet
print(type(results),len(results))#,result)
# print(result[0].text)
timeinfo = time.strftime('%Y-%m-%d %H:%M:%S (%A)')
if isinstance(results,list):
    index = 0
    for item in results:
        index+=1
        if isinstance(item,bs4.element.Tag):
            # print(item.text)
            try:
                headid = item.find(attrs={'class':'main review-item'})['id']
                headinfo = item.find(attrs={'class':'main-hd'})
                detail = item.find(attrs={'class':'main-bd'})

                userName=headinfo.find(attrs={'class':'name'}).string
                dateTime=headinfo.find(attrs={'class':'main-meta'}).string
                titile=detail.find('h2').string
                content=detail.find(attrs={'class':'short-content'}).text
                contentStr=content.strip('\n').strip(' ').replace('\n',',')
            except Exception:
                print('analysis html has ERROR!')
            else:
                listContent.append([str(index)+' : '+timeinfo,titile,userName,dateTime,contentStr])
            finally:
                pass
        else:
            print('item is not tag type!')

#保存结果到本地文件
try:
    recordFile=open(config.path.data_douban_path,'a',encoding='utf-8')
    recordFile.write('*** begin time: {0} ***\n'.format(timeinfo))
    for unit in listContent:
        for item in unit:
            recordFile.write(item+'\n')
    recordFile.close()
except Exception as error:
    pass
else:
    print('save success!path={0}'.format(config.path.data_douban_path))

if not os.path.exists(config.path.date_douban_html_path):
    fileLoc=open(config.path.date_douban_html_path,'wb')
    fileLoc.write(htmlcode)
    fileLoc.close()
else:
    print('file(html source code) is exists!!!')
