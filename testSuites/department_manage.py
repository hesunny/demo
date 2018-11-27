# -*- coding:utf-8 -*-

import unittest
from pageObjects.Department_manage import DepartmentPage
from frameWork.browser_engine import BrowserEngine
import time
from logs.log import Logger

DEPARTMENT_NAME = '自动化测试部门66'
logger = Logger(logger_name='TestDepartmentManage').get_logger()


class TestDepartmentManage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        cls.driver.quit()

    def test_b01_add_department(self):
        add_department_page = DepartmentPage(self.driver)
        time.sleep(2)
        add_department_page.click_department_manager()
        add_department_page.click_add_department()
        add_department_page.type_search_element(DEPARTMENT_NAME, '此为测试部门，可以随意删除')
        add_department_page.click_save_button()
        message = add_department_page.message_text()
        try:
            assert message == '保存成功'
            print("test pass--->test02_新增部门")
        except Exception as e:
            print("test failed as %s" % e, message)
        add_department_page.click_pop_up()

    def test_b02_change_department(self):
        add_department_page = DepartmentPage(self.driver)
        time.sleep(2)
        add_department_page.click_department_manager()


if __name__ == '__main__':
    unittest.main(TestDepartmentManage)
