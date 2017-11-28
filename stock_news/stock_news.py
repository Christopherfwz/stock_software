# -*- coding: utf-8 -*-

"""Main module."""


import zt_crawler
import url_crawler
import origin_crawler
import catchKeywords
import iwencai

unsaved = {}


#从iwencai获取当天股票代码和原因，如果所需时间与涨停板时间不同（如输入11日，涨停板上是10日，说明11日停市，无结果），
#此时iwencai返回的list为空，用的时候要判断一下

date = iwencai.getDate(4)
iwencaiResult = iwencai.getZtCode(date)
dateStr = iwencai.dateToString(date)#日期（string），存的时候可用
stockCode = iwencaiResult[0]#股票代码（list）
riseReason = iwencaiResult[1]#涨停原因（list），和代码的list是一一对应的

#验证一下
print dateStr
print stockCode
print riseReason


if stockCode:#判断是否为空，即当天是否开市
	for ZtCodes in stockCode:

		news = iwencai.getnews(ZtCodes, date)
		print news#验证一下
		for exactnews in news:#exactnews是一个股票对应的每一则新闻
			news_urls = url_crawler.start(exactnews)#这一条新闻在百度上拿出来的多个url
			for urls in news_urls:
				originResults = origin_crawler.origin_crawler(urls,unsaved)#每个新闻网站的时间、来源
				
				#用滑稽新写的，修正一下时间来源的格式，得到的originResult一定是含有5个元素的，为新闻网站url、网站名称、时间(2个)来源(1个)或者对应的‘无详细xxx’
				if originResults:
					if len(originResults)==3:
						resultList = catchKeywords.catchKeywords(originResults[2])
						originResults.pop()
						for element in resultList:
							originResults.append(element)
					elif len(originResults)==4:
						resultList = catchKeywords.catchKeywords(originResults[2],originResults[3])
						originResults.pop()
						originResults.pop()
						for element in resultList:
							originResults.append(element)

				print originResults#验证一下
