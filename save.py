# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import os
import sys
import random

import re
import json
import base64
import binascii

import rsa
import requests

import logging

from weibo_api import short_to_long

#excel读写操作
from openpyxl import Workbook, load_workbook
from openpyxl.writer.excel import ExcelWriter

from settings import SAVE_FILE_NAME, APP_SOURCE, SHEET_NAME

#存储搜索结果
def save_search_data(get_list, session, location=0, num=0):
# location: 是否要获取目标地址,1获取，0不获取
    wb = load_workbook(SAVE_FILE_NAME)
    ew = ExcelWriter(wb)
    ws = wb.get_sheet_by_name(SHEET_NAME)
    for i in get_list:
        i = i.encode('utf-8')
        i = i+u''
        if location==0:
            coordinate = None
        else:
            coordinate = get_location(i, session)
        temp_replace = re.compile('<[\s\S]+?>')
        i = temp_replace.sub(' ', i)
        i = i + u'\n'
        i = i.decode('string-escape').encode('gbk')
        i = unicode(i, 'unicode-escape')
        i = i.encode('utf-8')
        if coordinate:
            num = num + 1
            longitude = coordinate[0]
            latitude = coordinate[1]
            ws.cell(row=num+1, column=2).value = longitude
            ws.cell(row=num+1, column=3).value = latitude
            ws.cell(row=num+1, column=1).value = i        
        elif num==0:
            num = num + 1
            ws.cell(row=num+1, column=1).value = i
    ew.save(SAVE_FILE_NAME)
    print (num)
    return num
    

def get_location(get_text, session):
    location_re = re.compile(u'''<a class=[\S\s]+?icon_cd_place[\S\s]+?a>''')
    temp_l = location_re.search(get_text)
    if temp_l:
        origin_url = temp_l.group()
        location_re = re.compile(u'''http:.+? ''')
        url = location_re.search(origin_url).group()[:-2]
        url = url.replace('\\', '')
        print (url+'\n')
        coordinate = short_to_long(url, session, random.randint(0, 5))#顺序为经度、纬度 
        return coordinate 
    else:
        return None

if __name__ == '__main__':
    save_search_data()

