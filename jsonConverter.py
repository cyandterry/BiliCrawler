#!/usr/bin/env python
import json
import xlwt
from pprint import pprint

json_data=open('/home/ycao/Documents/bili/bili/another.json')

data = json.load(json_data)
lineNo = 0
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet('A Test Sheet')
sheet1.write(lineNo, 0, 'url')
sheet1.write(lineNo, 1, 'title')
sheet1.write(lineNo, 2, 'time')
lineNo += 1
print type(lineNo)
for videoLink in data:
    sheet1.write( lineNo, 0, videoLink['url'])
    sheet1.write( lineNo, 1, videoLink['title'])
    sheet1.write( lineNo, 2, videoLink['time'])
    lineNo += 1
book.save("result.xls")
print 'Done with saving'
json_data.close()
