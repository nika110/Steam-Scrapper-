# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



import pymongo

from steamparse import settings

#Append on MONGODB
class SteamparsePipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(settings.MONGODB_HOST, settings.MONGODB_PORT)
        db = self.conn[settings.MONGODB_DB]
        self.collection = db[settings.MONGODB_COLLECTION]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item