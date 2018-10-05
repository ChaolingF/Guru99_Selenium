from selenium import webdriver
import unittest
userID = "mngr156417"
pwd = "ahubAqE"
url = "http://www.demo.guru99.com/V4/"
expect_title = "Guru99 Bank Manager HomePage"

driver = webdriver.Chrome()
driver.get(url)

uid = driver.find_element_by_name("uid")
uid.send_keys(userID)
password = driver.find_element_by_name("password")
password.send_keys(pwd)
driver.find_element_by_name("btnLogin").click()

if(expect_title == driver.title):
    print("Test Case: PASS!!")
else:
    print("Test Case: FAIL!!")

driver.quit()
