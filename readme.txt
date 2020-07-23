1. Locators contains the Xpaths of the Elements
2. Wrapper contains the Wrapped Selenium calls :
for example:
    def wd_Send_keys (self, locator, text):
        self.drv.find_element_by_xpath(locator).clear()
        self.drv.find_element_by_xpath(locator).send_keys(text)
3. The wrapper is used and inherited by Page objects to perform actionss
 for example:
     def enter_userName(self, username):
        Wrap = Wrapper(self.drv)
        Wrap.wd_Send_keys(locator.username_textbox_xpath,username)

4. The Basetest has the Setup and the teardown methods
5. Tests use the Pageobjects to create the Tests