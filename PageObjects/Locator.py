from selenium import webdriver

class CommonLocator:
    #baseURL
    baseurl = "http://phantom-srv.kaz.com.bd/ccdb.LB"
    #login page objects
    username_textbox_xpath = "/html/body/div[1]/div/div/div/div[2]/form/div/div[2]/input"
    Password_textbox_xpath = "/html/body/div[1]/div/div/div/div[2]/form/div/div[4]/input"
    Submit_Button_xpath = "/html/body/div[1]/div/div/div/div[2]/form/div/div[6]/button"
    projec_nav_bar = "/html/body/div[1]/div[1]/div[1]/nav/div/div[2]/ul/li[1]/a"
    Projects_title = "/html/body/div[1]/div[2]/div[2]/div/div[2]/div/div/div/h1"
    Human_res = "/html/body/div[1]/div[1]/div[1]/nav/div/div[2]/ul/li[2]/a"