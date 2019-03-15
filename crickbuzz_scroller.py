#============== all library ============#
import requests
import os
import re
import pandas as pdas
from bs4 import BeautifulSoup

#=============== site information =====================#
r = requests.get('https://www.cricbuzz.com/cricket-news') # site link


soup = BeautifulSoup(r.text, 'html.parser')# parse site information
results = soup.find_all('div', attrs={'class':'cb-col cb-col-100 cb-lst-itm cb-lst-itm-lg'})# class name where get infomation

#print(image)
records = []
sl = 0
#===================== hold site necessary information =====================#
#********************** loop start **************************#
for result in results:

    sl = sl+1
    url = 'https://www.cricbuzz.com' + result.find('a')['href']
    tour = result.find('div',attrs={'class':'cb-nws-time'}).get_text()
    imageData =''

    postName = result.find('h2',attrs={'class':'cb-nws-hdln cb-font-18 line-ht24'}).get_text()
    postContent = result.find('div',attrs={'class':'cb-nws-intr'}).get_text()
    pubTime =  result.find('span',attrs={'class':'cb-nws-time'}).get_text()
    image = result.find('a',attrs={'': ''})
    data = image.find('img')
    #print(data.find('src',attrs={'class':'cb-lst-img'}))
    #imageData= 'https://www.cricbuzz.com' + image.find('img').attrs['src']

    records.append((sl,url,tour,postName,postContent,pubTime,imageData))
#********************** loop End **************************#



#===================== Import parce data from sites in csv file  =====================#
#date = datetime.datetime.now()
#data2 = pdas.DataFrame(date,columns=['Date'])
#data2.to_csv('cricbuzz.csv', index=False, encoding='utf-8')
data = pdas.DataFrame(records,columns=['Sl','Post link','On Tour','Post Name','Content','Time','ImageLink'])
if(os.path.isfile('./cricbuzz.csv')):
    os.remove('./cricbuzz.csv')
    data.to_csv('cricbuzz.csv', index=False, encoding='utf-8')
else:
    data.to_csv('cricbuzz.csv', index=False, encoding='utf-8')
