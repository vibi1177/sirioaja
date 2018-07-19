# -*- coding: utf-8 -*-
import scrapy


class SirioajaSpider(scrapy.Spider):
    name = "sirioaja"
    allowed_domains = ["sirioaja.it"]
    start_urls = [
        'https://sirioaja.it/scuola-per-estetista-contatti/',
    ]

    def parse(self, response):
        yield{'title' : resonse.css('title::text').extract()}
