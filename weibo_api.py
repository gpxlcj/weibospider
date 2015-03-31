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



#短链接转换为长链接取坐标
def short_to_long(url, session, app_num=0):
    if u't.cn' in url:
        try:
            temp_s = session.get('http://api.weibo.com/2/short_url/expand.json?url_short='+url+'&source='+APP_SOURCE_LIST[app_num])
        except:
            app_num += 1
            if app_num >= len(APP_SOURCE_LIST):
                app_num = 0
            temp_s = session.get('http://api.weibo.com/2/short_url/expand.json?url_short='+url+'&source='+APP_SOURCE_LIST[app_num])
    else:
        return None
    text = temp_s.text
    print (text)
    text_list = json.loads(text)
    text = text_list['urls'][0][u'url_long'][25:]
    coordinate = text.split('_')
    if len(coordinate) == 2:
        return coordinate
    else:
        return None

