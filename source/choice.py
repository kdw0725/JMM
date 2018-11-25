import os
import pymysql
import collections

conn = pymysql.connect(
        host="jmm.cvxf3ahhscl8.us-east-2.rds.amazonaws.com",
        port=3306, user='JMM',
        passwd='1q2w3e4r',
        db='JMM',
        charset='utf8'
)

cur = conn.cursor()

type = ''
store = ''

#cur.execute("SELECT * FROM CHOICE WHERE CHO_TYPE='?' and CHO_STORE='?', (type,store))


cur.execute("SELECT FROM CHOICE WHERE CHO_STORE=store");


conn.close()