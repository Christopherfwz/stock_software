# -*- coding: utf-8 -*-

"""Main module."""


import zt_crawler
import url_crawler
import origin_crawler
import iwencai
import xlwt

unsaved = {}

iwencaiResult = iwencai.start()
dateStock = iwencaiResult[0]
dict = iwencaiResult[1]

stockOrigin = xlwt.Workbook()
sheet1 = stockOrigin.add_sheet(u'Sheet1', cell_overwrite_ok=True)


rowCounter = 0
for (dates, stockcodes) in dateStock.items():
	for i in dateStock[dates]:
		columnCounter = 0
		sheet1.write(rowCounter, columnCounter, dates)
		columnCounter = 1
		sheet1.write(rowCounter, columnCounter, i)
		rowCounter += 1

rowCounter = 0
for (stock,list) in dict.items():
	columnCounter = 2
	for i in list:
		sheet1.write(rowCounter, columnCounter, i)
		columnCounter += 1
	rowCounter += 1

sheet2 = stockOrigin.add_sheet(u'Sheet2', cell_overwrite_ok=True)



stockOrigin.save('newsOrigin.xls')
