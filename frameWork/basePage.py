# __author__ = 'Yang'

from selenium import webdriver
import time

class AutomateDriver(object):
    """
        封装一个页面基类，让所有页面继承这个基类
    """

    def __init__(self):
        driver = webdriver.Chrome()
        try:
            self.driver = driver
        except Exception:
            raise NameError('Chrome not found!')

    def clear_cookies(self):
        """
        清楚驱动初始化后的所有cookies
        """
        self.driver.delete_all_cookies()

    def refresh_browser(self):
        self.driver.refresh()

    def maximize_window(self):
        self.driver.maximize_window()

    def get_url(self, url='http://pm-debug2.dzsh.net'):
        self.driver.get(url)

    def quit_browser(self):
        self.quit_browser()

    def close_browser(self):
        self.driver.close()

    def sleep(self, seconds):
        time.sleep(seconds)

    def get_element(self, selector):
        """
        八种定位元素方式的封装

        selector通过一个带有“i,xxx”的例子传递，分割符为“，”
        :return:
            element
        """

        if ',' not in selector:
            return self.driver.find_element_by_xpath(selector)

        selector_by = selector.split(',')[0]
        selector_value = selector.split(',')[1]

        if 'i' in selector_by or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif 'x' in selector_by or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif 'n' in selector_by or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif 'c' in selector_by or selector_by == 'class':
            element = self.driver.find_element_by_class_name(selector_value)
        elif 's' in selector_by or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif 't' in selector_by or selector_by == 'tag':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif 'l' in selector_by or selector_by == 'link':
            element = self.driver.find_element_by_link_text(selector_value)
        elif 'p' in selector_by or selector_by == 'partial':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        else:
            raise NameError('请输入有效的元素类型')
        return element

    def input(self, selector, text):
        """
        操作输入框
        """
        el = self.get_element(selector)
        el .clear()
        el .send_keys(text)

    def click(self, selector):
        """
        点击操作
        """
        el = self.get_element(selector)
        el.click()

