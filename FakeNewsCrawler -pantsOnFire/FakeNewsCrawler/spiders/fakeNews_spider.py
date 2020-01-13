import scrapy
from FakeNewsCrawler.items import FakenewscrawlerItem

class QuotesSpiderSpider(scrapy.Spider):
    name = 'news_spider'
    allowed_domains = ['politifact.com']
    start_urls = ['https://www.politifact.com/truth-o-meter/rulings/pants-fire/']

    def parse(self, response):
        newsSet = response.css("div.statement__body") 
        for news in newsSet :
            statement_source = news.css("p.statement__source a::text").extract_first()
            statement_text = news.css("p.statement__text a.link::text").extract_first()
            statement_edition = news.css("p.statement__edition span.article__meta::text").extract_first()
            
            item = FakenewscrawlerItem()
            item["statement_source"] = statement_source 
            item["statement_text"] = statement_text 
            item["statement_edition"] = statement_edition 
            
            yield item
            
            
            

        next_page_url = response.css('body > div.container-outer > div > div.pfmaincontent > div.content > div > main > div > span > a.step-links__next::attr(href)').extract_first()
        #next_page_url = response.xpath("//div[@class='pagination']//a/@href").extract_first()
        print(next_page_url)
        if next_page_url:
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url = absolute_next_page_url, callback = self.parse)