# __author__ = 'Yang'
# -*- coding:utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from logs.log import Logger

logger = Logger(logger_name='BasePage').get_logger()


class BasePage(object):
    """
        封装一个页面基类，让所有页面继承这个基类
    """

    # 初始化driver
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.5)

    def clear_cookies(self):
        """
        清除驱动初始化后的所有cookies
        """
        self.driver.delete_all_cookies()
        logger.info('clear cookies!!')

    def refresh_browser(self):
        self.driver.refresh()
        logger.info("refresh the browser......")


# 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

# 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

# 最大化浏览器
    def maximize_window(self):
        self.driver.maximize_window()

# 获取地址
    def get_url(self, browser_url):
        self.driver.get(browser_url)

# 关闭浏览器
    def close_browser(self):
        self.driver.close()
        logger.info('close browser...')

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

# 截图
    def get_windows_img(self):

        """
        在这里把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\screenshots下
        """

        file_path = 'F:/Python test/pm_dzsh_debug/screenshots/'
        # 格式化时间
        date = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + date + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
        except NameError as e:
            logger.error("failed to take screenshot! %s" % e)
            self.get_windows_img()

# 定位元素
    def get_element(self, selector):
        """
        八种定位元素方式的封装

        selector通过一个带有“i,xxx”的例子传递，分割符为“，”
        :return:
            element

        这个地方是根据 = > 来切割字符串 """
        element = ''
        if "=>" not in selector:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
            # return self.driver.find_element_by_xpath(selector)
        selector_by = selector.split("=>")[0]
        selector_value = selector.split("=>")[1]

        if selector_by == 'i' or selector_by == "id":
            try:
                element = self.wait.until(EC.visibility_of_element_located((By.ID, selector_value)))
                logger.info("Had find the element \' %s \' successful" % selector_value)
            except NoSuchElementException as e:
                logger.error("No Such Element Exception as %s" % e)
                self.get_windows_img()
        elif selector_by == 'n' or selector_by == 'name':
            element = self.wait.until(EC.visibility_of_element_located((By.NAME, selector_value)))
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, selector_value)))
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, selector_value)))
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            element = self.wait.until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, selector_value)))
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, selector_value)))
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                element = self.wait.until(EC.visibility_of_element_located((By.XPATH, selector_value)))
                logger.info("Had find the element \' %s \' successful" % selector_value)
            except NoSuchElementException as e:
                logger.error("No Such Element Exception as %s" % e)
                self.get_windows_img()
        elif selector_by == 's' or selector_by == 'css_selector':
            element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector_value)))
        else:
            raise NameError('Please enter a valid type of targeting elements.')
        return element

    def get_elements(self, selector):
        """
         获取多个元素，返回元素列表
    """
        elements = ''
        if "=>" not in selector:
            return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, selector)))
            # return self.driver.find_element_by_xpath(selector)
        selector_by = selector.split("=>")[0]
        selector_value = selector.split("=>")[1]

        if selector_by == 'i' or selector_by == "id":
            try:
                elements = self.wait.until(EC.visibility_of_all_elements_located((By.ID, selector_value)))
                logger.info("Had find the elements successful"
                            "by %s valid value: %s " % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No Such Element Exception as %s" % e)
                self.get_windows_img()
        elif selector_by == 'n' or selector_by == 'name':
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.NAME, selector_value)))
        elif selector_by == 'c' or selector_by == 'class_name':
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, selector_value)))
        elif selector_by == 'l' or selector_by == 'link_text':
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.LINK_TEXT, selector_value)))
        elif selector_by == 'p' or selector_by == 'partial_link_text':
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.PARTIAL_LINK_TEXT, selector_value)))
        elif selector_by == 't' or selector_by == 'tag_name':
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, selector_value)))
        elif selector_by == 'x' or selector_by == 'xpath':
            try:
                elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, selector_value)))
                logger.info("Had find the element successful"
                            "by %s valid value: %s" % (selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("No Such Element Exception as %s" % e)
                self.get_windows_img()
        elif selector_by == 's' or selector_by == 'css_selector':
            elements = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector_value)))
        else:
            raise NameError('Please enter a valid type of targeting elements.')
        return elements

    def input(self, selector, text):
        """
            操作输入框
            """
        el = self.get_element(selector)
        el.clear()
        el.send_keys(text)

    def click(self, selector):
        """
        点击操作
        ：:param selector
        """
        el = self.get_element(selector)
        el.click()
        self.sleep(2)

    def click_elements(self, selector, index):
        """获取元素类别，根据索引点击元素"""
        elements = self.get_elements(selector)
        elements_index = elements[index]
        try:
            elements_index.click()
            self.sleep(2)
            logger.info("then element clicked. ")
        except NameError as e:
            logger.error("failed to click the element as %s" % e)

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


