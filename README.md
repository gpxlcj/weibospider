微博爬虫 WeiboSpider
==
**Author:** [gpxlcj][1]</br>
**Update time:**2015.05.07</br>

[TOC]

Description
----------

A spider to catch the microblog data from [weibo][2].</br>
The data can be crawled by time, keywords and so on.the data field can be customed to grab.

**The summarize of each scripts:**

`main.py`         start script</br>
`settings.py`     the configure file</br>
`weibo_api.py`    get info via weibo api</br>
`save.py`         save data</br>
`login.py`        account login</br>
`base.py`         base function</br>
`spider.py`       catch weibo data</br>
`convert_shp.py`  convert to shp data</br>

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
