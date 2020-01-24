import requests
from requests import RequestException
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver
from .BasicSpider import BasicSpider

class ACLSeries(BasicSpider):

    def __init__(self,opt):
        super(ACLSeries, self).__init__()
        self.opt = opt

    def get_content(self,url,year):

        page = self.get_page(url)
        soup = BeautifulSoup(page, 'lxml')
        tag = soup.select('#title a')[0]
        pdf_url = tag['href']
        title = tag.get_text().strip()
        print("论文pdf链接:" + str(pdf_url))

        if '/' in title:
            title = title.replace('/','or')
        print("论文标题:"+str(title))

        self.saveFile(pdf_url,title,year)










