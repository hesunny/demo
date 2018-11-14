# -*- coding:utf-8 -*-

import unittest
from pageObjects.login import LoginPage
from frameWork.basePage import BasePage
from frameWork.config import Config, DRIVER_PATH, DATA_PATH
from frameWork.file_reader import YamlReader
from pageObjects.login import LoginPage


class TestLogin(unittest.TestCase):
    URL = Config().get('url')
    yaml = DATA_PATH + '/config.yaml'

    def sub_setup(cls):
        driver = BasePage()
        cls.driver = driver.get_url(cls.URL)

    def login(self):
        user_login = LoginPage()
        datas = YamlReader(self.yaml).data
        for d in datas:
            with self.subTest(data=d):
                self.sub_setup()
                user_login.type_search_element()
                user_login.click_button_login()


if __name__ == '__main__':
    unittest.main(verbosity=2)


