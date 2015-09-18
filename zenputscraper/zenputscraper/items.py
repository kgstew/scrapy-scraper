# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CspediaScraperItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    categoriesOfResponsibilities = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    promotionDate = scrapy.Field()
    company = scrapy.Field()
    address1 = scrapy.Field()
    address2 = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    postalCode = scrapy.Field()
    country = scrapy.Field()


