#! -*- coding:utf8 -*-
#开始序号
START_NUM = 1 

#总访问页数
TOTAL_PAGE = 49 
START_PAGE = 1 

#文件信息
SAVE_FILE_NAME = u'weibo_iesous.xlsx'
SHEET_NAME = u'iesous'

#微博登陆信息
USERNAME = 'gpxlcj@126.com'
PASSWORD = 'gg1993'

#微博API信息
APP_SOURCE = '211160679'
APP_SOURCE_LIST = ['3761458781', '3138778654', '1659882303', '2178679309', '1379235969', '1762645262', '1636267192']

#搜索关键词
KEY_WORDS = [u'耶稣 感谢', u'耶稣 生活', u'耶稣 阿门', u'耶稣 主教', u'耶稣 上帝',]
 
#搜索时间
START_YEAR = '2015'
START_MONTH = '3'
START_DAY = '1'
START_HOUR = '0'
START_TIME = START_YEAR + '-' + START_MONTH + '-' + START_DAY + '-' + START_HOUR

END_YEAR = '2015'
END_MONTH = '3'
END_DAY = '31'
END_HOUR = '23'
END_TIME = END_YEAR + '-' + END_MONTH + '-' + END_DAY + '-' + END_HOUR

#搜索时间间隔
INTER_DAY = 3
INTER_HOUR = 0

#搜索的地理位置中心
QUERY_COORDINATE_LIST = [
    {'latitude': '39.978364', 'longitude': '116.4840343'},
]

#每个月的时间
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY_NUM = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#mongodb数据库配置
MONGO_CLIENT_ADDR = 'localhost'
MONGO_CLIENT_PORT = 27017
