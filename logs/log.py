# __author__ = 'Yang'
# -*- coding:utf-8 -*-
import os
import logging
from logging.handlers import TimedRotatingFileHandler

"""
日志类。通过通过读取配置文件，定义日志级别，日志文件名，日志格式等
需导入 logger 模块
"""


class Logger(object):
    def __init__(self, logger_name='frameWork'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        self.log_file_name = 'test.log'
        self.backup_count = 5
        # 日志输出的级别
        self.console_output_level = 'WARNING'
        self.file_output_lever = 'DEBUG'
        # 日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):



