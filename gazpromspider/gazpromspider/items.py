# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GazpromspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    job_title = scrapy.Field()
    company_name = scrapy.Field()
    crawled_date = scrapy.Field()
    posted_date = scrapy.Field()
    job_description = scrapy.Field()
    job_url = scrapy.Field()

