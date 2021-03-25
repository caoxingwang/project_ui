from page.page_login import PageLogin
from page.page_add_student import PageAddStudent
from page.page_add_pay import PageAddPay
from base.get_driver import GetDriver
import page
from base.base import Base


class PageApproveOrder(Base):

    # 审批
    def page_schoolmaster_approve(self, name):
        # 财务菜单
        self.base_click(page.approveManagement)
        # 搜索
        self.base_input(page.approveStudentName, name)
        self.base_click(page.approveSearchButton)
        # 点击审批
        self.base_click(page.approveButton)
        self.base_click(page.approveButton2)


def main():
    PageLogin(GetDriver().get_driver()).page_login("easyjie", 888888)
    PageAddStudent(GetDriver().get_driver()).page_student(addType=2)
    print(PageAddStudent(GetDriver().get_driver()).page_student_name())
    PageAddPay(GetDriver().get_driver()).page_add_pay_info(payType=1)
    PageLogin(GetDriver().get_driver()).page_out_login()
    PageLogin(GetDriver().get_driver()).page_login("lianyouchao", 888888)
    PageApproveOrder(GetDriver().get_driver()).page_schoolmaster_approve("王亮")
    PageLogin(GetDriver().get_driver()).page_out_login()
    PageLogin(GetDriver().get_driver()).page_login("yanlinlin", 888888)
    PageApproveOrder(GetDriver().get_driver()).page_schoolmaster_approve("王亮")


if __name__ == "__main__":
    main()
