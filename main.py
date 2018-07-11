# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 17:56:50 2017

@author: sean
"""


from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
from selenium import webdriver
import os,re
cwd=os.getcwd()

#http://vsco.co/funkyspion/images/1

USERNAME='haydenscott'
TOTAL_NO=3
RECORD_FILM_TYPE=True


for page_no in range(1,TOTAL_NO+1):
    driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
    driver.get('http://vsco.co/'+USERNAME+'/images/'+str(page_no))
    imageindex_bs=BeautifulSoup(driver.page_source,'lxml')
    
    
    #with film type
    if RECORD_FILM_TYPE:
        names=imageindex_bs.find_all('a',{'href':re.compile('^/'+USERNAME+'/media')})
        name_links=[r'http://vsco.co'+name['href'] for name in names]
        for name_link in name_links:
            driver.get(name_link)
            image_bs=BeautifulSoup(driver.page_source,'lxml')
            film_type=image_bs.find('div', {'class':"DetailViewMetaCollapsible-meta-container"}).span.text
            img_link=r'http:'+re.search('[\s\S]*\.jpg',image_bs.img['src']).group()
            urlretrieve(img_link,cwd+'/imgs/'+film_type+'_'+re.search('\w+.jpg',img_link).group())
    else:
        imgs=imageindex_bs.find_all('img',{'src':re.compile('^//im.vsco.co/aws-us-west-2')})
        img_links=[r'http:'+re.search('[\s\S]*\.jpg',img['src']).group() for img in imgs]
        for i,img_link in enumerate(img_links):
            urlretrieve(img_link,cwd+'/imgs/'+re.search('\w+.jpg',img_link).group())

#without film type
'''    

'''


#<div class="DetailViewMetaCollapsible-meta-container"><span class="mr16">A7</span><time><span class="mr16">December 17, 2017</span><!-- react-text: 2039 --> <!-- /react-text --><!-- react-text: 2040 -->11:00am<!-- /react-text --></time><ul class="MediaSocialShare"><span class="mr10">Share:</span><li><button>Facebook</button></li><li><button>Twitter</button></li><li><button>Pinterest</button></li><li><button>Email</button></li></ul></div>