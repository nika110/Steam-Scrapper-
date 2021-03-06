import scrapy
from scrapy import Request
from itertools import product
from hashlib import sha256
from steamparse.items import RaviItem

RED_TEXT_XP = '//div[1]/div[7]/div[2]/div/div[1]/div/div/div/div[4]/div[2]'
IMG_XP = '//div[1]/div[7]/div[3]/div/div[1]/div/div/div/div[2]/div/img/@src'

BASE_URL = 'https://steamcommunity.com/profiles/'
MIDDLE_NUMBER = '76561198'

QUESTIONMARK_HASH = 'a454f00ccb8f2f1ccf7c08de679700879cf5da996df27362cd9df44137b80cd1'

HEADERS = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

class Spider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['steamcommunity.com', 'steamcdn-a.akamaihd.net']
    start_urls = []

    def start_requests(self):
        for comb in product(range(10), repeat=9):
            ending_number = ''.join(map(str, comb))[::-1]
            ending_number = MIDDLE_NUMBER + ending_number
            url = BASE_URL + ending_number
            request = Request(url=url, callback=self.parse, meta={"steam_id": ending_number})
            yield request

    def parse(self, response):
        image = response.xpath(IMG_XP).extract_first()
        red_text = response.xpath(RED_TEXT_XP).extract()
        if not red_text and image:
            _id = response.meta.get('steam_id')
            image = image.split('_full')[0] + '.jpg'
            yield Request(url=image, callback=self.parse_after, headers=HEADERS,
                          meta={"steam_id": _id,
                                "steam_profile": response.url})

    def parse_after(self, response):
        img_hash = sha256(response.body[:500])
        if img_hash != QUESTIONMARK_HASH:
            context = RaviItem()
            context['_id'] = response.meta.get("steam_id")
            context['image_hash'] = img_hash.hexdigest()
            context['steam_profile'] = response.meta.get("steam_profile")
            return context
