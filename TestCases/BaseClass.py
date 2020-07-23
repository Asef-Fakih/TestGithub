from selenium import webdriver
import unittest

class BaseClass(unittest.TestCase):
    global drv
    @classmethod
    def setUpClass(cls):
        cls.drv = webdriver.Chrome()  # the cromedriver is in the path, if not give the path there
        cls.drv.implicitly_wait(3)
        cls.drv.maximize_window()
        cls.drv.get("http://phantom-srv.kaz.com.bd/ccdb.LB")

    @classmethod
    def tearDownClass (cls):
        cls.drv.close()
        cls.drv.quit()
        print("test completed")
        #test line