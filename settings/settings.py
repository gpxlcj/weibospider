#! -*- coding:utf8 -*-
__author__ = 'gpxlcj'

'''
基本信息
'''
#微博登陆信息
USERNAME = 'gpxlcj@126.com'
PASSWORD = 'gg1993'

#微博API信息
APP_SOURCE = '211160679'
APP_SOURCE_LIST = ['3761458781', '3138778654', '1659882303', '2178679309', '1379235969', '1762645262', '1636267192']


#每个月的时间
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY_NUM = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

'''
搜索页面爬虫配置
'''
#开始序号
START_NUM = 1 

#总访问页数
TOTAL_PAGE = 49 
START_PAGE = 1 

#文件信息
SAVE_FILE_NAME = u'weibo_iesous.xlsx'
SHEET_NAME = u'iesous'

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


'''
根据地理位置爬取配置
'''
#搜索的地理位置中心
QUERY_COORDINATE_LIST = [
    {'latitude': '39.591093', 'longitude': '116.043093', 'num': '1'},
    {'latitude': '39.591093', 'longitude': '116.185277', 'num': '2'},
    {'latitude': '39.591093', 'longitude': '116.327463', 'num': '3'},
    {'latitude': '39.591093', 'longitude': '116.469647', 'num': '4'},
    {'latitude': '39.591093', 'longitude': '116.611833', 'num': '5'},
    {'latitude': '39.591093', 'longitude': '116.754018', 'num': '6'},
    {'latitude': '39.591093', 'longitude': '116.896203', 'num': '7'},
    {'latitude': '39.591093', 'longitude': '116.038388', 'num': '8'},
    {'latitude': '39.591093', 'longitude': '116.180573', 'num': '9'},
    {'latitude': '39.733277', 'longitude': '116.043093', 'num': '10'},
    {'latitude': '39.733277', 'longitude': '116.185277', 'num': '11'},
    {'latitude': '39.733277', 'longitude': '116.327463', 'num': '12'},
    {'latitude': '39.733277', 'longitude': '116.469647', 'num': '13'},
    {'latitude': '39.733277', 'longitude': '116.611833', 'num': '14'},
    {'latitude': '39.733277', 'longitude': '116.754018', 'num': '15'},
    {'latitude': '39.733277', 'longitude': '116.896203', 'num': '16'},
    {'latitude': '39.733277', 'longitude': '116.038388', 'num': '17'},
    {'latitude': '39.733277', 'longitude': '116.180573', 'num': '18'},
    {'latitude': '39.875462', 'longitude': '116.043093', 'num': '19'},
    {'latitude': '39.875462', 'longitude': '116.185277', 'num': '20'},
    {'latitude': '39.875462', 'longitude': '116.327463', 'num': '21'},
    {'latitude': '39.875462', 'longitude': '116.469647', 'num': '22'},
    {'latitude': '39.875462', 'longitude': '116.611833', 'num': '23'},
    {'latitude': '39.875462', 'longitude': '116.754018', 'num': '24'},
    {'latitude': '39.875462', 'longitude': '116.896203', 'num': '25'},
    {'latitude': '39.875462', 'longitude': '116.038388', 'num': '26'},
    {'latitude': '39.875462', 'longitude': '116.180573', 'num': '27'},
    {'latitude': '40.017647', 'longitude': '116.043093', 'num': '28'},
    {'latitude': '40.017647', 'longitude': '116.185277', 'num': '29'},
    {'latitude': '40.017647', 'longitude': '116.327463', 'num': '30'},
    {'latitude': '40.017647', 'longitude': '116.469647', 'num': '31'},
    {'latitude': '40.017647', 'longitude': '116.611833', 'num': '32'},
    {'latitude': '40.017647', 'longitude': '116.754018', 'num': '33'},
    {'latitude': '40.017647', 'longitude': '116.896203', 'num': '34'},
    {'latitude': '40.017647', 'longitude': '116.038388', 'num': '35'},
    {'latitude': '40.017647', 'longitude': '116.180573', 'num': '36'},
    {'latitude': '40.159833', 'longitude': '116.043093', 'num': '37'},
    {'latitude': '40.159833', 'longitude': '116.185277', 'num': '38'},
    {'latitude': '40.159833', 'longitude': '116.327463', 'num': '39'},
    {'latitude': '40.159833', 'longitude': '116.469647', 'num': '40'},
    {'latitude': '40.159833', 'longitude': '116.611833', 'num': '41'},
    {'latitude': '40.159833', 'longitude': '116.754018', 'num': '42'},
    {'latitude': '40.159833', 'longitude': '116.896203', 'num': '43'},
    {'latitude': '40.159833', 'longitude': '117.038388', 'num': '44'},
    {'latitude': '40.159833', 'longitude': '117.180573', 'num': '45'},
    {'latitude': '40.302018', 'longitude': '116.043093', 'num': '46'},
    {'latitude': '40.302018', 'longitude': '116.185277', 'num': '47'},
    {'latitude': '40.302018', 'longitude': '116.327463', 'num': '48'},
    {'latitude': '40.302018', 'longitude': '116.469647', 'num': '49'},
    {'latitude': '40.302018', 'longitude': '116.611833', 'num': '50'},
    {'latitude': '40.302018', 'longitude': '116.754018', 'num': '51'},
    {'latitude': '40.302018', 'longitude': '116.896203', 'num': '52'},
    {'latitude': '40.302018', 'longitude': '117.038388', 'num': '53'},
    {'latitude': '40.302018', 'longitude': '117.180573', 'num': '54'},
    {'latitude': '40.302018', 'longitude': '116.043093', 'num': '55'},
    {'latitude': '40.302018', 'longitude': '116.185277', 'num': '56'},
    {'latitude': '40.302018', 'longitude': '116.327463', 'num': '57'},
    {'latitude': '40.302018', 'longitude': '116.469647', 'num': '58'},
    {'latitude': '40.302018', 'longitude': '116.611833', 'num': '59'},
    {'latitude': '40.302018', 'longitude': '116.754018', 'num': '60'},
    {'latitude': '40.444202', 'longitude': '116.896203', 'num': '61'},
    {'latitude': '40.444202', 'longitude': '117.038388', 'num': '62'},
    {'latitude': '40.444202', 'longitude': '117.180573', 'num': '63'},
]

'''
数据库配置
'''
#mongodb数据库配置
MONGO_DB = {
    'address': 'localhost',
    'port': 27017,
    'db_name': 'weibodata',
    'collection_name': 'BeijingGeo',
}
MONGO_CLIENT_ADDR = 'localhost'
MONGO_CLIENT_PORT = 27017
