import unittest
from base.get_driver import GetDriver
from page.page_login import PageLogin


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 实例化driver
        cls.driver = GetDriver().get_driver()
        # 实例化Page对象
        cls.page = PageLogin(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # 关闭浏览器驱动
        GetDriver().quit_driver()

    # 测试登录退出用例
    def test_login(self):
        # 判断是否登录
        if self.page.page_if_login_success():
            # 如果已登录，退出登陆
            self.page.page_out_login()
            # 调用组合方法登录
            self.page.page_login('easyjie', '888888')
        else:
            self.page.page_login('easyjie', '888888')
            self.page.page_out_login()
            self.page.page_login('easyjie', '8888888')
            print(self.page.page_get_err_text() + "hahahahahahahah")
            self.assertEqual(self.page.page_get_err_text(), '用户名或密码错误!')
            self.page.base_get_image()

    # 逆向登录用例
    # def test_err_login(self):
    #     # 输入错误的用户名或密码
    #     self.page.page_login('easyjie', '88888888')
    #     self.assertEqual(self.page.page_get_err_text(), '用户名或密码错误!')
    #     self.page.base_get_image()