import urllib.request as re
import requests
import urllib
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument("--headless")  

def getExt(ar):
    result = ""
    l = len(ar)
    for i in range(1,l):
        if ar[-i] == '.' : break
        else :
            result = ar[-i] + result
    return result

    
print(getExt("holaamiguito.exec"))


num = 0
driver = webdriver.Chrome(chrome_options=chrome_options)
tags = ['g']
for tag in tags:
    driver.get("http://boards.4channel.org/" + tag + "/catalog")
    threads = driver.find_element_by_id('threads').get_attribute('innerHTML')
    threads = BeautifulSoup(threads,'html.parser')
    threads = threads.find_all('div',{'class':'thread'})
    threadsId = list(map(lambda x : x['id'][7:],threads)) 
    for thread in threadsId :
        thread = requests.get("http://boards.4channel.org/" + tag + "/thread/" + thread)
        thread = BeautifulSoup(thread.text,'html.parser')
        thread = thread.find_all('a',{'class':'fileThumb'})
        for ima in thread :
            print (ima['href'])
            re.urlretrieve("http:" + ima['href'], tag + '/' + str(num) + '.' + getExt(ima['href']))
            num += 1




driver.close()

