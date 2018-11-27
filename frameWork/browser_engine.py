# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from data.config import Config, DATA_PATH
from logs.log import Logger

logger = Logger('BrowserEngine').get_logger()


class BrowserEngine(object):

    Firefox_path = Config().get('Firefox_path')
    IE_path = Config().get('IE_path')
    chrome_path = Config().get('chrome_path')
    URL = Config().get('url', index=0)
    user_name = Config().get('login_name')
    password = Config().get('login_password')
    yaml = DATA_PATH + '/config.yaml'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):

        # 根据browser的值调用对应浏览器的驱动器，并在日志中输出步骤
        browser = Config().get('browser')
        if browser == "Firefox":
            driver = webdriver.Firefox(self.Firefox_path)
            time.sleep(2)
            logger.info("starting FireFox browser....")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_path)
            logger.info("starting Chrome browser....")
        elif browser == "IE":
            driver = webdriver.Ie(self.IE_path)
            logger.info("starting IE browser....")
            driver.find_element()
        # 打开配置文件中定义的地址
        driver.get(self.URL)
        time.sleep(3)
        logger.info("open url : %s" % self.URL)
        # 最大化浏览器窗口
        driver.maximize_window()
        logger.info("maximize the current windows...")
        # 登录
        driver.find_element_by_name("mobile_number").send_keys(self.user_name)
        driver.find_element_by_name("password").send_keys(self.password)
        driver.find_element_by_xpath("//button[contains(text(), '登录')]").click()
        logger.info("logining..........")
        time.sleep(2)
        # 设置隐形等待时间
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()

