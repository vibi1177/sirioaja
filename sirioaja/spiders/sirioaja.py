# -*- coding: utf-8 -*-
import scrapy


class SirioajaSpider(scrapy.Spider):
    name = "sirioaja"
    allowed_domains = ["sirioaja.it"]
    start_urls = [
        'https://sirioaja.it/scuola-per-estetista-contatti/',
    ]

    def parse(self, response):
        item  = {}

        item['title'] = response.css('title::text').extract_first()
        item['name'] = response.xpath(
            '//div[@class="textwidget"]/h3/text()'
        ).extract_first()
        item['address'] =  response.xpath(
            '//div[@id="text-3"]/div[@class="textwidget"]/text()'
        ).extract_first()
        item['info'] = response.xpath(
            '//div[@id="text-4"]/div[@class="textwidget"]/text()'
        ).extract_first()
        yield item
