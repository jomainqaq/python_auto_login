#coding=utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains #导入鼠标操作
from selenium.webdriver.common.keys import Keys #导入键值操作

import time
import sys

myusername="qq"
mypasswd="passwd"

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("http://www.manew.com/member.php?mod=logging&action=login")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//*[@class='c cl']/div[7]/table/tbody/tr/td/a[1]").click()
#//*[@id="loginform_Lb6p6"]/div/div[7]/table/tbody/tr/td/a[1]

driver.implicitly_wait(10)
driver.switch_to_frame("ptlogin_iframe")     #切换到frame，要不然查找不到元素

driver.implicitly_wait(10)
driver.find_element_by_id("switcher_plogin").click()

driver.implicitly_wait(10)
driver.find_element_by_id("u").send_keys(myusername)
driver.find_element_by_id("p").send_keys(mypasswd)

driver.implicitly_wait(5)
driver.find_element_by_class_name("login_button").click()   #定位到登陆框
#driver.find_elements_by_xpath("//*[@id='login_button']").click()
#//*[@id="login_button"]

driver.implicitly_wait(15)
driver.find_element_by_class_name("i_fx_checkin_b_wei").click()


