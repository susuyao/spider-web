# encoding=utf8
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf8')


class Catalog:
    """
    目录结构:
    name: 目录的名称
    url: 目录对应的url(文章列表的导航url)
    articles: 文章集合
    """

    def __init__(self, name, url):
        self.name = name  # 分类目录名称
        self.url = url  # 目录的导航
        self.articles = {}  # 文章列表


def parse(driver):
    html = driver.page_source
    # print html
    soup = BeautifulSoup(html, 'html.parser')
    # print soup
    # soup = soup.prettify()
    # print soup
    urls_list_soup = soup.select('.nav_com > ul > li > a')
    # print urls_list_soup
    # name_list = []
    # urls_list = []
    nav = {}
    for url in urls_list_soup:
        menu_name = url.get_text().strip()
        menu_url = 'https://www.csdn.net' + url.get('href')
        # name_list.append(menu_name)
        # urls_list.append(menu_url)
        nav[menu_name] = menu_url
    # print urls_list, name_list
    return nav


def parse_catalog(driver, catalog):
    driver.get(catalog.url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    detail_urls = soup.select('#feedlist_id > li > div > div.title > h2 > a')

    # 输出具体文章的URL
    ret = catalog.articles
    for u in detail_urls:
        k = u.get_text().strip()
        v = 'https://www.csdn.net' + u.get('href')
        ret[k] = v
    # print 'article URL list: %s.' % ret
    pass


if __name__ == '__main__':
    driver = webdriver.PhantomJS()
    driver.get('https://passport.csdn.net/account/login')
    driver.find_element_by_xpath('//div[@class="row wrap-login"]/div[2]/div/h3/a').click()
    time.sleep(2)
    driver.find_element_by_id('username').send_keys('aiziyuer')
    driver.find_element_by_id('password').send_keys('xxxxx')
    driver.find_element_by_class_name('logging').click()

    driver.get('https://www.csdn.net/')
    time.sleep(1)

    catalog_dict = parse(driver)
    catalogs = []  # 所有的分类文章
    for name, url in catalog_dict.iteritems():
        c = Catalog(name, url)
        parse_catalog(driver, c)
        catalogs.append(c)

    # 打印
    with open('url.csv', 'wb') as f:
        for catalog in catalogs:
            for a_name, a_url in catalog.articles.iteritems():
                # print "%s, %s, %s " % (catalog.name, a_name, a_url)
                data = [catalog.name, a_name, a_url]

                wr = csv.writer(f, dialect=csv.excel, delimiter=',')
                wr.writerow(data)
    driver.quit()
    pass
