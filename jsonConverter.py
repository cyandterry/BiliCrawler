#!/usr/bin/env python
from optparse import OptionParser
import json
import xlwt

# Adding options for user to name the report file
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="write to a specific FILE", metavar="FILE")
(options, args) = parser.parse_args()
if options.filename is None:
    file = 'result.xls'
else:
    filename = options.filename.split(".")[0]
    file = filename + '.xls'
# File is stored at ***.xls

json_data=open('/home/ycao/Documents/bili/items.json')
data = json.load(json_data)

lineNo = 0
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet('A Test Sheet')
sheet1.write(lineNo, 0, 'url')
sheet1.write(lineNo, 1, 'av number')
sheet1.write(lineNo, 2, 'Title')
sheet1.write(lineNo, 3, 'Play')
sheet1.write(lineNo, 4, 'Favor')
sheet1.write(lineNo, 5, 'Coin')
sheet1.write(lineNo, 6, 'Score')
sheet1.write(lineNo, 7, 'Time')
lineNo += 1

for videoLink in data:
    sheet1.write( lineNo, 0, videoLink['url'])
    sheet1.write( lineNo, 1, videoLink['avNo'])
    sheet1.write( lineNo, 2, videoLink['title'])
    sheet1.write( lineNo, 3, videoLink['play'])
    sheet1.write( lineNo, 4, videoLink['favor'])
    sheet1.write( lineNo, 5, videoLink['v_time'])
    sheet1.write( lineNo, 6, videoLink['v_score'])
    sheet1.write( lineNo, 7, videoLink['time'])
    lineNo += 1

book.save(file)
json_data.close()
