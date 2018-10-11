# __author__ = 'Yang'

from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


class AutomateDriver(object):
    """
        ��װһ��ҳ����࣬������ҳ��̳��������
    """

    def __init__(self):
        driver = webdriver.Chrome()
        try:
            self.driver = driver
        except Exception:
            raise NameError('Chrome not found!')

    def clear_cookies(self):
        """
        ���������ʼ���������cookies
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
        ���ֶ�λԪ�ط�ʽ�ķ�װ

        selectorͨ��һ�����С�i,xxx�������Ӵ��ݣ��ָ��Ϊ������
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
            raise NameError('��������Ч��Ԫ������')
        return element

    def input(self, selector, text):
        """
        ���������
        """
        el = self.get_element(selector)
        el .clear()
        el .send_keys(text)

    def click(self, selector):
        """
        �������
        ��:param selector
        """
        el = self.get_element(selector)
        el.click()
        self.sleep(2)

    def click_index(self, selector, index):
        """
        ���ָ��������Ԫ��
        :param selector, index
        """
        el = self.get_element(selector)
        Select(el).select_by_index(index)

    def click_by_text(self, text):
        """
         ͨ�������ı�����Ԫ��
        """
        self.get_element('p'+text).click()

    def execute_js(self, script):
        """
        ִ��JavaScript�ű�

        �÷���
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def scroll_js(self, selector, number):
        """
        ����������Ĳ�ͬ�������������
        number = 0 -----���ص����
               = 10000 -----��������ײ�
        """
        if self.driver.name == 'chrome':
            js = "var q=document.body.scrollTop= %d" % number
            self.driver.execute_script(js)
        else:
            js = "var q=document.getElementById(%s).scrollTop= %d" % selector % number
            self.driver.execute_script(js)

    def elements_focus_js(self, selector):
        """
        �۽�Ԫ�أ���ҳ��ֱ������Ԫ�س��ֵ�λ��
        """
        target = self.get_element(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def get_attribute(self, selector, attribute):
        """
        ��ȡԪ�����Ե�ֵ������Ԫ�ص�����
        """
        el = self.get_element(selector)
        return el.get_attribute(attribute)

    def get_text(self, selector):
        """
        ��ȡԪ�ص��ı���Ϣ,����Ԫ�ص��ı�
        """
        el = self.get_element(selector)
        return el.text

    def get_display(self, selector):
        """
        ��ȡҪ��ʾ��Ԫ�أ����صĽ��Ϊ���١�
        """
        el = self.get_element(selector)
        return el.is_displayed()

    def get_url_address(self):
        """
        ��ȡ��ǰҳ���URL��ַ
        """
        return self.driver.current_url

    def get_window_title(self):
        """
        ��ȡ��ǰ���ڵı���
        """
        return self.driver.title

    def accept_alert(self):
        """
        ���ܾ����
        :return:
        """
        self.driver.switch_to.alert.accept()

