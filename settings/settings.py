#! -*- coding:utf8 -*-
__author__ = 'gpxlcj'

'''
基本信息
'''
#微博登陆信息
USERNAME = 'g@g.com'
PASSWORD = 'gg12345'

#微博API信息
APP_SOURCE = ''
APP_SOURCE_LIST = ['', '']


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
KEY_WORDS = [u'qqq', u'xx']
 
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
]

'''
数据库配置
'''
#mongodb数据库配置
MONGO_DB = {
    'address': 'localhost', #数据库ip
    'port': 27017, #端口号
    'db_name': 'weibodata', #数据库名称
    'collection_name': 'BeijingGeo', #表名称
}