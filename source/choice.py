import pymysql

conn = pymysql.connect(
    host = "jmm.cvxf3ahhscl8.us-east-2.rds.amazonaws.com",
    port = 3306,
    user = 'JMM',
    passwd = '1q2w3e4r',
    db = 'JMM',
    charset = 'utf8')

cur = conn.cursor()

def choice_preference(type: object, store: object) -> object:
    total = cur.execute("SELECT * FROM CHOICE WHERE CHO_TYPE='%s';" % type)
    choice_count = cur.execute("SELECT * FROM CHOICE WHERE CHO_STORE='%s';" % store)
    avg = int(choice_count / total * 100)
    print("선택한 %s 맛집 선호도 : " % type + str(avg) + "%")

#choice_preference("자장면","함지박")
conn.commit()
conn.close()

