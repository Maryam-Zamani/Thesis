# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FakenewscrawlerItem(scrapy.Item):
	statement_source = scrapy.Field()
	statement_text =  scrapy.Field()
	statement_edition = scrapy.Field()
	