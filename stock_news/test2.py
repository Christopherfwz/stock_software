# -*- coding: utf-8 -*-

import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def geturl():
    start_url = 'https://touzi.sina.com.cn/api/openapi.php/TzyFreeService.getDKStocksList?num=1000&qq-pf-to=pcqq.c2c'
    req = urllib2.Request(start_url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    html = urllib2.urlopen(req).read().decode('utf-8')

    # first-level match
    patern1 = '{"stock_code":"\w+\d+"'
    temp_result1 = re.compile(patern1).findall(html)
    temp_result = []
    temp_result.extend(temp_result1)

    # second-level handle
    pattern2 = '\w+\d+'
    result = re.compile(pattern2).findall(','.join(temp_result))

    return result


def getnews(search_key, sizeup_ratio):
    # make sure search_key and page is valid
    try:
        search_key = str(search_key)

    except TypeError:
        return False

    # modify search_key and page to appropriate format
    key_code = urllib2.quote(search_key)

    # create a request and obtain the page responsed by Baidu
    url = 'https://touzi.sina.com.cn/api/openapi.php/'

    url_all = url + 'TzyFreeService.getStockThemes?symbol=' + key_code + '&qq-pf-to=pcqq.c2c'
    req = urllib2.Request(url_all)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    html = urllib2.urlopen(req).read().decode('utf-8')

    pattern_roughly = '"ratio":".+?","abstract":".+?","stocks"'
    pattern_ratio = '"ratio":".+?"'
    pattern_abstract = '"abstract":".+?"'
    pattern_third = ':".+?"'
    pattern_FR = '\d+.\d+'

    temp_result1 = re.compile(pattern_roughly).findall(html)
    temp_result2 = re.compile(pattern_ratio).findall(','.join(temp_result1))
    temp_result3 = re.compile(pattern_abstract).findall(','.join(temp_result1))
    temp_ratio = re.compile(pattern_third).findall(','.join(temp_result2))
    abstract = re.compile(pattern_third).findall(','.join(temp_result3))

    ratio = re.compile(pattern_FR).findall(','.join(temp_ratio))
    for counter in range(len(abstract)):
        abstract[counter] = abstract[counter][2:][:-1].decode('unicode_escape')
        # print abstract[counter]
        # print type(abstract[counter][2:][:-1]).decode('unicode_escape')

        # judge whether the ratio is size up
    counter0 = 0
    while counter0 < len(ratio):
        if float(ratio[counter0]) < sizeup_ratio:
            del ratio[counter0]
            del abstract[counter0]
        else:
            counter0 = counter0 + 1

    return abstract


while True:
    ten = raw_input("Please input the ratio:")
    if ten.isdigit(): break
ten = int(ten)

stockCode = geturl()
dict = {}
for i in range(20):
    dict[stockCode[i]] = getnews(stockCode[i], ten)

print dict
