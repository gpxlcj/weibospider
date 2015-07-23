#! -*- coding:utf-8 -*-
__author__ = 'gpxlcj'

import time
import os


#转换时间
def convert_time(year, month, day, hour=0):
    time_str = year+'-'+month+'-'+day+' '+hour+':'+'00:00'
    time_format = "%Y-%m-%d %H:%M:%S"
    form_time = time.strptime(time_str, time_format)
    time_stamp = str(time.mktime(form_time))
    return time_stamp


#短时间暂停运行
def wait_time(sleep_time):
    os_sleep = 'sleep '+str(sleep_time)
    os.system(os_sleep)
    return True

def arbitrary_precision_compare(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        return 1
    elif length2 < length1:
        return 2
    else:
        for i in range(0, length1):
            if str1[i] > str2[i]:
                return 1
            elif str1[i] < str2[i]:
                return 2
            else:
                pass
    return 0

