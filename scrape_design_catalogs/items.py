# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeDesignCatalogsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class HKItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    description = scrapy.Field()
    ean = scrapy.Field()
    product_code = scrapy.Field()
    dimensions = scrapy.Field()
    weight = scrapy.Field()
    all_specs = scrapy.Field()
    # pass

class HKPictureItem(scrapy.Item):
    # define the fields for your item here like:
    product_code = scrapy.Field()
    link = scrapy.Field()