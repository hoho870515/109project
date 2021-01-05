from flask import Flask, request, flash, render_template, url_for, jsonify
import base64
import os
import time
import json
import pymysql
import test
app = Flask(__name__)
app.config['SESSION_PROTECTION'] = 'strong'
app.config['SECRET_KEY'] = 'yeee'

class dataBase:
    def __init__(self, db = None):
        import pymysql.cursors
        # self.db = db
        self.db = pymysql.connect(host='140.134.26.4',#連結MySQL
                                user='user1234',
                                password='YgktVErWYMSrDTA9',                             
                                db='register')
    def open_db(self, sql, instruct, variable):#開啟Database
        rows = 'yeeeee'
        try:
            cursor = self.db.cursor()
            if instruct == 'select':
                print('select sql', sql, variable)
                cursor.execute(sql, variable)#下指令，皆用變數儲存
                rows = cursor.fetchone()
            elif instruct == 'insert':
                print('insert sql : ', sql, variable)
                cursor.execute(sql, variable)#下指令，皆用變數儲存
                self.db.commit()
                rows = 'Successed Reservation'
            elif instruct == 'delete':
                cursor.execute(sql, variable)#下指令，皆用變數儲存
                self.db.commit()
                rows = 'Successed Delete'
            else:
                rows = None
            print(instruct, 'result', rows, '\n')
            return rows
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            self.db.close()#關閉DataBase
        return rows
    def reservationOnline(self, ID, name, date, department, doctor):
        sql = "insert into patient values (%s, %s, %s, %s, %s, %s)"
        result = self.open_db(sql, 'insert', (ID, name, date, department, doctor, '0'))
        return result
    def inquire(self, ID, Name):
        sql = "select * from patient where ID = %s "#下指令，皆用變數儲存
        result = self.open_db(sql, 'select', ID)
        if result != None:
            result = json.dumps(result)
        
        return result
    def cancel(self, ID, name):
        sql = "delete from patient where ID = %s"
        result = self.open_db(sql, 'delete', ID)
        return result

@app.route('/reservationOnline', methods = ['GET', 'POST'])
def reservationOnline():
    if request.method == 'GET':
        return render_template('reservation-Online-1.html')
    elif request.method == 'POST':
        data = list(request.form.keys())
        print('data : ', data)
        if 'determine' in data:
            ID = request.form.get('patientId')
            name = request.form.get('patientName')
            date = request.form.get('date')
            department = request.form.get('department')
            doctor = request.form.get('doctor')

            db = dataBase()
            result = db.inquire(ID, name)
            if result == None:
                db = dataBase()
                patientData = db.reservationOnline(ID, name, date, department, doctor)
            else:
                patientData = 'None'
            print('Reservation result : ', patientData)
            return render_template('homePage.html', patientData = patientData)
        elif 'return' in data:
            print('return')
            return render_template('homePage.html')
        
#預約掛號
@app.route('/reservation', methods = ['GET', 'POST'])
def reservation():
    if request.method == 'GET':
        return render_template('reservation.html')
    elif request.method == 'POST':
        print(request)
        data = list(request.form.keys())
        print(data)
        if 'onlineBooking' in data:
            return render_template('reservation-Online-1.html', patientData = None)
        elif 'phoneBooking' in data:
            return render_template('reservation-Phone.html')
        else:
            return render_template('reservation.html')

@app.route('/check', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('Inquire-2.html')
    elif request.method == 'POST':
        
        data = list(request.form.keys())
        print(data)
        if 'determine' in data:
            ID = request.form.get("patientId")
            name = request.form.get("patientName")
            
            db = dataBase()
            result = db.inquire(ID, name)
            if result != None:
                db = dataBase()
                patientData = json.loads(db.inquire(ID, name))
            else:
                patientData = 'Inquire None'
            print('Inquire result : ', patientData)
            
            return render_template('Inquire-3.html', patientData = patientData)
        elif 'cancel' in data:
            print(request.form.get("patientId"))
            ID = request.form.get("patientId")
            name = request.form.get("patientName")
            print('cancel : ID', ID, ' Name ', name)

            db = dataBase()
            result = db.inquire(ID, name)
            if result != None:
                db = dataBase()
                patientData = db.cancel(ID, name)
            else:
                patientData = 'None'
            print('Cancel result : ', patientData)
            # return render_template('homePage.html')
        elif 'return' in data:
            print('return')
            return render_template('Inquire-2.html')
        else:
            return render_template('Inquire-3.html')
#查詢/取消預約掛號
@app.route('/inquireOnline', methods = ['GET', 'POST'])
def inquireOnline():
    if request.method == 'GET':
        return render_template('Inquire-1.html')
    elif request.method == 'POST':
        data = list(request.form.keys())
        print(data)
        if 'inquireOrCancel' in data:
            return render_template('Inquire-2.html')
        elif 'inquireCurrent' in data:
            return render_template('Inquire-4.html')

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('homePage.html')
    elif request.method == 'POST':
        data = list(request.form.keys())
        if 'inquireOnline' in data:
            return render_template('Inquire-1.html')
        elif 'reservation' in data:
            return render_template('reservation.html')
        elif 'description' in data:
            return render_template('description.html')
    
@app.route('/test',methods = ['GET', 'POST'])
def test():
    test.getData()

    return render_template('test.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 3333, debug = True, ssl_context = ('fcuar.com.pem', 'fcuar.com-key.pem'))
    