import scrapy
from scrapy import Request
from itertools import product
from hashlib import sha256
from steamparse.items import RaviItem

RED_TEXT_XP = '//div[1]/div[7]/div[2]/div/div[1]/div/div/div/div[4]/div[2]'
IMG_XP = '//div[1]/div[7]/div[3]/div/div[1]/div/div/div/div[2]/div/img/@src'

BASE_URL = 'https://steamcommunity.com/profiles/'
MIDDLE_NUMBER = '76561198'

HEADERS = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

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
            image = image.split('_full')[0] + '.jpg'
            yield Request(url=image, callback=self.parse_after, headers=HEADERS,
                          meta={"image": image,
                                "steam_id": _id})

    def parse_after(self, response):
        context = RaviItem()
        context['index'] = sha256(response.content[:500])
        context['image'] = response.meta.get("image")
        context['steam_id'] = response.meta.get("steam_id")
        return context
