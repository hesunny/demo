# -*- coding:utf-8 -*-

from frameWork.basePage import BasePage


class LoginPage(BasePage):
    """
           页面元素与元素的操作区分开来，易于维护
       """
    input_username = "name=>mobile_number"
    input_password = "name=>password"
    search_button_login = "xpath=>//button[contains(text(), '登录')]"

    def type_search_element(self, username, password):
        self.input(self.input_username, username)
        self.input(self.input_password, password)

    def click_button_login(self):
        self.click(self.search_button_login)
        self.sleep(3)

