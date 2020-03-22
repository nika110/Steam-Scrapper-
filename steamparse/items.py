# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RaviItem(scrapy.Item):
    _id = scrapy.Field()
    image_hash = scrapy.Field()
    steam_profile = scrapy.Field()
