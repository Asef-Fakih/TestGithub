import sys
sys.path.append("..")
from PageObjects.Locator import CommonLocator as locator
from PageObjects.wrapper import Wrapper

class Loginpage():

    def __init__ (self,drv):
        self.drv = drv


    def enter_userName(self, username):
        Wrap = Wrapper(self.drv)
        Wrap.wd_Send_keys(locator.username_textbox_xpath,username)

    def enter_password(self, password):
        Wrap = Wrapper(self.drv)
        Wrap.wd_Send_keys(locator.Password_textbox_xpath, password)

    def click_login(self):
        Wrap = Wrapper(self.drv)
        Wrap.wd_click_simple(locator.Submit_Button_xpath)