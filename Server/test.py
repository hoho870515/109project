import pymysql

import pymysql.cursors

db = pymysql.connect(host='140.134.26.4',#連結MySQL
                        user='user1234',
                        password='YgktVErWYMSrDTA9',                             
                        db='register')
cursor = db.cursor()
def getData():
    sql = "select * from patient"

    cursor.execute(sql)#下指令，皆用變數儲存
    rows = cursor.fetchall()
    for i in rows:
        print(i)
def insert():
    sql = "insert into patient values (%s, %s, %s, %s, %s, %s)"
    variable = ('A00000000', 'Roy', '2020-12-29',\
            'AAAAAAA', 'Denver', 0)
    
    cursor.execute(sql, variable)#下指令，皆用變數儲存
    db.commit()
getData()