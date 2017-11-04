# -*- coding: utf-8 -*-


class OriginDict:
    def __init__(self, type, name, time=None, origin=None, other=None, decoding=None):
        self.type = type
        self.name = name
        self.time = time
        self.origin = origin
        self.decoding = decoding
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
               ['/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/text()','/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/text()','/html/body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/text()'],
               ['/html/body/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/img/@alt','/html/body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/a/text()','/html/body/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/img/@alt'])
dict['stock.hexun.com'] = \
    OriginDict("static",
               "和讯网",
               'html/body/div[4]/div/div[1]/span/text()',
               'GB2312',
               ['/html/body/div[4]/div/div[1]/a/text()','/html/body/div[2]/div/div[3]/div[2]/div[1]/span[2]'])
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
# dict['finance.sina.com.cn'] = \
#     OriginDict("static",
#                "新浪财经",
#                time=None,
#                origin=None,
#                other='//*[@id="wrapOuter"]/div/div[4]/span/text()')
dict['www.sohu.com'] = \
    OriginDict("static",
               "搜狐",
               '//*[@id="news-time"]/text()',
               '//*[@id="article-container"]/div[2]/div[1]/div[1]/div/span[2]/a/text()')

dict['www.ccstock.cn'] = \
    OriginDict("static",
               "中国资本证券网",
               time=None,
               origin=None,
               other='//*[@id="left"]/div[1]/div/span/text()')

dict['www.cfi.net.cn'] = \
    OriginDict("static",
               "中财网",
               time=None,
               origin=None,
               other='//*[@id="tdcontent"]/table/tbody/tr/td[2]')

dict['www.cs.com.cn'] = \
    OriginDict("static",
               "中证网",
               '/html/body/div[4]/div[1]/div[1]/span[3]/text()',
               '/html/body/div[4]/div[1]/div[1]/span[2]/text()')

dict['www.csiii.cn'] = \
    OriginDict("dynamic",
               "中证资讯", )

dict['www.cx368.com'] = \
    OriginDict("static",
               "中国财讯网",
               '//*[@id="article-cmt"]/div[1]/div/div/table/tbody/tr/td[1]/span[2]/text()',
               '//*[@id="article-cmt"]/div[1]/div/div/table/tbody/tr/td[1]/text()')

# dict['www.dsd168.cn'] = \
#     OriginDict("static",
#                "安徽大时代",
#                '//*[@id="content"]/div/div[1]/div[2]/text()',
#                origin=None)
dict['www.ecjr.com'] = \
    OriginDict("static",
               "和讯易财",
               '/html/body/div[5]/div[1]/p/span[3]/text()',
               '/html/body/div[5]/div[1]/p/span[2]/text()')

dict['www.eeworld.com.cn'] = \
    OriginDict("static",
               "电子工程世界",
               '//*[@id="newsptit"]/div[1]/div/h6/span[1]/text()',
               '//*[@id="newsptit"]/div[1]/div/h6/span[2]/text()')

dict['www.esmchina.com'] = \
    OriginDict("static",
               "国际电子商情",
               '//*[@id="app"]/div/main/section/article/header/div/div/ul/li[1]/text()',
               '//*[@id="app"]/div/main/section/article/header/div/div/ul/li[3]/text()')

dict['www.eweb.net.cn'] = \
    OriginDict("static",
               "侃股网",
               '//*[@id="ct"]/div[1]/div[1]/div[1]/p/text()',
               '//*[@id="ct"]/div[1]/div[1]/div[1]/p/a/text()')

# 来源写在正文末尾，基本是投资快报
# dict['www.fxk8.com'] = \
#     OriginDict("static",
#                "风险看吧股市内参",
#                '//*[@id="divMainn"]/div/h4/text()[1]',
#                origin=None)

dict['www.gg-led.com'] = \
    OriginDict("static",
               "高工LED网",
               '//*[@id="meyu"]/div[2]/span[1]/text()[1]',
               '//*[@id="meyu"]/div[2]/span[1]/text()[2]')

