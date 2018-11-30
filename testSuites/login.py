# -*- coding:utf-8 -*-

import unittest
from frameWork.browser_engine import BrowserEngine
from data.config import Config
from pageObjects.login_page import LoginPage


class TestLogin(unittest.TestCase):
    user_name = Config().get('login_name2')
    password = Config().get('login_password2')

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_A01_login_out(self):
        login = LoginPage(self.driver)
        login.sleep(3)
        login.click_logout()
        login.type_search_element(self.user_name, self.password)
        login.click_button_login()


if __name__ == '__main__':
    unittest.main(TestLogin)



