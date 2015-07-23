# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import json

#配置文件
from settings.settings import APP_SOURCE_LIST, APP_SOURCE
from lib.log import lg_debug, lg_warning, lg_info, init_log
init_log()

#判断请求是否超出限制
def request_limit(url, session, app_num):
    temp_s = session.get('http://api.weibo.com/2/short_url/expand.json?url_short='+url+'&source='+APP_SOURCE_LIST[app_num])
    text = temp_s.text
    lg_debug(text)
    text_list = json.loads(text)
    if text_list.has_key('error'):
        lg_warning('error, out of request limit ERROR')
        return 0 
    else:
        return text_list


#短链接转换为长链接取坐标
def short_to_long(url, session, app_num=0):
    if u't.cn' in url:
        temp = 0 
        while (temp == 0):
            temp = request_limit(url, session, app_num)
            if temp == 0:
                pass
            else:
                text_list = temp
                break
            app_num += 1
            if app_num >= len(APP_SOURCE_LIST):
                lg_debug('all of the id out limited')
                return None
    else:
        return None
    text = text_list['urls'][0][u'url_long'][25:]
    coordinate = text.split('_')
    if len(coordinate) == 2:
        return coordinate
    else:
        return None


#根据微博id获取微博详细信息
def get_weibo_by_id(m_id, session):
    url = "http://api.weibo.com/2/statuses/show.json?source="+APP_SOURCE+"&id="+m_id
    text = session.get(url)
    text_dict = None
    try:
        text_dict = text.json()
    except Exception:
        lg_warning(Exception.message)
        lg_debug("get_weibo_by_id: No Json")
    return text_dict


#根据微博id批量获取微博详细信息
def get_weibo_by_ids(m_ids, session):
    id_str = str()
    for i in m_ids:
        id_str += i+","
    id_str = id_str[:-1]
    url = "http://api.weibo.com/2/statuses/show_batch.json?source="+APP_SOURCE+"&ids="+id_str
    text = session.get(url)
    text_dict = None
    text_list_dict = None
    try:
        text_dict = text.json()
        text_list_dict = text_dict['statuses']
        lg_debug('success catch the info_list')
    except Exception:
        lg_warning(Exception.message)
        lg_debug("get_weibo_by_ids: No Json")
    return text_list_dict


#根据地理坐标进行批量获取微博
def get_weibo_by_coordinate(session, coordinate, starttime, endtime, range=2000, sort=0, count=20, page=1, offset=0):
    url = "http://api.weibo.com/2/place/nearby_timeline.json?"
    url += "source="+APP_SOURCE
    url += "&lat="+coordinate['latitude']+"&long="+coordinate['longitude']
    url += "&starttime="+str(starttime)+"&range="+str(range)+"&sort="+str(sort)
    url += "&count="+str(count)+"&page="+str(page)+"&offset="+str(offset)
    text = session.get(url)
    text_dict = None
    text_list_dict = None
    try:
        text_dict = text.json()
        if text_dict.has_key('statuses'):
            text_list_dict = text_dict['statuses']
            lg_debug('success catch the info_list')
        else:
            lg_debug("get_weibo_by_coordinate: No Json")
    except Exception:
        lg_warning(Exception.message)
        lg_debug("get_weibo_by_coordinate: No Json")
    return text_list_dict