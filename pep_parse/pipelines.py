import time
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

# from itemadapter import ItemAdapter


# class PepParsePipeline:
#     def process_item(self, item, spider):
#         return item
import csv




class PepToCsvPipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        pass

    def close_spider(self, spider):
        pass