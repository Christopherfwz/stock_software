# -*- coding: utf-8 -*-

"""Main module."""


import zt_crawler
import url_crawler
import origin_crawler
import iwencai
import xlwt

unsaved = {}


stockOrigin = xlwt.Workbook()
sheet1 = stockOrigin.add_sheet(u'Sheet1', cell_overwrite_ok=True)

rowCounter = 0


dateStock = iwencai.getZtCode(iwencai.getDate(3))
for ZtCodes in dateStock:
	sheet1.write(rowCounter, 0, iwencai.dateToString(iwencai.getDate(3)))
	sheet1.write(rowCounter, 1, ZtCodes)
	
	news = iwencai.getnews(ZtCodes, iwencai.getDate(3))
	for exactnews in news:
		sheet1.write(rowCounter, 2, exactnews)
		
		news_urls = url_crawler.start(exactnews)
		for urls in news_urls:
			originResults = origin_crawler.origin_crawler(urls,unsaved)
			if originResults:
				columnCounter = 3
				for elemts in originResults:
					sheet1.write(rowCounter, columnCounter, elemts)
					columnCounter += 1
				rowCounter +=1
	
				
stockOrigin.save('newsOrigin.xls')
