# -*- coding:utf-8 -*-

from frameWork.basePage import BasePage


class DepartmentPage(BasePage):
    """
        页面元素与元素的操作区分开来，易于维护
    """
    # 一级元素
    departmentManager = "xpath=>//span[contains(text(), '部门管理')]"  # 部门管理菜单
    # 二级元素
    addDepartmentButton = "xpath=>//button[contains(text(),'新增部门')]"  # 新增部门按钮
    changeDepartmentButton = "xpath=>//button[@btn-content='修改']"  # 修改按钮
    deleteDepartmentButton = "xpath=>//button[contains(text(),'删除')]"  # 删除按钮
    tree_list = "xpath=>//ul[@tree-data='my_data']/li/a/span[@class='indented tree-label ng-binding']"  # 结构树
    # 三级元素
    input_department_name = "xpath=>//input[contains(@name,'name')]"  # 部门名称
    input_description = "xpath=>//input[contains(@name, 'desc')]"  # 部门描述
    save_button = "xpath=>//button[contains(@btn-style, 'save')]"  # 保存
    cancel_button = "xpath=>//button[contains(@btn-style, 'close')]"  # 取消
    delete_pop_up = "xpath=>//button[contains(text(),'确定')]"   # 确定删除
    # 四级元素
    pop_up_text = "xpath=>//div[contains(@class, 'layui-layer-content')]"  # 弹框提示内容
    ok_pop_up = "xpath=>//a[contains(text(),'确定')]"   # 确定

    # 点击部门管理菜单
    def click_department_manager(self):
        self.click(self.departmentManager)
        BasePage.sleep(2)
        self.sleep(2)

    # 点击新增部门按钮
    def click_add_department(self):
        self.click(self.addDepartmentButton)
        self.sleep(2)

    # 获取结构树最后一个元素
    def click_tree_last_element(self):
        self.click_elements(self.tree_list, -2)
        self.sleep(2)

    # 点击修改按钮
    def chang_department(self):
        self.click(self.changeDepartmentButton)
        self.sleep(2)

    # 点击删除
    def delete_department(self):
        self.click(self.deleteDepartmentButton)
        self.sleep(2)
        self.click(self.delete_pop_up)
        self.sleep(2)

    # 查找元素
    def type_search_element(self, department_name_input, description):
        self.input(self.input_department_name, department_name_input)
        self.input(self.input_description, description)

    # 点击保存
    def click_save_button(self):
        self.click(self.save_button)
        self.sleep(2)

    # 获取提示框文本
    def message_text(self):
        message = self.get_text(self.pop_up_text)
        return message

    # 点击提示框确定按钮
    def click_pop_up(self):
        self.click(self.ok_pop_up)
        self.sleep(2)

    # 点击取消
    def click_cancel(self):
        self.click(self.cancel_button)
