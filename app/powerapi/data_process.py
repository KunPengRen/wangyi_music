# -*- coding:utf8 -*-
import json
"""
数据处理模块
"""


def example_print_user_and_content(msg_list):
    """
    一个输出用户名和对应评论信息的例子
    :param msg_list: 完整信息
    :return:
    """
    i=0
    for msg in msg_list:
        msg_dict = json.loads(msg)
        comments = msg_dict["comments"]
        for comment in comments:
            user_msg = comment["user"]
            nickname = user_msg["nickname"]
            user_id = user_msg["userId"]
            content = comment["content"]
            time = comment["time"]
            print("%s : %s : %s" % (nickname, content,user_id))
            i+=1
    
    print i
            
