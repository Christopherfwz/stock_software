# -*- coding: utf-8 -*-

import urllib2
import re
import datetime
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')


def getZtCode():
    start_url = 'http://www.iwencai.com/stockpick/robot-search?w=%E6%B6%A8%E5%81%9C%E8%82%A1%E5%88%86%E6%9E%90&querytype=stock&robotResultPerpage=30'
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

def corDate(Numb):
	if int(Numb) < 10:
		correctDate = '0' + str(Numb)
	else:
		correctDate = str(Numb)
	return correctDate

def getnews(search_key):
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
    date_now = datetime.datetime.now()
    date_begin = datetime.datetime.now() + datetime.timedelta(days=-3)
    d_begin = str(date_begin.year) + corDate(date_begin.month) + corDate(date_begin.day)
    d_now = str(date_now.year) + corDate(date_now.now().month) + corDate(date_now.day)

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
    stockCode = getZtCode()
    dict = {}
    for i in range(len(stockCode)):
        dict[stockCode[i]] = getnews(stockCode[i])
    return dict

