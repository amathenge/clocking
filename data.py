#!/usr/bin/env python
from datetime import datetime
import sqlite3
f = open('02072021-Nightlogs.txt', 'r')

conn = sqlite3.connect('clocking.db')
conn.row_factory = sqlite3.Row
d = {}
sql = 'select * from codes order by id'
cur = conn.cursor()
res = cur.execute(sql)
for item in res:
    d[item['code']] = item['id']

record = ''
for line in f:
    record = line.strip().split()
    if len(record) == 6:
        if record[1] in d.keys():
            id = d[record[1]]
            dd = record[4]
            tt = record[5]
            date_time = datetime.strptime('{} {}'.format(dd,tt), '%Y-%m-%d %H:%M:%S')
            sql = 'insert into data (code, date_time) values (?, ?)'
            conn.execute(sql, [id, date_time])
            conn.commit()

conn.close()
f.close()