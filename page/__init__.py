from selenium.webdriver.common.by import By
from base.base import Base

# url链接
URL = "http://rmgs-dev-216.mijiaoyu.cn/"
# 用户名
userName = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[1]/div/div/input'
# 密码
passWord = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[2]/div/div/input'
# 验证码
inputVerifyCode = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[3]/div/div/input'
# 获取验证码
getVerifyCode = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[3]/div/button/span'
# 登录按钮
loginButton = By.XPATH, '//*[@id="app"]/div[1]/div/div/div/form/div[4]/div/div'
# 判断是否登录成功--用户信息
ueerNameInfo = By.XPATH, '//*[@id="app"]/section/section/header/div[2]/span'
# 退出登陆
outLoginIcon = By.XPATH, '//*[@id="app"]/section/section/header/div[2]/span/i'
outLoginButton = By.CSS_SELECTOR, '#dropdown-menu-4531 > li'
# 登录错误提示文本
loginErrText = By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div/form/p/span'
# 菜单--学生管理
studentManagement = By.XPATH, '//*[@id="app"]/section/aside/ul/li[3]/div/span'
# 添加学生--输入姓名
addStudentName = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[1]/td[1]/div/input'
# 添加学生--选择性别
addStudentSex = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[1]/td[2]/div/div/input'
# 添加学生--性别下拉框
addStudentSexInfo = By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li'
# 添加学生--选择校区
addStudentSchool = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[2]/td[3]/div/div/input'
# 添加学生--指定校区
addStudentSpecifiedSchool = By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[4]/span'
# 添加学生--校区下拉框
addStudentSchoolInfo = By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li'
# 添加学生--出身日期
addStudentBirthday = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[1]/td[3]/div/input'
# 添加学生--身份证号
addStudentIdentity = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[1]/td[4]/div/input'
# 添加学生--民族
addStudentNation = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[2]/td[1]/div/div/input'
# 添加学生--民族下拉框
addStudentNationInfo = By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li'
# 添加学生--籍贯
addStudentNativePlace = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[2]/td[2]/div/div[1]/input'
# 添加学生--籍贯下拉框
addStudentNativePlaceInfo = By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li'
# 添加学生--入学日期
addStudentStartSchoolTime = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[2]/td[4]/div/input'
# 添加学生--监护人姓名
addStudentGuardianName = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[4]/td[1]/div/input'
# 添加学生--监护人身份证号
addStudentGuardianIdentity = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[4]/td[2]/div/input'
# 添加学生--联系电话
addStudentPhone = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[4]/td[3]/div/input'
# 添加学生--在校状态
addStudentSchoolStatusCode = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[5]/td/label/span'
# 添加学生--上课状态
addStudentAttendStatus = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[6]/td/label/span'
# 添加学生--评估状态
addStudentAssessStatus = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[7]/td/label/span'
# 添加学生--现居住地址--省
addStudentCurrentAddressProvince = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[9]/td[1]/div/div[1]/input'
# 添加学生--现居住地址--省下拉列表
addStudentCurrentAddressProvinceInfo = By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul/li'
# 添加学生--现居住地址--市
addStudentCurrentAddressCity = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[9]/td[2]/div/div[1]/input'
addStudentCurrentAddressCityInfo = By.XPATH, '/html/body/div[9]/div[1]/div[1]/ul/li'
# 添加学生--现居住地址--区县
addStudentCurrentAddressCounty = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[9]/td[3]/div/div[1]/input'
addStudentCurrentAddressCountyInfo = By.XPATH, '/html/body/div[10]/div[1]/div[1]/ul/li'
# 添加学生--现居住地址--详细地址
addStudentCurrentAddressInfo = By.XPATH, '//*[@id="pane-basicInfo"]/div/table/tr[9]/td[4]/div/input'
# 添加学生--提交按钮
addStudentSubmit = By.XPATH, '//*[@id="app"]/section/section/main/div/div/button[1]/span'
# 添加学生--提交并缴费按钮
addStudentSubmitAndPay = By.XPATH, '//*[@id="app"]/section/section/main/div/div/button[2]/span'
# 添加缴费--缴费类型
addPayType = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[1]/table/tr[3]/td[1]/div/div/input'
# 添加缴费--缴费类型--评估费
addPayTypeAssist = By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[4]/span'
# 添加缴费--缴费类型--学费
addPayTypeTuition = By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]/span'
# 添加缴费--购课类型
addPayBuyCourseType = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[1]/table/tr[3]/td[2]/div/div/input'
# 添加缴费--购课类型--单科付费
addPayTypeCourseTypeOne = By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span'
# 添加缴费--购课类型--课时包
addPayTypeCourseTypePackage = By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]/span'
# 添加缴费--缴费属性--续费
addPayAttributeRenewal = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[1]/table/tr[3]/td[3]/label[2]/span[2]'
# 添加缴费--缴费属性--首次缴费
addPayAttributeFirst = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[1]/table/tr[3]/td[3]/label[1]/span[2]'
# 添加缴费--是否立即上课
addPayIfGoToClass = By.XPATH, ''
# 添加缴费--等待学位天数
addPayWaitDay = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[1]/table/tr[4]/td[2]/div/input'
# 添加缴费--课程类型
addPayCourseType = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[2]/th/div/div[3]/table/tbody/tr/td[' \
                             '2]/div/div/div[1]/input '
