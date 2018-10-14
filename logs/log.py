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
    def __init__(self, logger_name='framework'):
        self.logger = logging.getLogger(logger_name)
        logging.root.setLevel(logging.NOTSET)
        c = config