import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import warnings
import  MySQLdb
warnings.filterwarnings('ignore')
driver = webdriver.Firefox(executable_path="geckodriver.exe")

class TestStringMethods(unittest.TestCase):
    
    #test 系統說明
    def test_System(self):
        driver = webdriver.Firefox(executable_path="geckodriver.exe")
        driver.get('https://140.134.26.17:3333/')
        button = driver.find_element_by_xpath("/html/body/form/div/button[3]")
        button.click()
        a = driver.find_element_by_xpath("/html/body/div/p[2]").text
        self.assertEqual(a,'網路預約掛號')
        driver.close()
    
    #
    def test_Inquire(self):
        db  =  MySQLdb . connect ( 
        host = "140.134.26.4" ,      #主機名
        user = "user1234" ,          #用戶名
        passwd = "YgktVErWYMSrDTA9" ,#密碼
        db = "register" ,            #數據庫名稱
        charset="gb2312")       
        cur  =  db . cursor ()
        cur . execute ( "SELECT * FROM patient WHERE Name = 'AAA';" )
        test= cur . fetchall ()
       
        ID=test[0][0]
        date=test[0][1]
        name=test[0][2]
        department=test[0][3]
        doctor=test[0][4]
        number=test[0][5]
        db . close ()
       
        driver.get('https://140.134.26.17:3333/')
        #進入首頁
        button = driver.find_element_by_xpath("/html/body/form/div/button[2]")
        button.click()
        time.sleep(3)
        #進入線上查詢
        button = driver.find_element_by_xpath("/html/body/form/div/p[2]/input")
        button.click()
        time.sleep(3)
        
        inputElement = driver.find_element_by_name("ID")
        inputElement.send_keys(ID)
        
        inputElement = driver.find_element_by_name("name")
        inputElement.send_keys(name)
        
        button = driver.find_element_by_name("determine")
        button.click()
        
        text = driver.find_element_by_xpath("/html/body/form/div/p[@id='patientId']").text
        ID_web=text
        
        text = driver.find_element_by_xpath("/html/body/form/div/p[@id='patientName']").text
        date_web=text
        
        text = driver.find_element_by_xpath("/html/body/form/div/p[@id='date']").text
        name_web=text
        
        text = driver.find_element_by_id("department").text
        department_web=text
        
        text = driver.find_element_by_id("doctor").text
        doctor_web=text
        
        text = driver.find_element_by_xpath("/html/body/form/div/p[@id='number']").text
        number_web=text
        
        time.sleep(4)
        driver.close()

        ID='身分證ID: '+ID
        date='姓名: '+date
        name='日期: '+name
        department='科別: '+department
        doctor='醫生: '+doctor
        number='掛號號碼: '+number
        
        self.assertEqual(ID,ID_web)
        self.assertEqual(date,date_web)
        self.assertEqual(name,name_web)
        self.assertEqual(department,department_web)
        self.assertEqual(doctor,doctor_web)
        self.assertEqual(number,number_web)
        
    #def test_Reservation(self):
        

if __name__ == '__main__':
    unittest.main()