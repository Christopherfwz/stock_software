import urllib2
import re


# here sh_a stands for huA, sz_a stands for shenA
# number stands for the request number of the stock
def crawlSina(stock_type='sz_a', number=str(100)):
    url_all = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page=1&num=' + number + '&sort=changepercent&asc=0&node=' + stock_type + '&symbol='
    req = urllib2.Request(url_all)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0')
    html = urllib2.urlopen(req).read().decode('gbk')

    pattern = 'symbol:.+?buy:'
    all_stock = re.compile(pattern).findall(html)

    result = []
    pattern1 = 'percent:".+?"'
    pattern2 = 'code:".+?"'

    if stock_type == 'sz_a':
        precode = 'sz'
    elif stock_type == 'sh_a':
        precode = 'sh'
    else:
        precode = ''

    for stock in all_stock:
        change = re.compile(pattern1).findall(stock)
        changeNum = float(change[0][9:-1])
        if (changeNum > 9.5) and (changeNum < 11.0):
            temp_code = re.compile(pattern2).findall(stock)
            code = temp_code[0][6:-1]
            result.append(precode+code)

    return result


# stock_type = raw_input('input the stock type: ')
# number = raw_input('input the number: ')
# print(crawl(stock_type, number))
