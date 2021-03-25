import page
from page.page_login import PageLogin
from base.get_driver import GetDriver
from base.base import Base
import time


class PageAddStudent(Base):

    def page_student_name(self):
        return self.base_random_name()

    def page_student(self, addType=1):  # pay_type=1为添加学员，=2添加并缴费
        # 学生管理菜单
        self.base_click(page.studentManagement)
        # 姓名
        student_name = self.page_student_name()
        self.base_input(page.addStudentName, student_name)
        # 性别
        self.base_is_not_select(page.addStudentSex, page.addStudentSexInfo)
        # 随机校区
        # self.base_is_not_select(page.addStudentSchool, page.addStudentSchoolInfo)
        # 指定校区
        self.base_click(page.addStudentSchool)
        time.sleep(2)
        self.base_click(page.addStudentSpecifiedSchool)
        # 出生日期
        self.base_input(page.addStudentBirthday, self.base_random_date())
        # 身份证
        self.base_input(page.addStudentIdentity, self.base_random_identity())
        # 民族
        self.base_is_not_select(page.addStudentNation, page.addStudentNationInfo)
        # 籍贯
        self.base_is_not_select(page.addStudentNativePlace, page.addStudentNativePlaceInfo)
        # 入学时间
        self.base_input(page.addStudentStartSchoolTime, self.base_random_date())
        # 监护人姓名
        self.base_input(page.addStudentGuardianName, self.base_random_name())
        # 监护人身份证
        self.base_input(page.addStudentGuardianIdentity, self.base_random_identity())
        # 联系电话
        self.base_input(page.addStudentPhone, self.base_random_phone())
        # 在校状态
        self.base_click_radio_button(page.addStudentSchoolStatusCode)
        # 上课状态
        self.base_click_radio_button(page.addStudentAttendStatus)
        # 评估状态
        self.base_click_radio_button(page.addStudentAssessStatus)
        # 现居住地址--省
        self.base_is_not_select(page.addStudentCurrentAddressProvince, page.addStudentCurrentAddressProvinceInfo)
        # 现居住地址--市
        self.base_is_not_select(page.addStudentCurrentAddressCity, page.addStudentCurrentAddressCityInfo)
        # 现居住地址--区县
        self.base_is_not_select(page.addStudentCurrentAddressCounty, page.addStudentCurrentAddressCountyInfo)
        # 现居住地址--详细地址
        self.base_input(page.addStudentCurrentAddressInfo, self.base_random_address())
        if addType == 1:
            # 提交
            self.base_click(page.addStudentSubmit)
        else:
            self.base_click(page.addStudentSubmitAndPay)


def main():
    pageLogin = PageLogin(GetDriver().get_driver())
    pageLogin.page_login("easyjie", "888888")
    pageAddStudent = PageAddStudent(GetDriver().get_driver())
    pageAddStudent.page_student(addType=2)
    print(pageAddStudent.student_name)
    # GetDriver().quit_driver()


if __name__ == "__main__":
    main()
