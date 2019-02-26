# -*- coding: utf-8 -*-
import scrapy
from lxml import etree

from Airquality.items import AirqualityItem


class AirDataSpider(scrapy.Spider):
    name = 'air_data'
    allowed_domains = ['www.pm25.in']
    start_urls = ['http://www.pm25.in']

    def parse(self, response):
        selector=etree.HTML(response.body)
        self.item=AirqualityItem()

        #获取到了全国的城市的拼音，以队列的形式
        cities=selector.xpath('.//div[@class="all"]/div[2]//li/a/@href')
        for city in cities:
            url='http://www.pm25.in'+city
            print(url)
            yield scrapy.Request(url, callback=self.parse_city)

    def parse_city(self,response):
        selector = etree.HTML(response.body)

        adress = selector.xpath('.//tbody/tr/td[1]/text()')
        AQI = selector.xpath('.//tbody/tr/td[2]/text()')
        type = selector.xpath('.//tbody/tr/td[3]/text()')
        first = selector.xpath('.//tbody/tr/td[4]/text()')
        PM_25 = selector.xpath('.//tbody/tr/td[5]/text()')
        PM_10 = selector.xpath('.//tbody/tr/td[6]/text()')
        CO = selector.xpath('.//tbody/tr/td[7]/text()')
        NO2 = selector.xpath('.//tbody/tr/td[8]/text()')
        O3_1 = selector.xpath('.//tbody/tr/td[9]/text()')
        O3_8 = selector.xpath('.//tbody/tr/td[10]/text()')
        SO2 = selector.xpath('.//tbody/tr/td[11]/text()')

        for a,b,c,d,e,f,g,h,i,j,k in zip(adress,AQI,type,first,PM_25,PM_10,CO,NO2,O3_1,O3_8,SO2):
            self.item['adress'] =a
            self.item['AQI'] =b
            self.item['type'] =c
            self.item['first'] =d
            self.item['PM_25'] =e
            self.item['PM_10'] =f
            self.item['CO'] =g
            self.item['NO2'] =h
            self.item['O3_1'] =i
            self.item['O3_8'] =j
            self.item['SO2'] =k
            yield self.item


