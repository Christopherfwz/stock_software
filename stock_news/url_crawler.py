# -*- coding: utf-8 -*-

import urllib2
import re


# this function receives two parameters
# search_key stands for what you want to search
# page stands for which page you want to obtain
# function will return False if parameters are not valid
# otherwise, it will return a list containing all the urls
# if the list return by function is empty, it means that there's no result.

def crawl(search_key, page=1):
    # make sure search_key and page is valid
    try:
        search_key = str(search_key)
        page = int(page)
    except TypeError:
        return False

    # modify search_key and page to appropriate format
    key_code = urllib2.quote(search_key)
    page_code = str((page - 1) * 10)

    # create a request and obtain the page responsed by Baidu
    url = 'https://www.baidu.com/'
    url_all = url + 's?wd=' + key_code + '&pn=' + page_code
    req = urllib2.Request(url_all)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    try:
        html = urllib2.urlopen(req,timeout=10).read().decode('utf-8')
    except:
        print '读取url发生错误'
        result_error= []
        return result_error

    # first-level match
    patern1 = '}"\s*href = ".+?"\s*target="_blank"'
    patern2 = '<h3 class="t c-gap-bottom-small">\s*<a href=".+?" target="_blank">'
    temp_result1 = re.compile(patern1).findall(html)
    temp_result2 = re.compile(patern2).findall(html)
    temp_result = []
    temp_result.extend(temp_result1)
    temp_result.extend(temp_result2)

    # second-level handle
    pattern3 = 'href = ".+?"'
    result = re.compile(pattern3).findall(','.join(temp_result))

    # third-level handle
    for counter in range(len(result)):
        result[counter] = result[counter][8:][:-1]

    return result

def start(search_key):
    # search_key = raw_input('请输入关键词（关键词之间用空格隔开）：')
    # page = int(raw_input('请输入要记录的结果页数：'))
    page = 3
    result = []
    for i in range(0, page):
        result.extend(crawl(search_key, i))
    return result
