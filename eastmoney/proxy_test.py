import urllib
import urllib.request
import random

# 定义一个代理开关
proxySwitch = True

proxy_list = [
    {"http": "10.100.254.229:3128"}
]
header_list = [
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3676.400 QQBrowser/10.4.3469.400"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"}
]
# url = "http://www.baidu.com/"
# url = 'http://quote.eastmoney.com/stock_list.html'

url = 'http://f10.eastmoney.com/f10_v2/CompanySurvey.aspx?code=sh600000'
# 随机选择一个代理IP和User-Agent
proxy = random.choice(proxy_list)
headers = random.choice(header_list)
# 构建两个handler，一个使用代理IP 一个不使用代理IP
httpproxy_handler = urllib.request.ProxyHandler(proxy)
nullproxy_handler = urllib.request.ProxyHandler({})

if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

request = urllib.request.Request(url, headers=headers)
response = opener.open(request)
print(response.read())
