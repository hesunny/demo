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
        c = Config().get('log')
        self.log_file_name = c.get('fileName') if c and c.get('fileName') else 'test.log'  # 日志文件
        self.backup_count = c.get('backupCount') if c and c.get('backupCount') else 5  # 保留的日志数量
        # 日志输出的级别
        self.console_output_level = c.get('consoleLevel') if c and c.get('consoleLevel') else 'WARNING'
        self.file_output_lever = c.get('fileLevel') if c and c.get('fileLevel') else 'DEBUG'
        # 日志输出格式
        pattern = c.get('pattern') if c and c.get('pattern') else \
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        self.formatter = logging.Formatter(pattern)

    def get_logger(self):



