# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    capacity = scrapy.Field()
    interface = scrapy.Field()
    color = scrapy.Field()
    size = scrapy.Field()
    weight = scrapy.Field()