dict['www.gushi263.com'] = \
    OriginDict("static",
               "263股票行情网",
               time=None,
               origin=None,
               other='/html/body/div[8]/div[1]/div/div[2]/text()')
dict['www.hibor.com.cn'] = \
    OriginDict("static",
               "慧博投研资讯",
               '/html/body/div[6]/div[1]/div[2]/div[1]/div/span[2]/text()',
               '/html/body/div[6]/div[1]/div[2]/div[1]/div/span[1]/text()')

# 来源写在正文末尾
# dict['www.jfinfo.com'] = \
#     OriginDict("static",
#                "巨丰财经",
#                '/html/body/div[2]/div[2]/div[1]/div[1]/span[1]/text()',
#                origin=None)

dict['www.mhngx.com'] = \
    OriginDict("static",
               "澳门百家乐",
               '/html/body/div[3]/div/div[1]/div[1]/div[1]/span[1]/text()',
               '/html/body/div[3]/div/div[1]/div[1]/div[1]/span[3]/text()')

dict['www.microbell.com'] = \
    OriginDict("static",
               "慧博投研资讯",
               '/html/body/div[6]/div[1]/div[2]/div[1]/div/span[2]/text()',
               '/html/body/div[6]/div[1]/div[2]/div[1]/div/span[1]/text()')

dict['www.paper.edu.cn'] = \
    OriginDict("static",
               "中国科技论文在线",
               time=None,
               origin=None)

dict['www.shunheweimin.com'] = \
    OriginDict("static",
               "顺和都市在线",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="source_baidu"]/text()')

dict['www.southmoney.com'] = \
    OriginDict("static",
               "南方财富网",
               '/html/body/div[4]/div/div[2]/div/p/text()[1]',
               '/html/body/div[5]/div/div[2]/div/p/text()[2]')
dict['www.xajrxw.com'] = \
    OriginDict("static",
               "西安今日新闻",
               '/html/body/div[6]/div[4]/div[1]/p/span[1]/text()',
               '/html/body/div[6]/div[4]/div[1]/p/span[2]/a/text()')

dict['www.yicai.com'] = \
    OriginDict("static",
               "第一财经",
               '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/h2/span[2]/text()',
               '/html/body/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/h2/i/text()')

dict['www.yiqiniu.com'] = \
    OriginDict("static",
               "一起牛",
               '/html/body/div/div/div/div[1]/div[3]/div/div/div[1]/div[1]/text()',
               '/html/body/div/div/div/div[1]/div[3]/div/div/div[1]/div[2]/text()')

dict['www.yjcf360.com'] = \
    OriginDict("static",
               "赢家财富网",
               ['/html/body/div[7]/div[1]/div[2]/div[1]/div[1]/time/text()','/html/body/div[5]/div[1]/div[2]/div[1]/div[1]/time/text()'],
               ['/html/body/div[7]/div[1]/div[2]/div[1]/div[1]/span[1]/text()','/html/body/div[5]/div[1]/div[2]/div[1]/div[1]/span[1]/text()'])

dict['www.yuncaijing.com'] = \
    OriginDict("static",
               "云财经",
               time=None,
               origin=None)

# dict['www.zdcj.net'] = \
#     OriginDict("static",
#                "正点财经",
#                time=None,
#                origin=None,
#                other='/html/body/div[8]/div[2]/div/div[1]/div/text()')

dict['xinxijishufuwu.juhangye.com'] = \
    OriginDict("static",
               "信息服务行业-聚行业",
               time=None,
               origin=None,
               other='/html/body/div[3]/div[1]/div[2]/div/div[1]/p/text()')

dict['yuanchuang.10jqka.com.cn'] = \
    OriginDict("static",
               "同花顺财经",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="source_baidu"]/text()')

