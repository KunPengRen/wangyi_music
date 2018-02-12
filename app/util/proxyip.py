# -*- coding:utf8 -*-

import requests
import re
import time

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Hosts': 'hm.baidu.com',
    'Referer': 'http://www.xicidaili.com/nn',
    'Connection': 'keep-alive'
}
iplist = list()
# getip
for i in range(1,30):

    url = 'http://www.xicidaili.com/nn/' + str(i)
    
    req = requests.get(url=url,headers=headers)

    # 提取ip和端口
    ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})[\s\S]*?<td>(HTTP|HTTPS)</td>",req.text)
    # 将提取的ip和端口写入文件
    f = open("ip.txt","a+")
    for li in ip_list:
        ip = li[2]+'://'+li[0] + ':' + li[1] + '\n'
        checkip(ip,f)
    time.sleep(2)       # 每爬取一页暂停两秒

def checkip(ip,f):
    url = "http://ip.chinaz.com/getip.aspx"
    if ip.find("HTTPS"):
        proxy = {"HTTPS":ip}
    else:
        proxy = {"HTTP":ip}
    try:
        res = requests.get(url=url,proxies=proxy)
        print 'valid_ip: ' + ip
        f.write(ip)
    except Exception,e:
        print proxy
        print e
        continue
    