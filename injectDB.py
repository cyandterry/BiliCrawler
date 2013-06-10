#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import json

con = None

json_data=open('./items.json')
data = json.load(json_data)

try:
    con = lite.connect('result.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Bilibili(
                      avNo     integer primarykey,
                      Title    text,
                      URL      text,
                      Play     integer,
                      Favor    integer,
                      Coin     integer,
                      Score    integer,
                      Time     text
               );''')

    for dataItem in data:
        cur.execute('INSERT INTO Bilibili VALUES(?,?,?,?,?,?,?,?)', (dataItem['avNo'],dataItem['title'],dataItem['url'],dataItem['play'],dataItem['favor'],dataItem['v_time'],dataItem['v_score'],dataItem['time']))


except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.commit()
        con.close()
