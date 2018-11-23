# -*- coding:utf-8 -*-

import unittest
from data.config import Config, DATA_PATH
from pageObjects.login import LoginPage


driver = LoginPage()


class TestLogin(unittest.TestCase):
    URL = Config().get('url')
    user_name = Config().get('login_name')
    password = Config().get('login_password')
    yaml = DATA_PATH + '/config.yaml'

    def test_01_login(self):
        driver.type_search_element(self.user_name, self.password)
        driver.click_button_login()
        driver.click_logout()

    def test_02_logout(self):

        driver.type_search_element(self.user_name, self.password)
        driver.click_button_login()
        driver.click_logout()


if __name__ == '__main__':
    unittest.main(TestLogin)



