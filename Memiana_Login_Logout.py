# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Memiana_Login_Logout(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_Memiana_Login_Logout(self):
        success = True
        wd = self.wd
        wd.get("https://www.memiana.com/login/")
        wd.find_element_by_id("authLogin").click()
        wd.find_element_by_id("authLogin").clear()
        wd.find_element_by_id("authLogin").send_keys("sgorbut@live.ru")
        wd.find_element_by_id("authPassword").click()
        wd.find_element_by_id("authPassword").clear()
        wd.find_element_by_id("authPassword").send_keys("Zk97TQZtAfl0")
        wd.find_element_by_xpath("//div[@id='loginFormButton']//span[.='Войти']").click()
        wd.find_element_by_link_text("Выйти").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
