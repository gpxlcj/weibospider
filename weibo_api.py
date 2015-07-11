# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys

import re
import json
import base64
import binascii

import rsa
import requests

import logging

#配置文件
from settings import APP_SOURCE, APP_SOURCE_LIST,SAVE_FILE_NAME

#判断请求是否超出限制
def request_limit(url, session, app_num):
    temp_s = session.get('http://api.weibo.com/2/short_url/expand.json?url_short='+url+'&source='+APP_SOURCE_LIST[app_num])
    text = temp_s.text
    print (text)
    text_list = json.loads(text)
    if text_list.has_key('error'):
        return 0
    else:
        return text_list

#短链接转换为长链接取坐标
def short_to_long(url, session, app_num=0):
    if u't.cn' in url:
        temp = 0
        while(temp == 0):
            temp = request_limit(url, session, app_num)
            if temp == 0:
                pass
            else:
                text_list = temp
                break
            app_num += 1
            if app_num >= len(APP_SOURCE_LIST):
                print ('all of the id out limited')
                return None
    else:
        return None
    text = text_list['urls'][0][u'url_long'][25:]
    coordinate = text.split('_')
    if len(coordinate) == 2:
        return coordinate
    else:
        return None
