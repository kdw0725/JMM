import urllib.request
import requests
from bs4 import BeautifulSoup
import json
import datetime
import re
import math
import os
import sys
import time
from pyproj import Proj
from pyproj import transform
from selenium import webdriver
from collections import OrderedDict
'''
def GPSfind(posx, posy):
    dic1 = {}
    dic2 = {}
    dic3 = {}
    dic4 = {}
    for i in range(0,89):
        th = math.radians(i)
        posx_cos = 1879 * math.cos(th) + posx
        posy_sin = 1879 * math.sin(th) + posy
        print(int(posx_cos),int(posy_sin))
        dic1[int(posx_cos)] = int(posy_sin)
    for i in range(90,179):
        th = math.radians(i)
        posx_cos = 1879 * math.cos(th) + posx
        posy_sin = 1879 * math.sin(th) + posy
        print(int(posx_cos), int(posy_sin))
        dic2[int(posx_cos)] = int(posy_sin)
    for i in range(180,269):
        th = math.radians(i)
        posx_cos = 1879 * math.cos(th) + posx
        posy_sin = 1879 * math.sin(th) + posy
        print(int(posx_cos), int(posy_sin))
        dic3[int(posx_cos)] = int(posy_sin)
    for i in range(270,360):
        th = math.radians(i)
        posx_cos = 1879 * math.cos(th) + posx
        posy_sin = 1879 * math.sin(th) + posy
        print(int(posx_cos), int(posy_sin))
        dic4[int(posx_cos)] = int(posy_sin)
    print(dic1)
    print(dic2)
    print(dic3)
    print(dic4)
'''
def research(title):
    client_id = "fechS4lsKMLVwarW0I01"
    client_secret = "MxwdD119Rv"
    encText = urllib.parse.quote(title)
    url = 'https://openapi.naver.com/v1/search/blog?query='+encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode ==200):
        response_body = response.read()
        locinfo = response_body.decode('utf-8')
        print(locinfo)
    else:
        print("Error Code:" + response)
def userGPS():
    client_id = "fechS4lsKMLVwarW0I01"
    client_secret = "MxwdD119Rv"
    location = input("현재 위치를 말씀해 주세요 : ")
    encText = urllib.parse.quote(location)

    url = 'https://openapi.naver.com/v1/search/local?query='+encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        locinfo = response_body.decode('utf-8')
        json_data = json.loads(locinfo)
        item = json_data.get('items')
        posx = item[0].get('mapx')
        posy = item[0].get('mapy')
        print(location+"의 GPS 주소는 ("+posx+","+posy+")입니다.")
        return posx, posy
    else:
        print("Error Code:" + response)


def storeInfo(location):
    client_id = "fechS4lsKMLVwarW0I01"
    client_secret = "MxwdD119Rv"
    encText = urllib.parse.quote(location)

    store_url = 'https://openapi.naver.com/v1/search/local?query='+encText
    request = urllib.request.Request(store_url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode ==200):
        response_body = response.read()
        locinfo = response_body.decode('utf-8')

        json_data = json.loads(locinfo)
        item = json_data.get('items')

        file_data = OrderedDict()

        for j in range(len(item)):
            title = item[j].get('title')
            s_title = re.sub('<.+?>','',title,0,re.I | re.S)
            s_telephone = item[j].get('telephone')
            s_address = item[j].get('address')
            s_roadAddress = item[j].get('roadAddress')
            s_mapx = item[j].get('mapx')
            s_mapy = item[j].get('mapy')
            (a,b) = transGPS(s_mapx,s_mapy)
            store_information = [s_title, s_telephone, s_address, s_roadAddress, a,b]
            for i in store_information:
                if(i==""):
                    print('NULL')
                else:
                    print(i)
            print(sep='\n')
    else:
        print("Error Code:"+response)

def find_info():
    location = input("현재 위치를 말씀해 주세요 : ")
    search_url = 'https://place.map.daum.net/'+str(location)
    res = requests.get(search_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    section_sname = soup.findAll("h2", {"class" : "tit_location"})
    section_pnum = soup.findAll("span", {"class" : "txt_contact"})
    section_addr = soup.findAll("span", {"class" : "txt_address"})

    for name in section_sname:
        print(name)
    for pnum in section_pnum:
        print(pnum)
    for addr in section_addr:
        print(addr)

def search_info():
    location =input("맛집 이름 입력 : ")
    encText = urllib.parse.quote(location)
    search_url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=' + encText

    html = requests.get(search_url).text
    soup = BeautifulSoup(html,'html.parser')
    maps = soup.findAll('div',{'class':"wrap_cont"})
    for b in maps:
        for link in b.findAll('a'):
            if 'href' in link.attrs:
                if 'place' in link.attrs['href']:
                    store_mapping = (link.attrs['href']).split('/')
                    return store_mapping[3]

def menuCraw():
    dt = datetime.datetime.now()
    today_week = dt.weekday()
    url = 'http://skhu.ac.kr/uni_zelkova/uni_zelkova_4_3_view.aspx?idx=350'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    lunch_menu = soup.find_all("td", {"class" : "color606"})
    a = lunch_menu[today_week]
    b = str(a).split('<br/>')
    print(b)

def calGPS(sposx, sposy):
    userGPS()
    if(sposx > posx):
        print(dic1)
    else:
        print("hi")

def matgip():
    client_id = "fechS4lsKMLVwarW0I01"
    client_secret = "MxwdD119Rv"
    location = input("가게 이름 : ")
    encText = urllib.parse.quote(location)

    store_url = 'https://openapi.naver.com/v1/search/local?query='+encText
    request = urllib.request.Request(store_url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode ==200):
        response_body = response.read()
        locinfo = response_body.decode('utf-8')

        json_data = json.loads(locinfo)
        item = json_data.get('items')

        print(item)
    else:
        print("Error Code:"+response)

def transGPS(x,y):
    WGS84 = {'proj': 'latlong', 'datum': 'WGS84', 'ellps': 'WGS84', }
    TM128 = {'proj': 'tmerc', 'lat_0': '38N', 'lon_0': '128E', 'ellps': 'bessel',
             'x_0': '400000', 'y_0': '600000', 'k': '0.9999',
             'towgs84': '-146.43,507.89,681.46'}
    (y,x) = ( transform(Proj(**TM128), Proj(**WGS84), x, y) )
    return x,y

def googleSearch(x,y):
#    mapurl1 = 'https://www.google.co.kr/maps/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/@'+str(x)+','+ str(y)+',20z/data=!4m4!2m3!5m1!10e2!6e5'
    mapurl1 = 'https://www.google.co.kr/maps/search/%EC%9D%8C%EC%8B%9D%EC%A0%90/@'+str(x)+','+ str(y)+',18z/data=!4m4!2m3!5m1!10e2!6e5'
    print(mapurl1)
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extensions')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.get(mapurl1)

    for tickbox in driver.find_elements_by_css_selector("input#section-query-on-pan-checkbox-id"):
        try:
            driver.set_window_size(1920,1080)
            tickbox.click()
            #driver.refresh()
            time.sleep(5)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            #print(soup)
            name = soup.findAll("span", {"jstcache": "143"})
            for i in name:
                print(i.text)
            driver.close()
        except:
            None


if __name__ == '__main__':

    (a, b) = userGPS()
    (x, y) = transGPS(a, b)
    print(x, y)
    googleSearch(str(x)[0:10], str(y)[0:10])

    '''
    storeInfo()
'''
    'https://github.com/s-owl/skhufeeds/blob/master/skhufeeds/crawlers/crawlers/menu.py'

