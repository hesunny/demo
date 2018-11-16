# __author__ = 'Yang'
# -*- coding:utf-8 -*-

import os
import logging
from logging.handlers import TimedRotatingFileHandler
from data.config import LOG_PATH, Config


"""
日志类。通过读取配置文件，定义日志级别，日志文件名，日志格式等
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
        """
        在logger中添加日志句柄并返回，如果logger中已有句柄，则直接返回
                                """
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count 份
            file_handler = TimedRotatingFileHandler(filename=os.path.join(LOG_PATH),
                                                    when='D', interval='1', backupCount=self.backup_count,
                                                    delay=True, encoding='utf-8')
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_lever)
            self.logger.addHandler(file_handler)
        return self.logger


logger = Logger().get_logger()





