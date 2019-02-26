# -*- coding: utf-8 -*-
import xlsxwriter
import time
from twisted.enterprise import adbapi
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AirqualityPipeline(object):
    def open_spider(self, spider):
        self.workbook = xlsxwriter.Workbook('D:/爬虫数据/'+time.strftime("%Y-%m-%d")+'.xlsx')  # 创建一个Excel文件
        self.worksheet = self.workbook.add_worksheet()  # 创建一个sheet
        self.num0=0

    def process_item(self, item, spider):
        print(item['adress'])
        #self.num0 = self.num0 + 1
        #row = 'A' + str(self.num0)
        #data = [item['goods_list'], item['price_list'], item['UnitPrice_list'], time.strftime("%Y-%m-%d")]
        #self.worksheet.write_row(row, data)
        return item

    def close_spider(self, spider):
        self.workbook.close()
