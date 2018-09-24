import scrapy
from scrapy import Spider
from selenium import webdriver

class CsdnSpider(Spider):
    name = 'csdnspider'
    allowed_domain = ['csdn.net']
    start_urls = ['https://www.csdn.net/']

    headers = {
        'Host':'passport.csdn.net',
        'Referer':'https://www.csdn.net/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    def start_requests(self):
        return [scrapy.Request(url='https://passport.csdn.net/account/login',headers=self.headers,callback=self.login)]

    def login(self,response):
        browser = webdriver.PhantomJS()


    def parse(self, response):
        pass