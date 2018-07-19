# -*- coding: utf-8 -*-
import scrapy


class SirioajaSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["sirioaja.it"]
    start_urls = [
        'https://sirioaja.it/scuola-per-estetista-contatti/',
    ]

    def parse(self, response):
        yield{resonse.css('title::text').extract_first()}
