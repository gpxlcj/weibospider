# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import re
import random
import logging
import datetime

from official.weibo_api import get_weibo_by_ids
#excel读写操作

from save import save_search_data, save_data_by_db
from lib.base import save_catch_page
from lib.log import lg_debug, lg_info, lg_warning

#配置信息
from settings.settings import START_PAGE, TOTAL_PAGE, START_TIME, END_TIME
from settings.settings import INTER_LAT, INTER_LON, DISTANCE, QUERY_COORDINATE_LIST

from lib.lib_func import wait_time, convert_time
from official.weibo_api import get_weibo_by_coordinate


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
        lg_debug('log more time')
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
            lg_warning('not match  weibo id')
    time = str(datetime.datetime.now()).upper()
    lg_debug(time+'\n'+'ID_LIST Here')
    lg_info('get_id_list: ' + str(id_list))
    return id_list


#判断是否超过页码
def out_page(text):
    r_page = re.compile(u'feed_list_page_morelist'+'[\s\S]+'+u'page next S_txt1 S_line1?')
    temp = r_page.search(text)
    if temp:
        return True
    else:
        lg_info('out_page: out of page limit')
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
        wait_time(sleep_time)
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
        lg_info(status)
    return num


#直接抓取html页面数据
def get_page_info(text, session, location, num):
    get_list = get_p(text)
    if get_list == 0:
        pass
    else:
        num = save_search_data(get_list, session, location, num)
    lg_info('record number: ' + str(num))
    return num

'''
------------------------------------
获取历史数据
------------------------------------
'''


#构建四叉树
def fourtree(session, coordinate, starttime, geo_range, inter_lat, inter_lon):
    temp_time = random.randint(2, 5)
    wait_time(temp_time)
    info_list = get_weibo_by_coordinate(session, coordinate, starttime, 0, geo_range, 0, 50, 20, 0)
    if info_list:
        print (geo_range)
        save_data_by_db(info_list)
    else:
        print (0)
    if info_list:
        inter_lat = round(inter_lat/2, 6)
        inter_lon = round(inter_lon/2, 6)
        coordinate1 = dict()
        coordinate2 = dict()
        coordinate3 = dict()
        coordinate4 = dict()
        geo_range = float(geo_range)
        geo_range = int(round(geo_range/2*1.3))
        if geo_range < 100:
            geo_range = 100
        coordinate1['latitude'] = str(round(float(coordinate['latitude']) + inter_lat, 6))
        coordinate1['longitude'] = str(round(float(coordinate['longitude']) + inter_lat, 6))
        coordinate2['latitude'] = str(round(float(coordinate['latitude']) - inter_lon, 6))
        coordinate2['longitude'] = str(round(float(coordinate['longitude']) + inter_lon, 6))
        coordinate3['latitude'] = str(round(float(coordinate['latitude']) + inter_lat, 6))
        coordinate3['longitude'] = str(round(float(coordinate['longitude']) - inter_lat, 6))
        coordinate4['latitude'] = str(round(float(coordinate['latitude']) - inter_lon, 6))
        coordinate4['longitude'] = str(round(float(coordinate['longitude']) - inter_lon, 6))
        l1 = fourtree(session, coordinate1, starttime, geo_range, inter_lat, inter_lon)
        l2 = fourtree(session, coordinate2, starttime, geo_range, inter_lat, inter_lon)
        l3 = fourtree(session, coordinate3, starttime, geo_range, inter_lat, inter_lon)
        l4 = fourtree(session, coordinate4, starttime, geo_range, inter_lat, inter_lon)
        l5 = [{'coordinate': coordinate, 'geo_range': geo_range}]
        return l1+l2+l3+l4 +l5
    else:
        return [{'coordinate': coordinate, 'geo_range': geo_range}]


#获取历史数据
def get_info_history(session):
    geo_num = 63
    starttime = convert_time('2015', '1', '1', '0')
    starttime = str(starttime)
    starttime = starttime[:-2]
    page_count = 50
    endtime = starttime
    sort = 0
    offset = 0
    inter_lat = INTER_LAT
    inter_lon = INTER_LON
    for p_id in range(0, geo_num):
        geo_range = DISTANCE
        p = 1
        index = [0]*50
        view_list = fourtree(session, QUERY_COORDINATE_LIST[p_id], starttime, geo_range, inter_lat, inter_lon)
        for view in view_list:
            p = 1
            while p < 20:
                coordinate = view['coordinate']
                geo_range = view['geo_range']
                temp_time = random.randint(10, 15)
                wait_time(temp_time)
                info_list = get_weibo_by_coordinate(session, coordinate, starttime, endtime, geo_range, 0, page_count, p, 0)
                if info_list:
                    pd = save_data_by_db(info_list)
                    if not pd:
                        break
                    p += 1
                else:
                    break
        sleep_time = random.randint(10, 20)
        wait_time(sleep_time)





