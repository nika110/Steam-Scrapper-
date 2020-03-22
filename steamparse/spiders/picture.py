# -*- coding: utf-8 -*-
import scrapy


class PictureSpider(scrapy.Spider):
    name = 'picture'
    allowed_domains = ['steamcommunity.com', 'steamcdn-a.akamaihd.net']
    start_urls = []

    def parse(self, response):
        pass
