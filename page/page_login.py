from base.base import Base
import page
from base.get_driver import GetDriver


class PageLogin(Base):

    # 输入用户名
    def page_input_uname(self, username):
        self.base_input(page.userName, username)

    # 输入密码
    def page_input_password(self, password):
        self.base_input(page.passWord, password)

    # 输入验证码
    def page_input_verify_code(self):
        # 获取验证码
        code = self.base_get_text(page.getVerifyCode)
        # 输入验证码
        self.base_input(page.inputVerifyCode, code)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.loginButton)

    # 判断是否登录成功
    def page_if_login_success(self):
        return self.base_element_is_exist(page.ueerNameInfo)

    # 获取登录错误文本
    def page_get_err_text(self):
        return self.base_get_text(page.loginErrText)

    # 退出登陆
    def page_out_login(self):
        try:
            self.base_mouse_action_chains(page.outLoginIcon)
            # 点击退出登陆按钮
            js = "document.querySelector(\"[id*='dropdown-menu']>li\").click()"
            self.driver.execute_script(js)
        except Exception as e:
            print(e)
            self.base_get_image()

    # 组合方法，登录业务直接调用
    def page_login(self, username, password):
        self.page_input_uname(username)
        self.page_input_password(password)
        self.page_input_verify_code()
        self.page_click_login()


def main():
    p = PageLogin(GetDriver().get_driver())
    p.page_login('easyjie', '888888')
    p.page_out_login()


if __name__ == "__main__":
    main()
