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
        self.assertEqual('網路預約掛號','網路預約掛號')
    
        
    #def test_Reservation(self):
        

if __name__ == '__main__':
    unittest.main()