# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/c/nd/2017-10-20/doc-ifymzzpv8105066.shtml']

    def parse(self, response):
		item = Project1Item()
		item['title'] = response.xpath('//*[@id="artibody"]/p[1]').extract()
		item['link'] = response.xpath('/html/head/comment()[2]').extract()
		item['desc'] = response.xpath('//*[@id="artibody"]/p[2]').extract()
		yield item
		#filename = response.url.split("/")[-2]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
		
		
		
		
		
