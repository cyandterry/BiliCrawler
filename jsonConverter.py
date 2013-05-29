#!/usr/bin/env python
import json
import xlwt
from pprint import pprint

json_data=open('/home/ycao/Documents/bili/bili/another.json')

data = json.load(json_data)
lineNo = 0
book = xlwt.Workbook(encoding="utf-8")
sheet1.write(lineNo, 0, 'url')
sheet1.write(lineNo, 1, 'title')
sheet1.write(lineNo, 2, 'time')
lineNo += 1

for videoLink in data:
    sheet1.write(lineNo, 0, data['url'])
    sheet1.write(lineNo, 1, data['title'])
    sheet1.write(lineNo, 2, data['time'])
    lineNo += 1
book.save("result.xls")

json_data.close()
