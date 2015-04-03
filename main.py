# -*- coding: utf-8 -*-

import os
import sys
import json

from login import get_session, wblogin
from settings import START_PAGE, USERNAME, PASSWORD, START_NUM, TOTAL_PAGE, APP_SOURCE, SAVE_FILE_NAME, SHEET_NAME, KEY_WORDS
from spider import search_info, init_xls


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    print(json.dumps(wblogin(USERNAME, PASSWORD), ensure_ascii=False))
    num = START_NUM #信息总条数
    init_xls()
    for i in KEY_WORDS:
        num = search_info(get_session(), i, str(), str(), num, 1) 
