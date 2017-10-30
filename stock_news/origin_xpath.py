# -*- coding: utf-8 -*-


class OriginDict:
    def __init__(self, type, name, time=None, origin=None, other=None):
        self.type = type
        self.name = name
        self.time = time
        self.origin = origin
        if other is not None:

            self.other = other


dict = {}

dict['finance.ifeng.com'] = \
    OriginDict("dynamic",
               "凤凰财经")
dict['news.sina.com.cn'] = \
    OriginDict("static",
               "新浪新闻",
               '//*[@id="navtimeSource"]/text()',
               '//*[@id="navtimeSource"]/span/span/a/text()')
dict['m.cnbeta.com'] = \
    OriginDict("static",
               "cnBeta",
               '/html/body/div[1]/section/div[2]/span[1]/text()',
               '/html/body/div[1]/section/div[2]/span[2]/text()')
dict['trust.eastmoney.com'] = \
    OriginDict("static",
               "东方财富网",
               '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/text()',
               '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/img/@alt')
dict['www.prcfe.com'] = \
    OriginDict("static",
               "中国财经新闻网",
               '/html/body/div[3]/div[1]/ul[1]/li[1]/span/text()',
               '/html/body/div[3]/div[1]/ul[1]/li[2]/span/text()')
dict['stock.eastmoney.com'] = \
    OriginDict("static",
               "东方财富网-股票频道",
               '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/text()',
               '/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/img/@alt')
dict['stock.hexun.com'] = \
    OriginDict("static",
               "和讯网",
               'html/body/div[4]/div/div[1]/span/text()',
               '/html/body/div[4]/div/div[1]/a/text()')
dict['stock.jfinfo.com'] = \
    OriginDict("static",
               "巨丰财经",
               '/html/body/div[2]/div[2]/div[1]/div[1]/span[1]/text()')
dict['stock.n8n8.cn'] = \
    OriginDict("static",
               "多赢股票网",
               '/html/body/div[2]/div[4]/div/div[1]/div[1]/div[1]/div[1]/span[2]/text()')
dict['wallstreetcn.com'] = \
    OriginDict("static",
               "华尔街见闻",
               '//*[@id="app"]/div/main/div/div[4]/div[1]/div[2]/div[1]/span/text()',
               '//*[@id="app"]/div/main/div/div[4]/div[1]/div[2]/div[2]/text()')
dict['web.ql18.com.cn'] = \
    OriginDict("static",
               "钱龙网",
               '/html/body/div[3]/div[4]/div[1]/div[1]/span[1]/text()',
               '/html/body/div[3]/div[4]/div[1]/div[1]/span[2]/text()')
dict['www.a528.net'] = \
    OriginDict("dynamic",
               "足球网址大全")
dict['mini.eastday.com'] = \
    OriginDict("static",
               "东方头条",
               '/html/body/div[7]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/i[1]/text()',
               '/html/body/div[7]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/i[2]/text()')
dict['finance.sina.com.cn'] = \
    OriginDict("static",
               "新浪财经",
               '//*[@id="wrapOuter"]/div/div[4]/span/text()',
               '//*[@id="wrapOuter"]/div/div[4]/span/span/a/text()')
dict['www.sohu.com'] = \
    OriginDict("static",
               "搜狐",
               '//*[@id="news-time"]/text()',
               '//*[@id="article-container"]/div[2]/div[1]/div[1]/div/span[2]/a/text()')
dict['xueqiu.com'] = \
    OriginDict("static",
               "雪球",
               '//*[@id="status-94182504"]/div[1]/div[1]/div[2]/a/text()',
               '//*[@id="status-94182504"]/div[1]/div[1]/div[2]/span/text()')
dict['www.360doc.com'] = \
    OriginDict("static",
               "360doc个人图书馆",
               '//*[@id="bgchange"]/div[2]/div[1]/text()',
               '//*[@id="docsource"]/a/text()')
dict['www.ce.cn'] = \
    OriginDict("static",
               "中国经济网",
               '//*[@id="articleTime"]/text()',
               '//*[@id="articleSource"]/text()')
dict['www.chinanews.com'] = \
    OriginDict("static",
               "中国新闻网",
               time=None,
               origin=None,
               other='//*[@id="cont_1_1_2"]/div[4]/div[2]/text()')
dict['news.xinhuanet.com'] = \
    OriginDict("static",
               "新华网",
               '//*[@id="conTit"]/div/span[1]/text()',
               '//*[@id="source"]/text()')
dict['guba.eastmoney.com'] = \
    OriginDict("static",
               "股吧",
               time=None,
               origin=None,
               other='//*[@id="zwconttb"]/div[2]/text()')
dict['stock.10jqka.com.cn'] = \
    OriginDict("static",
               "同花顺财经",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="sourcename"]/text()')
dict['money.163.com'] = \
    OriginDict("static",
               "网易财经",
               '//*[@id="epContentLeft"]/div[1]/text()[1]',
               '//*[@id="epContentLeft"]/div[1]/text()[2]')
dict['stock.jrj.com.cn'] = \
    OriginDict("static",
               "金融街股票",
               '/html/body/div[14]/div[4]/div[1]/div[3]/p[1]/span[1]/text()',
               '/html/body/div[14]/div[4]/div[1]/div[3]/p[1]/span[2]/text()[2]')
dict['news.hexun.com'] = \
    OriginDict("static",
               "和讯",
               '/html/body/div[4]/div/div[1]/span/text()',
               '/html/body/div[4]/div/div[1]/a/text()')
dict['www.p5w.net'] = \
    OriginDict("static",
               "全景网",
               '/html/body/div[3]/div[1]/div/div[1]/span[1]/time/text()',
               '/html/body/div[3]/div[1]/div/div[1]/span[1]/i[1]/a/text()')
dict['www.howbuy.com'] = \
    OriginDict("static",
               "财经新闻",
               '/html/body/div[2]/div/div[3]/div[2]/div[1]/text()[4]',
               '/html/body/div[2]/div/div[3]/div[2]/div[1]/span[2]/text()')
dict['news.163.com'] = \
    OriginDict("static",
               "网易新闻",
               '//*[@id="epContentLeft"]/div[1]/text()[1]',
               '//*[@id="ne_article_source"]/text()')
dict['stock.qq.com'] = \
    OriginDict("static",
               "腾讯证券",
               '//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[4]/text()',
               '//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[2]/a/text()')
dict['diyitui.com'] = \
    OriginDict("static",
               "第一推",
               '/html/body/div[6]/div[3]/div[1]/div/div[2]/text()',
               '/html/body/div[6]/div[3]/div[1]/div/div[2]/a/text()')
dict['www.china.com.cn'] = \
    OriginDict("static",
               "中国网",
               time=None,
               origin=None,
               other='/html/body/div[5]/div[1]/div[2]/div[1]/text')
dict['cpc.people.com.cn'] = \
    OriginDict("static",
               "十九大新闻",
               '/html/body/div[5]/div[1]/div/p[2]/text()',
               '/html/body/div[5]/div[1]/div/p[2]/a/text()')
# dict[''] = \
#     OriginDict("static",
#                "",
#                '/text()',
#                '/text()')