# 康复训练
addPayCourseTypeKFXL = By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span'
# 添加缴费--课程级别
addPayCourseLevel = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[2]/th/div/div[3]/table/tbody/tr/td[' \
                              '3]/div/div/div/input '
# 添加缴费--课程级别下拉列表
addPayCourseLevelInfo = By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li'
# 添加缴费--课程级别--初级 ---为啥找不了
addPayCourseLevelPrimary = By.CSS_SELECTOR, 'body > div:nth-child(7) > div.el-scrollbar > ' \
                                            'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > li:nth-child(1) '
# 添加缴费--课程名称
addPayCourseName = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[2]/th/div/div[3]/table/tbody/tr/td[' \
                             '4]/div/div/div/input '
# 添加缴费--课程名称下拉列表
addPayCourseNameInfo = By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul/li'
# 添加缴费--常规课时
addPayRegularClassCount = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[2]/th/div/div[3]/table/tbody/tr/td[' \
                                    '5]/div/div/input '
# 添加缴费--原单价
addPayPrice = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(2) > table > tr:nth-child(2) > th > div > ' \
                               'div.el-table__body-wrapper.is-scrolling-left > table > tbody > tr > ' \
                               'td.el-table_1_column_6.is-center > div > div > input '
# 添加缴费--付款人--学费
addPayPaymentName = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(3) > table > tr:nth-child(2) > ' \
                                     'td:nth-child(2) > div > input '
# 添加缴费--付款金额
addPayAmount = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[2]/td[2]/div/input'
# 添加缴费--付款方式--学费
addPayPayType = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(3) > table > tr:nth-child(2) > td:nth-child(' \
                                 '6) > div > div > input '
# 添加缴费--付款方式下拉列表--学费
addPayPayTypeInfo = By.CSS_SELECTOR, 'body > div:nth-child(9) > div.el-scrollbar > ' \
                                     'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--家支经办人--学费
addPayCommissioner = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(3) > table > tr:nth-child(2) > ' \
                                      'td:nth-child(8) > div > div.el-input.el-input--small.el-input--suffix > input '
# 添加缴费--家支经办人下拉列表--学费
addPayCommissionerInfo = By.CSS_SELECTOR, 'body > div:nth-child(10) > div.el-scrollbar > ' \
                                          'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--收款账户--学费
addPayBankAccount = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(3) > table > tr:nth-child(3) > ' \
                                     'td:nth-child(2) > div > div.el-input.el-input--small.el-input--suffix > input '
# 添加缴费--收款账户下拉列表--学费
addPayBankAccountInfo = By.CSS_SELECTOR, 'body > div:nth-child(11) > div.el-scrollbar > ' \
                                         'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--票据类型--学费
addPayBillType = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(3) > table > tr:nth-child(3) > ' \
                                  'td:nth-child(4) > div > div.el-input.el-input--small.el-input--suffix > input '
# 添加缴费--票据类型下拉列表--学费
addPayBillTypeInfo = By.CSS_SELECTOR, 'body > div:nth-child(12) > div.el-scrollbar > ' \
                                      'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--票据类型下拉列表--不开具发票--学费
