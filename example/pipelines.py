# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from datetime import datetime
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class ExamplePipeline(object):
    def process_item(self, item, spider):
        item["crawled"] = datetime.utcnow()
        item["spider"] = spider.name
        return item

class MyImagesPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
          for image_url in item['image_urls']:
              yield Request(image_url)
              
    def item_completed(self, results, item, info):
         image_path = [x['path'] for ok,x in results if ok]
         if not image_path:
             raise DropItem('Item contains no images')
         item['image_paths'] = image_path
         return item