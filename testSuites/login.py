# -*- coding:utf-8 -*-

import unittest
from frameWork.basePage import BasePage
from data.config import Config, DATA_PATH
from data.file_reader import YamlReader
from pageObjects.login import LoginPage


class TestLogin(unittest.TestCase):
    URL = Config().get('url')
    user_name = Config().get('login_name')
    print(user_name)
    password = Config().get('login_password')
    print(password)
    yaml = DATA_PATH + '/config.yaml'

    driver.get(self.URL)
    def test_01_login(self):
        user_login = LoginPage()
        user_login.type_search_element(self.user_name, self.password)
        user_login.click_button_login()


if __name__ == '__main__':
    unittest.main(TestLogin)


