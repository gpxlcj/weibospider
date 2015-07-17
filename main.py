# -*- coding: utf-8 -*-

import json

from user.login import get_session, wblogin
from settings.settings import USERNAME, PASSWORD, START_NUM, KEY_WORDS, DAY_NUM, QUERY_COORDINATE_LIST
from spider import search_info, search_info_by_id
from settings.base import init_xls, init_env, convert_time
from official.weibo_api import get_weibo_by_coordinate
from save import save_data_by_db



if __name__ == '__main__':
    init_env()
    print(json.dumps(wblogin(USERNAME, PASSWORD), ensure_ascii=False))

    num = START_NUM
    init_xls()
    session = get_session()
#根据关键词搜索
#    for i in KEY_WORDS:
#        for j in range(0, 3):
#            start_time = '2015-5-'+str(3*j+1)
#            end_time = '2015-5-'+str(3*j+3)
#            num = search_info_by_id(session, KEY_WORDS[0], start_time, end_time, num, 0)
    for y in range(2015, 2016):
        for m in range(1, 2):
            for d in range(1, DAY_NUM[m]):
                for p in range(1, 21):
                    starttime = convert_time(str(y), str(m), str(d), '0')
                    print('starttime')
                    print(starttime)
                    endtime = float(starttime)+3600*24
                    starttime = str(starttime)
                    starttime = starttime[:-2]
                    info_list = get_weibo_by_coordinate(session, QUERY_COORDINATE_LIST[0],
                                            starttime, endtime, 2000, 0, 20, p, 0)
                    save_data_by_db(info_list)