addPayBillTypeNo = By.CSS_SELECTOR, 'body > div:nth-child(8) > div.el-scrollbar > ' \
                                    'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul > ' \
                                    'li.el-select-dropdown__item.hover '
# 添加缴费--票据编码--学费
addPayBillCode = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[3]/table/tr[3]/td[3]/div/input'
# 添加缴费--缴费日期--学费
addPayPayDate = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[3]/table/tr[4]/td[1]/div/input'
# 添加缴费--付款日期--学费
addPayPayedDate = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[3]/table/tr[4]/td[2]/div/input'
# 添加缴费--到账日期--学费
addPayReceiptDate = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[3]/table/tr[4]/td[3]/div/input'
# 添加缴费--付款人--入学评估
addPayPaymentNameAssess = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[2]/td[1]/div/input'
# 添加缴费--付款方式--入学评估
addPayPayTypeAssess = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(2) > table > tr:nth-child(2) > ' \
                                       'td:nth-child(6) > div > div.el-input.el-input--small.el-input--suffix > ' \
                                       'input '
# 添加缴费--付款方式下拉列表--入学评估
addPayPayTypeAssessInfo = By.CSS_SELECTOR, 'body > div:nth-child(5) > div.el-scrollbar > ' \
                                           'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--家支经办人--入学评估
addPayCommissionerAssess = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(2) > table > tr:nth-child(2) > ' \
                                            'td:nth-child(8) > div > div > input '
# 添加缴费--家支经办人下拉列表--入学评估
addPayCommissionerAssessInfo = By.CSS_SELECTOR, 'body > div:nth-child(6) > div.el-scrollbar > ' \
                                                'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--收款账户--入学评估
addPayBankAccountAssess = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(2) > table > tr:nth-child(3) > ' \
                                           'td:nth-child(2) > div > div.el-input.el-input--small.el-input--suffix > ' \
                                           'input '
# 添加缴费--收款账户下拉列表--入学评估
addPayBankAccountAssessInfo = By.CSS_SELECTOR, 'body > div:nth-child(7) > div.el-scrollbar > ' \
                                               'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--票据类型--入学评估
addPayBillTypeAssess = By.CSS_SELECTOR, '#pane-pay > div > table > tr:nth-child(2) > table > tr:nth-child(3) > ' \
                                        'td:nth-child(4) > div > div > input '
# 添加缴费--票据类型下拉列表--入学评估
addPayBillTypeAssessInfo = By.CSS_SELECTOR, 'body > div:nth-child(8) > div.el-scrollbar > ' \
                                            'div.el-select-dropdown__wrap.el-scrollbar__wrap > ul '
# 添加缴费--票据编码--入学评估
addPayBillCodeAssess = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[3]/td[3]/div/input'
# 添加缴费--缴费日期--入学评估
addPayPayDateAssess = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[4]/td[1]/div/input'
# 添加缴费--付款日期--入学评估
addPayPayedDateAssess = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[4]/td[2]/div/input'
# 添加缴费--到账日期--入学评估
addPayReceiptDateAssess = By.XPATH, '//*[@id="pane-pay"]/div/table/tr[2]/table/tr[4]/td[3]/div/input'
# 添加缴费--提交
addPaySubmit = By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[2]/button[1]/span'
# 审批订单--财务管理菜单
approveManagement = By.XPATH, '//*[@id="app"]/section/aside/ul/li[4]/div/span'
# 审批订单--订单列表
approveOrderList = By.XPATH, '//*[@id="app"]/section/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr/td[4]'
# 审批订单--指定姓名的订单审批
# index = 0
# approveButton = By.XPATH, '//*[@id="app"]/section/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr[%d]/td[' \
#                          '17]/div/span' % index
# 审批订单--学员姓名
approveStudentName = By.CSS_SELECTOR, "[placeholder$='姓名']"
# 审批订单--搜索按钮
approveSearchButton = By.XPATH, "//*[text()='查询']"
# 审批订单--审批按钮
approveButton = By.XPATH, '//*[@id="app"]/section/section/main/div/div[3]/div[1]/div[3]/table/tbody/tr/td[17]/div/span'
# 审批订单--审批通过按钮
approveButton2 = By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/button[1]'
