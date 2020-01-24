import requests
from requests import RequestException
from bs4 import BeautifulSoup
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from .BasicSpider import BasicSpider

class AAAI(BasicSpider):

    def __init__(self,opt):
        super(AAAI, self).__init__()
        self.opt = opt

    def get_content(self,url,year):
        if year == 2019:

            page = self.get_page(url)
            soup = BeautifulSoup(page, 'lxml')
            pdf_url = soup.select('.pdf')
            title = soup.select('.page_title')
            pdf_url = pdf_url[0]['href']
            title = title[0].get_text().strip()

        else:

            url = url.replace('view', 'viewPaper')

            while True:
                try:
                    chrome_options = Options()
                    chrome_options.add_argument('--headless')
                    chrome_options.add_argument('--disable-gpu')
                    # browser = webdriver.Chrome(executable_path="E:\\chromedriver",chrome_options=chrome_options)
                    browser = webdriver.Chrome(chrome_options=chrome_options)
                    browser.get(url)
                    browser.implicitly_wait(10)
                    pdf_url = browser.find_element_by_css_selector('#paper a')
                    pdf_url = pdf_url.get_attribute('href')
                    pdf_url = pdf_url.replace('view', 'viewFile')
                    title = browser.find_element_by_css_selector('#title')
                    title = title.text.strip()
                    if browser:
                        browser.close()
                    break
                except NoSuchElementException:
                    if browser:
                        browser.close()
                    print('selenium fail,重试。')
                    continue
            '''
            page = get_page(url)
            soup = BeautifulSoup(page, 'lxml')
            pdf_url = soup.select('#paper a')
            pdf_url = pdf_url[0]['href']
            pdf_url = pdf_url.replace('view', 'viewFile')
            print(pdf_url)
            title = soup.select('#title')
            title = title[0].get_text().strip()
            '''

        if '/' in title:
            title = title.replace('/', 'or')
        print("论文pdf链接:" + str(pdf_url))
        print("论文标题:" + str(title))

        self.saveFile(pdf_url,title,year)










