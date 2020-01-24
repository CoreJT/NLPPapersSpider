import requests
from requests import RequestException
from bs4 import BeautifulSoup
import re
from config import *
import os
from selenium import webdriver
from hashlib import md5

class BasicSpider:

    def __init__(self, opt=None):
        self.model_name = str(type(self))  # 模型的默认名字

    def get_page(self,url, flag=True, threshold=20):
        count = 0
        while True:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',

                }
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    response.encoding = response.apparent_encoding
                    if flag:
                        return response.text
                    else:
                        return response.content
                return None
            except RequestException:
                print('fail')
                count = count + 1
                if count >= threshold:
                    break
                continue

    def get_url(self,page):
        soup = BeautifulSoup(page, 'lxml')
        urls = []

        for i,a in enumerate(soup.select('.publ-list .inproceedings .publ ul .drop-down .head a')):
            if i%4==0:
                urls.append(a['href'])

        if urls!=[]:
            p_str = soup.select('#completesearch-info-matches')[0].get_text()
            if 'one' not in p_str:
                pattern = re.compile('\d+',re.S)
                num = pattern.findall(p_str)[0]
            else:
                num = 1
            assert int(num)==len(urls)
            return urls

        return None

    def saveFile(self,pdf_url, title, year):
        '''
        if '/' in self.opt.Meeting:
            meeting = self.opt.Meeting.replace('/','_')
        else:
            meeting = self.opt.Meeting
        '''
        name = self.opt.path+str(self.opt.Field) + '/' + str(self.opt.Meeting) + '/' + str(year)
        if not os.path.exists(name):
            os.makedirs(name)
        #filepath = name + '/{}.pdf'.format(title)
        filepath = name + '/{}.pdf'.format(md5(title.encode()).hexdigest())
        #filepath = name + '/{}.pdf'.format(pdf_url.split('/')[-1])
        if not os.path.exists(filepath):
            content = self.get_page(pdf_url, False)
            if content != None:
                with open(filepath, 'wb') as f:
                    f.write(content)
        else:
            print("已经下载过了！")

    def main(self):
        for year in self.opt.Years:
            print("{0}:".format(year))
            for keyword in self.opt.Keywords:
                keyword1 = self.opt.Meeting+' '+keyword
                #url = 'https://dblp.uni-trier.de/search?q={0}%20venue%3A{1}%3A%20year%3A{2}%3A'.format(keyword,self.opt.Meeting,year)
                url = 'https://dblp.uni-trier.de/search?q={0}%20year%3A{1}%3A'.format(keyword1,year)
                page = self.get_page(url)
                urls = self.get_url(page)

                if urls != None:
                    print("所有论文页面url提取成功！共{0}篇。".format(len(urls)))
                    for url1 in urls:
                        print("论文页面:" + str(url1))
                        self.get_content(url1, year)
                else:
                    print("年份:{0},关键词:{1} 没有相关论文！".format(year,keyword))


