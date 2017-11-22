# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact
from application2 import Application2

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_new_contact(unittest.TestCase):
    def setUp(self):
        self.app = Application2()
    
    def test_add_new_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_new_contact(Contact(firstname="asdfaasdf", lastname="asdfeee", address="dfsf", mobile="asfsdg", email="dfs"))
        self.app.logout()

    def test_add_empty_new_contact(self):
        self.app.login(username="admin", password="secret")
        self.app.create_new_contact(Contact(firstname="", lastname="", address="", mobile="", email=""))
        self.app.logout()

    def tearDown(self):
        self.app.destroy()

if __name__ == '__main__':
    unittest.main()
