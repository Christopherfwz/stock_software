# -*- coding: utf-8 -*-

"""Main module."""


import zt_crawler
import url_crawler
import origin_crawler
import iwencai
import xlwt
import xlrd
from xlutils.copy import copy

unsaved = {}
dict = iwencai.start()

f = copy(xlrd.open_workbook('stockcode.xls'))
sheet1 = f.sheets()[0]
sheet2 = f.add_sheet(u'sheet2', cell_overwrite_ok=True)

rowCounter1 = 0
rowCounter2 = 0

for (stock,list) in dict.items():
    print "dict[%s]=" % stock
    columnCounter1 = 3
    for i in list:
        print i+'\n'
        sheet1.write(rowCounter1,columnCounter1,i)
        columnCounter1 += 1
        
        columnCounter2 = 0
        sheet2.write(rowCounter2,columnCounter2,i)
        columnCounter2 += 1
        
        # print unsaved
        news_urls = url_crawler.start(i)
        
        for j in news_urls:
            # print j
            originResult = origin_crawler.origin_crawler(j,unsaved)
            
            sheet2.write(rowCounter2,columnCounter2,j)
            columnCounter2 += 1
            sheet2.write(rowCounter2,columnCounter2,originResult.time())
            columnCounter2 += 1
            sheet2.write(rowCounter2,columnCounter2,originResult.origin())
            columnCounter2 += 1
            sheet2.write(rowCounter2,columnCounter2,originResult.other())
            
            rowCounter2 +=1
            columnCounter2 = 1
        
    rowCounter1 += 1

f.save('stockOrigin.xls')

print unsaved
