from base.base import Base
import page
from page.page_login import PageLogin
from page.page_add_student import PageAddStudent
from base.get_driver import GetDriver


class PageAddPay(Base):

    def page_add_pay_info(self, payType=1, courseType=1):  # payType=1评估费 2学费;courseType=1单科付费，2课时包
        if payType == 1:
            # 缴费类型
            self.base_is_not_select(page.addPayType, page.addPayTypeAssist)
            # 付款金额
            self.base_input(page.addPayAmount, self.base_random_num())
            # 等待学位天数
            self.base_input(page.addPayWaitDay, self.base_random_num())
            self.base_input(page.addPayPaymentNameAssess, self.base_random_name())
            self.base_is_not_select(page.addPayPayTypeAssess, page.addPayPayTypeAssessInfo)
            self.base_is_not_select(page.addPayCommissionerAssess, page.addPayCommissionerAssessInfo)
            self.base_is_not_select(page.addPayBankAccountAssess, page.addPayBankAccountAssessInfo)
            self.base_is_not_select(page.addPayBillTypeAssess, page.addPayBillTypeAssessInfo)
            if self.base_element_is_exist(page.addPayBillCodeAssess):
                self.base_input(page.addPayBillCodeAssess, self.base_random_num())
            self.base_input(page.addPayPayDateAssess, self.base_random_date())
            self.base_input(page.addPayPayedDateAssess, self.base_random_date())
            self.base_input(page.addPayReceiptDateAssess, self.base_random_date())
        else:
            # 缴费类型
            self.base_is_not_select(page.addPayType, page.addPayTypeTuition)
            if courseType == 1:
                # 购课类型
                self.base_is_not_select(page.addPayBuyCourseType, page.addPayTypeCourseTypeOne)
            else:
                # 购课类型
                self.base_is_not_select(page.addPayBuyCourseType, page.addPayTypeCourseTypePackage)
            # 课程类型
            self.base_click(page.addPayCourseType)
            self.base_click(page.addPayCourseTypeKFXL)
            # 随机课程级别
            self.base_is_not_select(page.addPayCourseLevel, page.addPayCourseLevelInfo)
            # 课程级别
            # self.base_click(page.addPayCourseLevel)
            # self.base_click(page.addPayCourseLevelPrimary)
            # 课程名称
            self.base_is_not_select(page.addPayCourseName, page.addPayCourseNameInfo)
            # 常规课时
            self.base_input(page.addPayRegularClassCount, self.base_random_num())
            # 原单价
            self.base_input(page.addPayPrice, self.base_random_num())
            # 等待学位天数
            self.base_input(page.addPayWaitDay, self.base_random_num())
            # 付款人
            self.base_input(page.addPayPaymentName, self.base_random_name())
            # 付款方式
            self.base_is_not_select(page.addPayPayType, page.addPayPayTypeInfo)
            # 家支经办人
            self.base_is_not_select(page.addPayCommissioner, page.addPayCommissionerInfo)
            # 收款账户
            self.base_is_not_select(page.addPayBankAccount, page.addPayBankAccountInfo)
            # 随机票据类型
            self.base_is_not_select(page.addPayBillType, page.addPayBillTypeInfo)
            if self.base_element_is_exist(page.addPayBillCode):
                self.base_input(page.addPayBillCode, self.base_random_num())
            # 不开具发票
            # self.base_click(page.addPayBillType)
            # self.base_click(page.addPayBillTypeNo)
            # 缴费日期
            self.base_input(page.addPayPayDate, self.base_random_date())
            # 付款日期
            self.base_input(page.addPayPayedDate, self.base_random_date())
            # 到账日期
            self.base_input(page.addPayReceiptDate, self.base_random_date())
        # 提交
        self.base_click(page.addPaySubmit)


def main():
    pageLogin = PageLogin(GetDriver().get_driver())
    pageLogin.page_login("easyjie", "888888")
    pageAddStudent = PageAddStudent(GetDriver().get_driver())
    pageAddStudent.page_student(addType=2)
    pageAddPay = PageAddPay(GetDriver().get_driver())
    pageAddPay.page_add_pay_info(payType=1)
    pageLogin.page_out_login()
    pageLogin.page_login("lianyouchao", "888888")
    # GetDriver().quit_driver()
    print(pageAddStudent.student_name)


if __name__ == "__main__":
    main()
