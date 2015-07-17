# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os

import re
import random

import logging
import datetime

from official.weibo_api import get_weibo_by_id, get_weibo_by_ids
#excel读写操作

from save import save_search_data, save_data_by_db
from settings.base import save_catch_page

#配置信息
from settings.settings import START_PAGE, TOTAL_PAGE, START_TIME, END_TIME

logging.basicConfig(level=logging.DEBUG)


#获取关注人姓名(未实现)
def search_follow(session, user_id, num, is_me=0):
    if is_me:
        for i in range(1, 6):
            url = u"http://weibo.com/p/100505"+user_id+"/myfollow?t=1&cfs=&Pl_Official_RelationMyfollow__104_page="+i+"#Pl_Official_RelationMyfollow__104"
            text = session.get(url).text     


#处理搜索页面抓取的数据
def get_p(text):
    content_list = re.findall(r'<p class=\\"comment_txt\\"[\s\S]+?<\\/p>', text)
    if content_list:
        content_len = len(content_list)
        for i in range(0, content_len):
            re_text = re.match(r'<p class[\s\S]+?>', content_list[i])
            re_text = re_text.group()
            temp_len = len(re_text)
            content_list[i] = content_list[i][temp_len:]
            content_list[i] = content_list[i][:-5]
        return content_list
    else:
        print ('log more time')
    return 0


#生成时间
def generate_time():
    time = {
        'start_time': START_TIME, 
        'end_time': END_TIME
    }
    return time 


#抓取存储微博id
def get_id_list(text, session):
    re_id = re.compile("<div mid=[\s\S]+?>")
    origin_id_list = re_id.findall(text)
    re_id = re.compile("mid=\\\\\"[0-9]+\\\\\"")
    id_list = list()
    for i in origin_id_list:
        temp = re_id.search(i)
        if temp:
            temp = temp.group()
            temp = temp[6:len(temp)-2]
            id_list.append(temp)
        else:
            print("None")
    time = str(datetime.datetime.now()).upper()
    print(time+'\n'+'ID_LIST Here')
    print(id_list)
    return id_list


#判断是否超过页码
def out_page(text):
    r_page = re.compile(u'feed_list_page_morelist'+'[\s\S]+'+u'page next S_txt1 S_line1?')
    temp = r_page.search(text)
    if temp:
        return True
    else:
        return False


#搜索信息
def search_info(session, keyword="", start_time="", end_time="",  num=1, location=0):
    content_text = str()
    id_text = str()
    haslink = str()
    if location != 0:
        haslink = "&haslink=1"
    for i in range(START_PAGE, START_PAGE+TOTAL_PAGE):
        url = 'http://s.weibo.com/weibo/'+keyword+'&scope=ori'+haslink+'&timescope=custom:'+start_time+':'+end_time+'&page='+str(i)+'&rd=newTips'
        sleep_time = random.randint(10, 30)
        os_sleep = 'sleep '+str(sleep_time)
        os.system(os_sleep)
        get_text = session.get(url).text
        get_text = u'' + get_text
        get_text = get_text.encode('utf-8')
        content_text = save_catch_page(get_text)
        pd = out_page(content_text)
        if not pd:
            return num
        num = get_page_info(content_text, session, location, num)
    return num


#搜索信息通过id
def search_info_by_id(session, keyword="", start_time="", end_time="",  num=1, location=0):
    content_text = str()
    id_text = str()
    haslink = str()
    if location != 0:
        haslink = "&haslink=1"
    for i in range(START_PAGE, START_PAGE+TOTAL_PAGE):
        url = 'http://s.weibo.com/weibo/'+keyword+'&scope=ori'+haslink+'&timescope=custom:'+start_time+':'+end_time+'&page='+str(i)+'&rd=newTips'
        sleep_time = random.randint(10, 30)
        os_sleep = 'sleep '+str(sleep_time)
        os.system(os_sleep)
        get_text = session.get(url).text
        get_text = u'' + get_text
        get_text = get_text.encode('utf-8')
        content_text = save_catch_page(get_text)
        pd = out_page(content_text)
        if not pd:
            return num
        id_list = get_id_list(content_text, session)
        info_list = get_weibo_by_ids(id_list, session)
        status = save_data_by_db(info_list)
        print(status)
    return num



#直接抓取html页面数据
def get_page_info(text, session, location, num):
    get_list = get_p(text)
    if get_list == 0:
        pass
    else:
        num = save_search_data(get_list, session, location, num)
    return num
