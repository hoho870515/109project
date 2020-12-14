from flask import Flask, request, send_from_directory, render_template, url_for, jsonify, Blueprint
import base64
import os
import time
import json
import pymysql

app = Flask(__name__)

class dataBase:
    def __init__(self, db = None):
        import pymysql.cursors
        # self.db = db
        self.db = pymysql.connect(host='140.134.26.4',#連結MySQL
                                user='user1234',
                                password='YgktVErWYMSrDTA9',                             
                                db='register')
    # def open_db(self):#開啟Database
    def getPatient(self):
        pass
    def getRegisterInfo(self):
        pass
    def getMedicalRecord(self):
        pass
    def getData(self):
        try:
            cursor = self.db.cursor()
            sql = ("select * from patient")#下指令，皆用變數儲存
            cursor.execute(sql)
            rows = cursor.fetchall()
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            self.db.close()#關閉DataBase
        
        return list(rows[0])
    def booking():
        pass
    def inquire(self, ID, Name):
        try:
            cursor = self.db.cursor()
            sql = ("select * from patient where ID = '"+ID+"' ")#下指令，皆用變數儲存
            cursor.execute(sql)
            rows = cursor.fetchall()
            # print(len(rows))
            # print(rows)
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            self.db.close()#關閉DataBase
        return json.dumps(rows)
    def cancel():
        pass

# @app.route('/booking', methods = ['GET', 'POST'])
# def booking():
#     pass

@app.route('/reservationOnline', methods = ['GET', 'POST'])
def reservationOnline():
    if request.method == 'GET':
        return render_template('reservation-Online-1.html')
    elif request.method == 'POST':
        print(request)
        data = list(request.form.keys())
        ID = request.form.get("ID")
        name = request.form.get("name")
        # if 'onlineBooking' in data:    
        #     print('ID: ', ID, 'name: ', name)
        #     return render_template('reservation-Online-1.html')

@app.route('/reservation', methods = ['GET', 'POST'])
def reservation():
    if request.method == 'GET':
        return render_template('reservation.html')
    elif request.method == 'POST':
        print(request)
        data = list(request.form.keys())
        ID = request.form.get("ID")
        name = request.form.get("name")
        if 'onlineBooking' in data:    
            print('ID: ', ID, 'name: ', name)
            return render_template('reservation-Online-1.html')
        elif 'phoneBooking' in data:
            return render_template('reservation-Phone.html')
        else:
            return render_template('reservation.html')

@app.route('/check', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('Inquire-2.html')
    elif request.method == 'POST':
        print(request)
        data = list(request.form.keys())
        if 'determine' in data:
            ID = request.form.get("ID")
            name = request.form.get("name")
            print('ID: ', ID, 'name: ', name)
            db = dataBase()
            patientData = json.loads(db.inquire(ID, name))[0]
            return render_template('Inquire-3.html', patientData = patientData)
        elif 'cancel' in data:
            print('cancel')
            return render_template('homePage.html')
        elif 'return' in data:
            print('return')
            return render_template('Inquire-2.html')
        else:
            return render_template('Inquire-3.html')

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
    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 3333, debug = True, ssl_context = ('fcuar.com.pem', 'fcuar.com-key.pem'))
    