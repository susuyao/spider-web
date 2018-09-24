# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    menu_url = scrapy.Field()
    menu_name = scrapy.Field()
    next_url = scrapy.Field()
    next_name = scrapy.Field()
