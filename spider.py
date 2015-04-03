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

#excel读写操作
from openpyxl import Workbook, load_workbook

from save import save_search_data

#配置信息
from settings import START_PAGE, USERNAME, PASSWORD, START_NUM, TOTAL_PAGE, APP_SOURCE, SAVE_FILE_NAME, SHEET_NAME, KEY_WORDS

logging.basicConfig(level=logging.DEBUG)


#处理抓取的数据
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


#存储抓取的页面信息
def save_catch_page(get_text):
    file_a = open('page_1', 'wb')
    get_text = u'' + get_text
    file_a.write(get_text)
    file_a.close()
    return get_text
    

#初始化excel表格
def init_xls():
    wb = Workbook()
    ws = wb.get_active_sheet()
    ws.cell(row=1, column=1).value = u'描述'
    ws.cell(row=1, column=2).value = u'经度'
    ws.cell(row=1, column=3).value = u'纬度'
    ws.title = SHEET_NAME
    wb.save(SAVE_FILE_NAME)


#搜索信息
def search_info(session, keyword="", start_time="", end_time="",  num=1, location=0):
    for i in range(START_PAGE, START_PAGE+TOTAL_PAGE):
        os.system('sleep 10')
        get_text = session.get('http://s.weibo.com/wb/'+keyword+'&xsort=time&scope=ori&haslink=1&page='+str(i)).text
        get_text = u'' + get_text
        get_text = get_text.encode('utf-8')
        get_text = save_catch_page(get_text)
         
        get_list = get_p(get_text)
        if get_list == 0:
            pass
        else:
            num = save_search_data(get_list, session, location, num)
    return num
    


