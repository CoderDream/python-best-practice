#导入需要使用到的模块
import urllib
import re
import pandas as pd
import pymysql
import os


class ConnectTestUtil:
    #爬虫抓取网页函数
    def getHtml(url):
        html = urllib.request.urlopen(url).read()
        html = html.decode('gbk')
        return html

    #抓取网页股票代码函数
    def getStackCode(html):
        s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
        pat = re.compile(s)
        code = pat.findall(html)
        return code


if __name__ == '__main__':
    connect_test_util = ConnectTestUtil()
    test_url = 'http://quote.eastmoney.com/stocklist.html'
    connect_test_util.getHtml(test_url)
