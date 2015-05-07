# -*- coding: utf-8 -*-

import os
import sys
import json

from login import get_session, wblogin
from settings import START_PAGE, USERNAME, PASSWORD, START_NUM, TOTAL_PAGE, APP_SOURCE, SAVE_FILE_NAME, SHEET_NAME, KEY_WORDS
from spider import search_info, search_follow
from base import init_xls


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    print(json.dumps(wblogin(USERNAME, PASSWORD), ensure_ascii=False))
    num = 1 #信息开始记录的行数
    init_xls(1)
    id_list = search_follow(get_session(), '', num, 1)
    for i in id_list:
        search_follow(get_session(), i, num, 0)
#-----------------------------------
    
#-----------------------------------
#    num = START_NUM
#    init_xls()
#    for i in KEY_WORDS:
#        for j in range(2, 10):
#            start_time = '2015-3-'+str(3*j+1)
#            end_time = '2015-3-'+str(3*j+3)
#            num = search_info(get_session(), KEY_WORDS[12], start_time, end_time, num, 1) 
#-----------------------------------
