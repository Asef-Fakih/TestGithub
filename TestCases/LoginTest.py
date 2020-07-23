from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
sys.path.append("...")
from PageObjects.Locator import CommonLocator as cl
from  PageObjects.wrapper import Wrapper
from PageObjects.Login import Loginpage
from TestCases.BaseClass import BaseClass
import time
import unittest

class LoginTest(BaseClass):
    global drv
    @classmethod
    def setUpClass(cls):
        super(LoginTest, cls).setUpClass()

    def test_login(self):
        drv = self.drv
        login = Loginpage(drv)
        login.enter_userName("superadmin1@ccdb.com")
        login.enter_password("123")
        login.click_login()
        time.sleep(6)

    def test_project (self):
        drv = self.drv
        drv.execute_script("arguments[0].click()", drv.find_element_by_xpath(cl.projec_nav_bar))
        wait = WebDriverWait(drv, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, cl.Projects_title)))
        title = element.text
        drv.execute_script("arguments[0].click()", drv.find_element_by_xpath(cl.Human_res))
        time.sleep(5)


    @classmethod
    def tearDownClass (cls):
        super(LoginTest, cls).tearDownClass()


# if __name__ == '__main__':
#     unittest.main()
