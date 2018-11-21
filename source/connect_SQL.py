import os
import pymysql
db = pymysql.connect(
    host = "jmm.cvxf3ahhscl8.us-east-2.rds.amazonaws.com",
    port = 3306,
    user = 'JMM',
    passwd = '1q2w3e4r',
    db = 'JMM',
    charset = 'utf8'
)

cursor = db.cursor()

sql = "SELECT * FROM STORE"

cursor.execute(sql)

data = cursor.fetchall()

data = list(data)
print(data)

db.close()