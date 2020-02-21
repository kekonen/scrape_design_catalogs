# -*- coding: utf-8 -*-
import scrapy
from scrape_design_catalogs.items import HKItem, HKPictureItem
import logging


class HklivingSpider(scrapy.Spider):
    name = 'hkliving'
    allowed_domains = ['hkliving.nl']
    start_urls = [f'https://hkliving.nl/collections/all-products/?q=&page={i}&ItemsPerPage=100&SortTerm=sortorder' for i in range(1,10)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        for product_selector in response.css('.col-6.col-md-6.col-lg-4.col-xl-4'):
            internal_link = product_selector.css('a::attr(href)').get()
            next_page = response.urljoin(internal_link)
            yield scrapy.Request(next_page, callback=self.parse_product)

    def parse_product(self, response):
        product_name = response.css('h2::text').get().replace('\xa0', '')[1:]
        product_description = response.css('.hk_description::text').get().strip()

        specs_selectors = response.css('li.hk_row_specs')[1:]

        specs = {}
        for spec_selector in specs_selectors:
            text_values = [value.strip() for value in spec_selector.css('::text').getall()[1:]]
            spec_name = text_values[0]  #spec_selector.css('strong::text').get()
            spec_value = text_values[1].replace(': ', '')
            
            specs[spec_name] = spec_value

        product = HKItem()

        product['name'] = product_name
        product['description'] = product_description
        product['ean'] = specs['EAN code']
        product['product_code'] = specs['product code']
        product['dimensions'] = specs['dimensions']
        product['weight'] = specs['product weight (gr)']
        yield product

        picture = HKPictureItem()

        picture['product_code'] = specs['product code']
        picture['link'] = response.css('img.img-responsive').attrib['src']
        yield picture

