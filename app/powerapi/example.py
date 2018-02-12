# -*- coding:utf-8 -*-
"""
author: power
pub_time: 2018/02/05
"""

from code import *
from settings import *
from data_process import *
from musiclist import *

iplist = list()
result = list()
with open('./ip.txt') as f :
    for line in f.readlines():
        iplist.append(line.strip())
        

if __name__ == "__main__":
    # 音乐的id
    #music_id = '28234970'
    #print music_list
    #print iplist
    #music_list = ['29567189']
    i = 1
    for music_id in music_list:
        i+=1
        url = base_url % music_id
        print 'now url is----'+ music_id
        pgnum = int(get_comments_pgnum(url,iplist))/20
        # 得到第一页到第五页的评论内容
        msgs = get_comments(url, iplist,from_page=1, to_page=pgnum)
        with open('./zjy.txt','w') as f :
            for msg in msgs:
                f.write(msg)

        print '----The music %s is finisth now is the %d music' %(music_id,i)