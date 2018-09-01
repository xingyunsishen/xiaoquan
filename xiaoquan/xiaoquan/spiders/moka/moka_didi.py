# -*- coding: utf-8 -*-
import scrapy


class MokaDidiSpider(scrapy.Spider):
    name = 'moka_didi'
    start_urls = ['https://mp.weixin.qq.com/mp/homepage?__biz=MzI4NzM4MTQyMg==']

    def parse(self, response):
        print(response)
