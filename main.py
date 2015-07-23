# -*- coding: utf-8 -*-

import json
import random
from datetime import datetime

from user.login import get_session, wblogin
from settings.settings import USERNAME, PASSWORD, START_NUM, QUERY_COORDINATE_LIST
from lib.base import init_xls, init_env
from lib.log import lg_debug, lg_info, lg_warning, init_log
from lib.lib_func import convert_time, wait_time, arbitrary_precision_compare
from official.weibo_api import get_weibo_by_coordinate
from save import save_data_by_db


if __name__ == '__main__':
    init_env()
    lg_info(json.dumps(wblogin(USERNAME, PASSWORD), ensure_ascii=False))
    init_log()
    num = START_NUM
    init_xls()
    session = get_session()
#根据关键词搜索
#    for i in KEY_WORDS:
#        for j in range(0, 3):
#            start_time = '2015-5-'+str(3*j+1)
#            end_time = '2015-5-'+str(3*j+3)
#            num = search_info_by_id(session, KEY_WORDS[0], start_time, end_time, num, 0)

#按时间来计算
#    for y in range(2015, 2016):
#        for m in range(1, 2):
#            for d in range(1, DAY_NUM[m]):
#                for p in range(1, 21):
#                    starttime = convert_time(str(y), str(m), str(d), '0')
#                    print('starttime')
#                    print(starttime)
#                    endtime = float(starttime)+3600*24
#                    starttime = str(starttime)
#                    starttime = starttime[:-2]
#                    info_list = get_weibo_by_coordinate(session, QUERY_COORDINATE_LIST[0],
#                                            starttime, endtime, 2000, 0, 20, p, 0)
#                    save_data_by_db(info_list)

#按照地点遍历
    count_time = datetime(2015, 7, 21, 18, 20)
    geo_num = 63
    page_count = 50
    geo_range = 10000
    index_num = ['0'] * geo_num
    while datetime.now() < count_time:

        for p_id in range(0, geo_num):
            p = 1
            starttime = convert_time('2015', '7', '1', '0')
            endtime = starttime
            starttime = str(starttime)
            starttime = starttime[:-2]
            info_list = get_weibo_by_coordinate(session, QUERY_COORDINATE_LIST[p_id],
                                    starttime, endtime, geo_range, 0, page_count, p, 0)
            save_data_by_db(info_list)
            if not info_list:
                continue
            else:
                pass
            length = len(info_list)
            cmpstr1 = info_list[length-1]['mid']
            cmpstr2 = index_num[p_id]
            index_num[p_id] = info_list[0]['mid']
            while arbitrary_precision_compare(cmpstr1, cmpstr2) == 1:
                p += 1
                info_list = get_weibo_by_coordinate(session, QUERY_COORDINATE_LIST[p_id],
                                        starttime, endtime, geo_range, 0, page_count, p, 0)
                save_data_by_db(info_list)
                if not info_list:
                    break
                else:
                    pass
                length = len(info_list)
                cmpstr1 = info_list[length-1]['mid']
                if p >= 20:
                    break
        sleep_time = random.randint(10, 20)
        wait_time(sleep_time)