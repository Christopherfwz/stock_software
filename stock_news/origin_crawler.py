# -*- coding: utf-8 -*-

import urllib2
import re
from lxml import etree
from origin_xpath import dict
import socket


def origin_crawler(url,unsaved):
    global real_url, res

    socket.setdefaulttimeout(6)
    # url = raw_input("URL:")
    # url = "https://touzi.sina.com.cn/public/strategy/ls"
    # url = "https://finance.ifeng.com/public/strategy/ls"
    # url = "http://finance.sina.com.cn/roll/2017-10-21/doc-ifymzksi0679558.shtml"

    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
        response = urllib2.urlopen(req,timeout=1)
        real_url = response.geturl()  # 获取真实url地址

        proto, rest = urllib2.splittype(real_url)
        res, rest = urllib2.splithost(rest)  # 提取域名（res）
    except:
        print '超时'
        return

    # print real_url,res


    try:
        if dict[res].type == 'dynamic':
            print 1
        elif dict[res].type == 'static':
            req = urllib2.Request(real_url)
            req.add_header('User-Agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
            html = urllib2.urlopen(req,timeout=60).read().decode('utf-8')
            dom = etree.HTML(html)
            xpath_time = dict[res].time
            xpath_origin = dict[res].origin
            time = dom.xpath(xpath_time)[0].encode('utf-8')
            origin = dom.xpath(xpath_origin)[0].encode('utf-8')
            if time is None and origin is None:
                xpath_other = dict[res].other
                other = dom.xpath(xpath_other)[0].encode('utf-8')
                print other

            print '\033[5;43m'+time, origin+' \033[0m!'
        else:
            print '数据库信息不完整，当前页面无法处理。'
    except KeyError:
        print '当前网站未收录，无法处理。 网站域名：' + res
        if unsaved.get(res) is not None:
            unsaved[res] = unsaved.get(res)+1
        else:
            unsaved[res] = 1
    except:
        print '未知错误。'

