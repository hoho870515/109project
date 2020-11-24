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
    def inquireOrCancel(self, ID, Name):
        try:
            cursor = self.db.cursor()
            sql = ("select * from patient where ID euqal '"+ID+"' ")#下指令，皆用變數儲存
            cursor.execute(sql)
            rows = cursor.fetchall()
            print(rows)
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            self.db.close()#關閉DataBase

# @app.route('/booking', methods = ['GET', 'POST'])
# def booking():
#     pass

# @app.route('/', methods = ['GET', 'POST'])
# def booking():
#     pass

# @app.route('/', methods = ['GET', 'POST'])
# def booking():
#     pass

@app.route('/check', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('Inquire-2.html')
    elif request.method == 'POST':    
        print(request.form.get("ID"))
        print(request.form.get("name"))
        db = dataBase()
        db.inquireOrCancel(ID, name)
        return render_template('Inquire-3.html')

@app.route('/inquireOnline', methods = ['GET', 'POST'])
def inquireOnline():
    if request.method == 'GET':
        return render_template('Inquire-1.html')
    elif request.method == 'POST':
        data = list(request.form.to_dict().keys())
        if data[0] == 'inquireOrCancel':
            return render_template('Inquire-2.html')
        elif data[0] == 'inquireCurrent':
            return render_template('Inquire-4.html')

@app.route('/', methods = ['GET', 'POST'])
def index():
    # db = dataBase()
    # patientData = db.getData()
    
    if request.method == 'GET':
        return render_template('homePage.html')
    elif request.method == 'POST':
        data = list(request.form.to_dict().keys())
        if data[0] == 'inquireOnline':
            return render_template('Inquire-1.html')
        elif data[0] == 'reservation':
            pass
        elif data[0] == 'description':
            pass
    

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 3333, debug = True, ssl_context = ('fcuar.com.pem', 'fcuar.com-key.pem'))
    