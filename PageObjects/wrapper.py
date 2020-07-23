from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from abc import abstractmethod
import selenium

class Wrapper(object):

    def __init__(self, drv):
        self.drv = drv

    def wait_for_element_visiblity(self, waitTime, locator):
        element = WebDriverWait(self.drv, waitTime).until(EC.visibility_of_element_located(By.XPATH, locator))
        return element

    def wait_until_element_clickable(self, waitTime, locator):
        element = WebDriverWait(self.drv, waitTime).until(EC.element_to_be_clickable(By.XPATH, locator))
        return element

    def switch_to_window(self, wHandle):
        self.drv.switch_to.window(wHandle)

    def wd_find_web_element (self, locator):
        webel = self.drv.find_element_by_xpath(locator)
        return webel

    def wd_Send_keys (self, locator, text):
        self.drv.find_element_by_xpath(locator).clear()
        self.drv.find_element_by_xpath(locator).send_keys(text)


    def wd_click (self, waitTime, locator):
        self.wait_until_element_clickable(waitTime, "xpath", locator ).click()

    def wd_click_simple(self, locator):
        self.drv.find_element_by_xpath(locator).click()
