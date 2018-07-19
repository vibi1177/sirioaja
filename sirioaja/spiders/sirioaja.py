# -*- coding: utf-8 -*-
import scrapy


class SirioajaSpider(scrapy.Spider):
    name = "sirioaja"
    allowed_domains = ["sirioaja.it"]
    start_urls = [
        'https://sirioaja.it/scuola-per-estetista-contatti/',
    ]

    def parse(self, response):
        yield
        {
            'title' : response.css('title::text').extract_first()
            'name'  : response.xpath(
                '//div[@class="textwidget"]/h3/text()'
            ).extract_first();
            'address'  : response.xpath(
                '//div[@class="textwidget"]/text()'
            ).extract_first();
        }