# dict['zqrb.ccstock.cn'] = \
#     OriginDict("static",
#                "证券日报",
#                time=None,
#                origin=None)
#dict['xueqiu.com'] = \
#    OriginDict("static",
#               "雪球",
#               ['//*[@id="status-94182504"]/div[1]/div[1]/div[2]/a/text()','//*[@id="status-94588947"]/div[1]/div[1]/div[2]/a/text()']
#               '//*[@id="status-94182504"]/div[1]/div[1]/div[2]/span/text()')
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
               ['//*[@id="conTit"]/div/span[1]/text()','/html/body/div[2]/div[3]/div/div[2]/span[1]/text()'],
               ['//*[@id="source"]/text()','//*[@id="source"]/text()'])
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
               'gbk',
               ['/html/body/div[14]/div[4]/div[1]/div[3]/p[1]/span[1]/text()','/html/body/div/div[4]/div[1]/div[3]/p[1]/span[1]/text()'],
               ['/html/body/div[14]/div[4]/div[1]/div[3]/p[1]/span[2]/a/text()','/html/body/div/div[4]/div[1]/div[3]/p[1]/span[2]/text()[2]'])
dict['news.hexun.com'] = \
    OriginDict("static",
               "和讯",
               '/html/body/div[4]/div/div[1]/span/text()',
               '/html/body/div[4]/div/div[1]/a/text()')
dict['www.p5w.net'] = \
    OriginDict("static",
               "全景网",
               'GB2312',
               ['/html/body/div[3]/div[1]/div/div[1]/span[1]/time/text()','/html/body/div[4]/div[1]/div/div[1]/span[1]/time/text()'],
               ['/html/body/div[3]/div[1]/div/div[1]/span[1]/i[1]/a/text()','/html/body/div[4]/div[1]/div/div[1]/span[1]/i[1]/a/text()'])
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
               ['//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[4]/text()','//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[3]/text()'],
               ['//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[2]/a/text()','//*[@id="Main-Article-QQ"]/div/div[1]/div[1]/div[1]/div/div[1]/span[2]/a/text()'])
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
###################

#  600093.aniu.tv  无法访问

# finance.ifeng.com
dict['app.finance.ifeng.com'] = \
    OriginDict("static",
               "凤凰网财经",
               '//*[@id="artical_sth"]/p/span[1]/text()',
               '//*[@id="artical_sth"]/p/span[3]/span/text()')

# http://yuanchuang.10jqka.com.cn
dict['basic.10jqka.com.cn'] = \
    OriginDict("static",
               "同花顺财经",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="source_baidu"]/text()')

#  bbs.hcbbs.com  bbs论坛，都是帖子
#  bbs.jrj.com.cn  同上
#  bbs.tianya.cn  继续同上

#  cwzx.shdjt.com  这网站是在自己的页面里开个子窗口打开别的新浪之类的新闻

dict['data.eastmoney.com'] = \
    OriginDict("static",
               "数据中心_东方财富网",
               '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/span[2]/text()',
               '/html/body/div[4]/div/div[3]/div[1]/div/div[2]/span[3]/text()')

#  dspace.imech.ac.cn  这是个研究所的数据库，全是论文
#  fhtc.imr.ac.cn  同上

dict['ent.zdface.com'] = \
    OriginDict("static",
               "Lady FACE 娱乐",
               '//*[@id="mbSourceCard"]/span/text()',
               '//*[@id="ent"]/div[6]/div[1]/div[1]/div[1]/div/span/span[3]/text()')

dict['finance.china.com.cn'] = \
    OriginDict("static",
               "中国财经",
               time=None,
               origin=None,
               other=['/html/body/div[5]/span/text()','/html/body/div[4]/span/text()'])

dict['finance.cjn.cn'] = \
    OriginDict("static",
               "长江财经",
               '//*[@id="main-content"]/div[1]/article/div[1]/span[1]/text()',
               '//*[@id="main-content"]/div[1]/article/div[1]/span[2]/text()')

dict['finance.gucheng.com'] = \
    OriginDict("static",
               "股城网",
               '//*[@id="title"]/aside/time/text()',
               '//*[@id="title"]/aside/em/text()')

