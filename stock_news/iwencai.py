# -*- coding: utf-8 -*-

import urllib2
import re
import datetime
import sys
import time
import xlwt

reload(sys)
sys.setdefaultencoding('utf-8')


def getDate(daysAgo):
	date_got = datetime.datetime.now() + datetime.timedelta(days=-int(daysAgo))
	return date_got


def corDate(Numb):
	if int(Numb) < 10:
		correctDate = '0' + str(Numb)
	else:
		correctDate = str(Numb)
	return correctDate

def dateToString(date):
	date_string=str(date.year)+corDate(date.month)+corDate(date.day)
	return date_string

def getZtCode(date_required):
    basic_url = 'http://www.iwencai.com/'
    date_string = dateToString(date_required)
    start_url=basic_url+'stockpick/robot-search?w=%E6%B6%A8%E5%81%9C%20'+date_string+'&querytype=stock&robotResultPerpage=30'
    req = urllib2.Request(start_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    html = urllib2.urlopen(req).read().decode('utf-8')

    # first-level match
    patern1 = 'stockpick_ztyy&querytype=&tid=stockpick&w=.*?&queryarea=all">.*?</a>'
    temp_result1 = re.compile(patern1).findall(html)
    temp_result = []
    temp_result.extend(temp_result1)

    # second-level handle
    pattern2 = 'stockpick&w=\d+'
    temp_stockcode = re.compile(pattern2).findall(','.join(temp_result))
    pattern3 = '>.*?</a>'
    rise_reason = re.compile(pattern3).findall(','.join(temp_result))

    # third-level handle
    pattern4 = '\d+'
    stockcode = re.compile(pattern4).findall(','.join(temp_stockcode))
    for counter in range(len(rise_reason)):
        rise_reason[counter] = rise_reason[counter][1:][:-4]

        # judge whether the reason is 'new stock'
    counter0 = 0
    while counter0 < len(rise_reason):
        if rise_reason[counter0] == u'\u65b0\u80a1':
            del stockcode[counter0]
            del rise_reason[counter0]
        else:
            counter0 = counter0 + 1

    return stockcode

def getnews(search_key,date_required):
    # make sure search_key and page is valid
    try:
        search_key = str(search_key)

    except TypeError:
        return False

    # modify search_key and page to appropriate format
    key_code = urllib2.quote(search_key)

    # create a request and obtain the page responsed by Baidu
    url = 'http://www.iwencai.com/'

    # set time range for news
    date_now = dateToString(date_required)
    date_begin = dateToString(date_required + datetime.timedelta(days=-3))

    url_all = url + 'diag/block-detail?pid=11656&codes=' + key_code + '&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%22'
    url_all = url_all + d_begin + '%22%2C%22' + d_now + '%22%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A9381%7D%7D%7D'
    req = urllib2.Request(url_all)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    time.sleep(2)
    print url_all
    html = urllib2.urlopen(req).read()

    # use re to select news
    pattern_news = 'abstract.*?source'
    final_news = temp_result1 = re.compile(pattern_news).findall(html)

    for counter in range(len(final_news)):
        final_news[counter] = final_news[counter][11:][:-9].decode('unicode_escape')

    return final_news

def start():
	stockCode = {}
	dict = {}
	f = xlwt.Workbook() 
	sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True) 
    
	for d in range(0,5):
		stockCode[dateToString(getDate(d))] = getZtCode(getDate(d))
		for i in range(len(stockCode[dateToString(getDate(d))])):
			dict[stockCode[dateToString(getDate(d))][i]] = getnews(stockCode[dateToString(getDate(d))][i],getDate(d))
            sheet1.write(i,0,dateToString(getDate(d)))
			sheet1.write(i,1,stockCode[dateToString(getDate(d))][i])
		f.save('stockcode.xls')
	 
	return dict
