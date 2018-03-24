from scrapy.linkextractors import LinkExtractor
from scrapy.spider import Rule
from scrapy_redis.spiders import CrawlSpider
from example.items import baiduTieba

class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'dmoz'
    #allowed_domains = ['dmoz.org']
    start_urls = ['http://tieba.baidu.com/p/3707205431']
    img_urls = []
    
    rules = [
        Rule(LinkExtractor(allow=(r"/p/3707205431\?pn")), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):
        #items1 = baiduTieba()
        items = baiduTieba()
        items['title'] = "".join(response.xpath("//title/text()").extract())
        x1 = response.xpath("//img[@class='BDE_Image']/@src").extract()
        items['image_urls'] = x1
        yield items

