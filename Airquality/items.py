# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirqualityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    adress = scrapy.Field()
    AQI = scrapy.Field()
    type = scrapy.Field()
    first = scrapy.Field()
    PM_25 = scrapy.Field()
    PM_10 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O3_1 = scrapy.Field()
    O3_8 = scrapy.Field()
    SO2 = scrapy.Field()
    pass
