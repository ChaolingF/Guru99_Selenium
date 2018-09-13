from selenium import webdriver
import unittest
userID = "mngr153050"
pwd = "UpErara"

class test_Guru99Bank(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.demo.guru99.com/V4/")
    def test_VaildUserIDPWD(self):
        uid = self.driver.find_element_by_name("uid")
        uid.send_keys(userID)
        password = self.driver.find_element_by_name("password")
        password.send_keys(pwd)
        self.driver.find_element_by_name("btnLogin").click()

        managerid = self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[3]/td").text
        self.assertIn(userID,managerid)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()