dict['finance.huanqiu.com'] = \
    OriginDict("static",
               "环球财经",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="source_baidu"]/a/text()')

dict['ggjd.cnstock.com'] = \
    OriginDict("static",
               "公告解读_中国证券网",
               '//*[@id="pager-content"]/div[1]/span[1]/text()',
               '//*[@id="pager-content"]/div[1]/span[2]/a/text()')

#  guba.hexun.com  这个网站是个人发帖发表看法
#  guba.sina.com.cn  这个是专家发表看法

#  guiyang.huangye88.com  这是个黄页……怎么混进来的……

dict['gupiao.jd.com'] = \
    OriginDict("static",
               "京东股票",
               time=None,
               origin=None,
               other='/html/body/div[5]/div[5]/div/section/div/div[1]/text()')

dict['gupiao.southmoney.com'] = \
    OriginDict("static",
               "南方股票网",
               '//*[@id="articleTime"]/text()',
               '//*[@id="articleSource"]/a/text()')

#  ir.sia.ac.cn  依旧是论文库
#  jue-ce.com  个人发帖网站

dict['kuaixun.stcn.com'] = \
    OriginDict("static",
               "证券时报网",
               time=None,
               origin=None,
               other=['/html/body/div[7]/div[1]/div[2]/div/text()','/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div/text()'])

dict['lights.ofweek.com'] = \
    OriginDict("static",
               "半导体照明网",  # 是的，这真的只是个做半导体的，不知道为什么做的这么正式
               '//*[@id="steven"]/body/div[4]/div[3]/div[1]/div[2]/div[1]/nobr/span/text()',
               '//*[@id="laiyuan"]/span/span/text()')

#  mapp.jrj.com.cn  404 not found ???

dict['stock.10jqka.com.cn'] = \
    OriginDict("static",
               "同花顺财经",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="source_baidu"]/text()')

dict['news.cnstock.com'] = \
    OriginDict("static",
               "中国证券网_新闻",
               '//*[@id="pager-content"]/div[1]/span[1]/text()',
               '//*[@id="pager-content"]/div[1]/span[2]/a/text()')

dict['news.emoney.cn'] = \
    OriginDict("static",
               "益盟操盘手",
               '//*[@id="review"]/div[1]/div[1]/p[1]/span[2]/text()',
               '//*[@id="review"]/div[1]/div[1]/p[1]/span[1]/text()')

dict['news.kuqiw.com'] = \
    OriginDict("static",
               "酷企网",
               '/html/body/div[10]/div[1]/div[1]/div[2]/text()[1]',
               '/html/body/div[10]/div[1]/div[1]/div[2]/a/text()')

dict['news.lianzhou.cn'] = \
    OriginDict("static",
               "连州网",
               '/html/body/div[4]/div[1]/div[2]/div[1]/span[1]/text()',
               '/html/body/div[4]/div[1]/div[2]/div[1]/span[2]/text()')

dict['news.scol.com.cn'] = \
    OriginDict("static",
               "四川在线_新闻中心",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="source_baidu"]/a/text()')

#  news.shdjt.com  也是在自己的页面里开个子窗口打开别的新浪之类的新闻

#  passport.weibo.com  这是新浪微博……

#  q.stock.sohu.com  这个全都没有来源

#  quotes.money.163.com  没找到有新闻的部分

dict['sc.stock.cnfol.com'] = \
    OriginDict("static",
               "中金在线",
               '//*[@id="pubtime_baidu"]/text()',
               '//*[@id="source_baidu"]/span/text()')

#  spirit.tjkx.com  没有来源

dict['sports.hljnews.cn'] = \
    OriginDict("static",
               "黑龙江新闻网",
               '/html/body/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td/span[1]/text()',
               '/html/body/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td/span[2]/text()')

#  stock.cngold.org  打不开
# dict[''] = \
#     OriginDict("static",
#                "",
#                '/text()',
#                '/text()')
