import requests
from requests import RequestException
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver
from .BasicSpider import BasicSpider

class IJCAI(BasicSpider):

    def __init__(self,opt):
        super(IJCAI, self).__init__()
        self.opt = opt

    def get_content(self,url,year):

        page = self.get_page(url)
        soup = BeautifulSoup(page, 'lxml')
        pdf_url = soup.select('.btn-download')

        if pdf_url==[]:
            pattern = re.compile('<p><a href="(.*?)">PDF</a></p>',re.S)
            pdf_url = pattern.findall(page)[0]
            pdf_url = 'https://www.ijcai.org'+pdf_url
        else:
            pdf_url = pdf_url[0]['href']

        print("论文pdf链接:"+str(pdf_url))
        pattern = re.compile('<h1>(.*?)</h1>',re.S)
        res = pattern.findall(page)

        if res == []:
            pattern = re.compile('<p>(.*?)<br />.*?<i>.*?</i>.*?</p>',re.S)
            res = pattern.findall(page)

        title = res[0].strip()
        if '/' in title:
            title = title.replace('/','or')
        print("论文标题:"+str(title))

        self.saveFile(pdf_url,title,year)








