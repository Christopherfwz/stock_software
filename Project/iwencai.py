# -*- coding: utf-8 -*-

import requests
import re
import datetime
import sys
import time

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
	print start_url
	
	req = requests.Session()
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Connection': 'keep-alive',
		'Host': 'www.iwencai.com',
		'Cookie': 'other_uid=Ths_iwencai_Xuangu_ht9qa8bpgdo095kgkbvubk8fw05fjisb; other_uname=vp879mirqz; v=AlG6IT0z70gKvgNcdVyPsEdYZlbvvsU3bzJpRDPmTZg32n-Aew7VAP-CeRfD;',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
	}
	req.headers.update(headers)
	resp = req.get(start_url)
	html = resp.text
	
	# judge whether the date is true
	pattern_d1 = 'natl_box" title="\d+.*?status'
	pattern_d2 = 'title=".*?'+u'\u65e5'
	d0 = re.compile(pattern_d1).findall(html)
	d1 = re.compile(pattern_d2).findall(','.join(d0))
	d1[0] = d1[0][7:]
	date_wanted = str(date_required.year)+u'\u5e74'+str(date_required.month)+u'\u6708'+str(date_required.day)+u'\u65e5'
	if d1[0]!=date_wanted:
		return

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

	return stockcode,rise_reason

def getnews(search_key,date_required):

	# create a request and obtain the page responsed by Baidu
	url = 'http://www.iwencai.com/'

	# set time range for news
	date_now = dateToString(date_required)
	date_begin = dateToString(date_required + datetime.timedelta(days=-3))

	url_all = url + 'diag/block-detail?pid=11656&codes=' + search_key + '&codeType=stock&info=%7B%22view%22%3A%7B%22nolazy%22%3A1%2C%22parseArr%22%3A%7B%22_v%22%3A%22new%22%2C%22dateRange%22%3A%5B%22'
	url_all = url_all + date_begin + '%22%2C%22' + date_now + '%22%5D%2C%22staying%22%3A%5B%5D%2C%22queryCompare%22%3A%5B%5D%2C%22comparesOfIndex%22%3A%5B%5D%7D%2C%22asyncParams%22%3A%7B%22tid%22%3A9381%7D%7D%7D'
	
	req = requests.Session()
	headers = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh-CN,zh;q=0.8',
		'Connection': 'keep-alive',
		'Host': 'www.iwencai.com',
		'Cookie': 'other_uid=Ths_iwencai_Xuangu_ht9qa8bpgdo095kgkbvubk8fw05fjisb; other_uname=vp879mirqz; v=AlG6IT0z70gKvgNcdVyPsEdYZlbvvsU3bzJpRDPmTZg32n-Aew7VAP-CeRfD;',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
	}
	req.headers.update(headers)
	resp = req.get(url_all)
	html = resp.text
	
	# req = urllib2.Request(url_all)
	# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
	# html = urllib2.urlopen(req).read()
	time.sleep(2)


	# use re to select news
	pattern_news = 'abstract.*?source'
	final_news = temp_result1 = re.compile(pattern_news).findall(html)

	for counter in range(len(final_news)):
		final_news[counter] = final_news[counter][11:][:-9].decode('unicode_escape')

	return final_news
