import pymysql

conn = pymysql.connect(
    host = "jmm.cvxf3ahhscl8.us-east-2.rds.amazonaws.com",
    port = 3306,
    user = 'JMM',
    passwd = '1q2w3e4r',
    db = 'JMM',
    charset = 'utf8'
)

cur = conn.cursor()

def store_insert(num,name,phone,rnaddress,address):
    #num = str(input("넘버 입력:")) # 이부분 구상 해야함
    #name = str(input("가게 이름 입력:"))
    #phone = str(input("가게 번호 입력:"))
    #rnaddress = str(input("가게 도로명 주소 입력:"))
    #address = str(input("가게 지번 주소 입력:"))
    cur.execute("INSERT INTO STORE VALUES('%s','%s','%s','%s','%s');" %(num,name,phone,rnaddress,address))

def choice_insert(loc,type,store):
    #loc = str(input("지역 입력:"))
    #type = str(input("음식 종류 입력:"))
    #store = str(input("맛집 종류 입력:"))
    cur.execute("INSERT INTO CHOICE VALUES('%s','%s','%s');" %(loc,type,store))

#choice_insert("항동","자장면","함지박")
conn.commit()
conn.close()
