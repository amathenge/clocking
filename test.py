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
print(d)

for line in f:
    record = line.strip().split()
    if len(record) == 6:
        if record[1] in d.keys():
            print('found: {}'.format(record[1]))


ds = '478   005C66FB FFFFFFFF  0         2021-7-2 4:52:50'
ds = ds.split()
id = d[ds[1]]
dd = ds[4]
dt = ds[5]
date_t = '{} {}'.format(dd,dt)
print(date_t)
date_t = datetime.strptime(date_t, '%Y-%m-%d %H:%M:%S')
print(date_t)

sql = 'insert into data (code, date_time) values (?, ?)'
conn.execute(sql, [id, date_t])
conn.commit()

conn.close()
f.close()