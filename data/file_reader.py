# __author__ = 'Yang'
# -*- coding:utf-8 -*-
# http://www.cnblogs.com/zidonghua/p/7430083.html#_label2
import yaml
import os
from xlrd import open_workbook

"""
文件读取。YamlReader读取yaml文件，ExcelReader读取excel。
"""


class YamlReader:
    def __init__(self, yaml):
        if os.path.exists(yaml):
            self.yaml = yaml
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        """
            如果是第一次调用data，读取yaml文件，否则直接返回之前保存的数据
        """
        if not self._data:
            with open(self.yaml, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
      读取excel文件中的内容。返回list。
      """
    def __init__(self, excel, sheet, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            workbook = open_workbook(self.excel)

            if type(self.sheet) not in [int, str]:
                raise SheetTypeError('please pass in <type int> or <type str>, not{0}'.format(type(self.sheet)))
            elif type == int:
                s = workbook.sheet_by_index(self.sheet)
            else:
                s = workbook.sheet_by_name(self.sheet)

            if self.title_line:
                title = s.row_values(0)   # 首行为title

                for col in range(1, s.nrows):
                    self._data.append(dict(zip(title, s.row_values(col))))
                    # 依次遍历其余行，与首行组成dict, 加入到self._data中
            else:
                for col in range(0, s.nrows):
                    # 遍历所有行，加到self._data中
                    self._data.append(s.row_values(col))
        return self._data


if __name__ == '__main__':
    # y = 'F:/Python test/pm_dzsh_debug/data/config.yaml'
    # reader = YamlReader(y)
    # print(reader.data)

    # e = 'F:/Python test/pm_dzsh_debug/data/config.xls'
    # reader_e = ExcelReader(e, sheet='login', title_line=False)
    # print(reader_e.data)
    a = 'F:/Python test/pm_dzsh_debug/data/config.xls'
    reader_a = ExcelReader(a, sheet='login', title_line=True)
    print(reader_a.data)