# __author__ = 'Yang'
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from data.config import Config, DATA_PATH
from data.file_reader import YamlReader
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):
    """
        封装一个页面基类，让所有页面继承这个基类
    """
    URL = Config().get('url')
    user_name = Config().get('login_name')
    password = Config().get('login_password')
    yaml = DATA_PATH + '/config.yaml'

    def __init__(self):
        chrome_url = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
        driver = webdriver.Chrome(chrome_url)
        self.wait = WebDriverWait(self.driver, 10, 0.5)
        try:
            self.driver = driver
        except Exception:
            raise NameError('Chrome not found!')

    def clear_cookies(self):
        """
        清除驱动初始化后的所有cookies
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

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    def get_element(self, selector):
        """
        八种定位元素方式的封装

        selector通过一个带有“i,xxx”的例子传递，分割符为“，”
        :return:
            element
        """

        if '=>' not in selector:
            return self.driver.find_element_by_xpath(selector)

        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if 'i' in selector_by or selector_by == 'id':
            element = self.driver.find_element_by_id(selector_value)
        elif 'x' in selector_by or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
        elif 'n' in selector_by or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif 'c' in selector_by or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif 's' in selector_by or selector_by == 'css_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        elif 't' in selector_by or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif 'l' in selector_by or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif 'p' in selector_by or selector_by == 'partial_link_text':
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
        ：:param selector
        """
        el = self.get_element(selector)
        el.click()
        self.sleep(2)

    def click_index(self, selector, index):
        """
        点击指定索引的元素
        :param selector, index
        """
        el = self.get_element(selector)
        Select(el).select_by_index(index)

    def click_by_text(self, text):
        """
         通过链接文本单击元素
        """
        self.get_element('p'+text).click()

    def execute_js(self, script):
        """
        执行JavaScript脚本

        用法：
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def scroll_js(self, selector, number=10000):
        """
        根据浏览器的不同操作纵向滚动条
        number = 0 -----》回到最顶部
               = 10000 -----》拉到最底部
        """
        if self.driver.name == 'chrome':
            js = "var q=document.body.scrollTop= %d" % number
            self.driver.execute_script(js)
        else:
            js = "var q=document.getElementById(%s).scrollTop= %d" % (selector,number)
            self.driver.execute_script(js)

    def elements_focus_js(self, selector):
        """
        聚焦元素，让页面直接跳到元素出现的位置
        """
        target = self.get_element(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def submit(self, selector):
        """
        提交指定的信息

        """
        el = self.get_element(selector)
        el.submit()

    def get_attribute(self, selector, attribute):
        """
        获取元素属性的值，返回元素的属性
        """
        el = self.get_element(selector)
        return el.get_attribute(attribute)

    def remove_attribute(self, selector, attribute):
        # 用js去掉某个元素的某个属于
        js = 'document.getElementById(%s).removeAttribute(%s);'%selector %attribute
        self.driver.execute_script(js)

    def get_text(self, selector):
        """
        获取元素的文本信息,返回元素的文本
        """
        el = self.get_element(selector)
        return el.text

    def get_display(self, selector):
        """
        获取要显示的元素，返回的结果为真或假。
        """
        el = self.get_element(selector)
        return el.is_displayed()

    def get_url_address(self):
        """
        获取当前页面的URL地址
        """
        return self.driver.current_url

    def get_window_title(self):
        """
        获取当前窗口的标题
        """
        return self.driver.title

    def accept_alert(self):
        """
        接受警告框
        :return:
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        解除警报框
        """
        self.driver.switch_to.alert.dismiss()

    def implicitly_wait(self, second):
        """
        隐式等待页面上的所有元素
        """
        self.driver.implicitly_wait(second)

    def switch_frame(self, reference, value):
        """
        reference是传入的参数，用来定位frame，可以传入id、name、index以及selenium的WebElement对象
        switch_to.frame() 等同于原来的switch_to_frame()
        """
        if reference == 'element':
            el = self.get_element(value)
            self.driver.switch_to.frame(el)
        elif reference == 'index':
            self.driver.switch_to.frame(value)


