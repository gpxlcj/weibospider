# -*- coding:utf8 -*-

import openpyxl as pxl
import shapefile as shp


def convert():
    sp = shp.Writer(shp.POINT)
    sp.field('content')
    sp.field('type', 'C', 40)
    wk = pxl.load_workbook('weibo_iesous.xlsx')
    wb = wk.get_sheet_by_name('iesous')
    l = wb.max_row
    for i in range(2, l+1):
        content = wb.cell(column=1, row=i).value
        longitude = wb.cell(column=2, row=i).value
        latitude = wb.cell(column=3, row=i).value
        try:
            longitude = float(longitude)
            latitude = float(latitude)
            sp.point(longitude, latitude)
            sp.record('xxx', 'Point')
        except:
            pass
    sp.save()
if __name__ == '__main__':
    convert()