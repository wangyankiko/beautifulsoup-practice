#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup
import re
import urllib
#create the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en,zh-CN;q=0.8,zh;q=0.6'
}
#page_url
all_url = 'http://www.mzitu.com/all/http://www.mzitu.com/all/'
#to get the html
start_html = requests.get(all_url,headers=headers)

#to analyize the html
soup = BeautifulSoup(start_html.text)

all_a = soup.find('div', class_='all').find_all('a')

for a in all_a:
    tittle = a.get_text()
    # delete the space
    path = os.getcwd() + '/' + tittle.encode('utf-8').strip()
    if os.path.exists(path) is False:
        os.mkdir(path)
    if not a:
        print "done!"
        break
    href_url = a['href']
    print href_url
    href_html = requests.get(href_url, headers=headers)
    href_html_soup = BeautifulSoup(href_html.text)
    max_span = href_html_soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()
    count = 1
    for page in range(1, int(max_span)+1):

        page_url = href_url+'/'+str(page)
        print page_url
        img_html = requests.get(page_url, headers=headers)
        img_list = re.findall(r'src="(http.+?\.jpg)"', img_html.text, re.I)

        for imgurl in img_list:
            print 'downloading the %d pitcture of page %s' % (count, tittle)
            temp = path+'/%d.jpg' % count
            print imgurl
            urllib.urlretrieve(imgurl, temp)
            count += 1
    print "the picture of page %s is successfuly" % tittle









