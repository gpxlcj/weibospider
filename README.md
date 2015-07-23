微博爬虫 WeiboSpider
==
**Author:** [gpxlcj][1]  
**Update time:**2015.05.07

Description
----------

A spider to catch the microblog data from [weibo][2].  
The data can be crawled by time, keywords and so on.the data field can be customed to catch.
中文详细信息 [WeiboSpider wiki][4]
Detail info in English [WeiboSpider wiki][5]
**The summarize of each scripts:**

`main.py`         start script  
`settings.py`     the configure file  
`weibo_api.py`    get info via weibo api  
`save.py`         save data  
`login.py`        account login  
`base.py`         base function  
`spider.py`       catch weibo data  
`convert_shp.py`  convert to shp data  

ENVIRONMENT
--
- Python 2.7.6  
- rsa 3.1.4  
- requests 2.5.3  
- openpyxl 2.2.0  
- pyshp 1.2.1  
 

EXAMPLE
--
You can custom the `main.py` to design your spider. Get the information from [Introduction][3]

```python
#! -*- coding:utf-8 -*-
from login import wblogin
from base import init_env
import json

if __name__ == "__main__":
    init_env()
    log = json.dumps(wblogin(USERNAME, PASSWORD), ensure_ascii=False)
```


[1]:http://github.com/gpxlcj/
[2]:http://weibo.com
[3]:http://weibospider.gpxlcj.com
[4]:http://github.com/gpxlcj/weibospider/wiki/简明使用手册
[5]:http://github.com/gpxlcj/weibospider/wiki/tutorial