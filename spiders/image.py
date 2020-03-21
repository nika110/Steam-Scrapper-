import scrapy
from scrapy import Request
from itertools import product
from steamparse.items import RaviItem

RED_TEXT_XP = '//div[1]/div[7]/div[2]/div/div[1]/div/div/div/div[4]/div[2]'
IMG_XP = '//div[1]/div[7]/div[3]/div/div[1]/div/div/div/div[2]/div/img/@src'

BASE_URL = 'https://steamcommunity.com/profiles/'
MIDDLE_NUMBER = '76561198'

class Spider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['steamcommunity.com']
    start_urls = []

    def start_requests(self):
        for comb in product(range(10), repeat=9):
            ending_number = ''.join(map(str, comb))[::-1]
            ending_number = MIDDLE_NUMBER + ending_number
            url = BASE_URL + ending_number
            request = Request(url=url, callback=self.parse, meta={"steamid": ending_number})
            yield request

    def parse(self, response):
        image = response.xpath(IMG_XP).extract_first()
        red_text = response.xpath(RED_TEXT_XP).extract()
        _id = response.meta.get('steamid')
        if not red_text and image:
            context = RaviItem()
            context['image'] = image
            context['_id'] = _id
            return context