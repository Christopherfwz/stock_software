# -*- coding: utf-8 -*-

"""Main module."""


import zt_crawler
import url_crawler
import origin_crawler
import iwencai

unsaved = {}
dict = iwencai.start()
for (stock,list) in dict.items():
    print "dict[%s]=" % stock
    for i in list:
        print i+'\n'
        # print unsaved
        news_urls = url_crawler.start(i)
        for j in news_urls:
            # print j
            origin_crawler.origin_crawler(j,unsaved)

print unsaved
