import time
import page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from selenium.webdriver.support.ui import Select
import random


class Base:

    def __init__(self, driver):
        # log.info("[base]: 正在获取初始化driver对象:{}".format(driver))
        self.driver = driver

    # 查找元素方法
    def base_find(self, loc, timeout=20, poll=1):
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入元素
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        # 输入
        el.send_keys(value)

    # 获取文本信息
    def base_get_text(self, loc):
        return self.base_find(loc).text

    # 获取一组文本信息
    def base_get_texts(self, loc, target):
        ele = self.base_find_elements(loc)
        for i in ele:
            if i.text == target:
                return ele.index(i)


    # 截图
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 判断元素是否存在
    def base_element_is_exist(self, loc):
        try:
            self.base_find_elements(loc, timeout=2)
            return True  # 代表元素存在
        except:
            return False  # 代表元素不存在

    # 鼠标悬停操作
    def base_mouse_action_chains(self, loc):
        ActionChains(self.driver).move_to_element(self.base_find(loc)).perform()

    # 回到登录页
    def base_index(self):
        self.driver.get(page.URL)

    # 切换frame表单方法
    def base_switch_frame(self, name):
        self.driver.switch_to.frame(name)

    # 回到默认目录方法
    def base_default_content(self):
        self.driver.switch_to.default_content()

    # 切换窗口 方法 调用此方法
    def base_switch_to_window(self, title):
        # log.info("正在执行切换title值为：{}窗口 ".format(title))
        self.driver.switch_to.window(self.base_get_title_handle(title))

    # 获取指定title页面的handle方法
    def base_get_title_handle(self, title):
        # 获取当前页面所有的handles
        for handle in self.driver.window_handles:
            # log.info("正在遍历handles：{}-->{}".format(handle, self.driver.window_handles))
            # 切换 handle
            self.driver.switch_to.window(handle)
            # log.info("切换 :{} 窗口".format(handle))
            # 获取当前页面title 并判断 是否等于 指定参数title
            # log.info("判断当前页面title:{} 是否等于指定的title:{}".format(self.driver.title, title))
            if self.driver.title == title:
                # log.info("条件成立！ 返回当前handle{}".format(handle))
                # 返回 handle
                return handle

    # 页面刷新
    def base_refresh(self):
        self.driver.refresh()

    # 强制等待
    @staticmethod
    def base_wait(num):
        time.sleep(num)

    # 随机生成名字
    def base_random_name(self):
        return Faker(locale='zh_CN').name()

    # 随机生成地址
    def base_random_address(self):
        return Faker(locale='zh_CN').address()

    # 定位一组元素
    def base_find_elements(self, loc, timeout=20, poll=1):
        # 使用显示等待 查找元素
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 定位下拉框 select标签
    def base_select(self, loc, visible_text, value, index=1, locationType=1):  # 1:index 2:value 3:visible_text
        if locationType == 1:
            return Select(self.base_find(loc)).select_by_index(index)
        elif locationType == 2:
            return Select(self.base_find(loc)).select_by_value(value)
        else:
            return Select(self.base_find(loc)).select_by_visible_text(visible_text)

    # 非select标签的下拉框定位
    def base_is_not_select(self, loc, ele):
        self.base_click(loc)
        time.sleep(1)
        if self.base_element_is_exist(ele):
            if len(self.base_find_elements(ele)) > 1:
                self.base_find_elements(ele)[random.randint(1, len(self.base_find_elements(ele)) - 1)].click()
            else:
                self.base_find_elements(ele)[random.randint(0, len(self.base_find_elements(ele)) - 1)].click()
        else:
            self.base_wait(1)
            if len(self.base_find_elements(ele)) > 1:
                self.base_find_elements(ele)[random.randint(1, len(self.base_find_elements(ele)) - 1)].click()
            else:
                self.base_find_elements(ele)[random.randint(0, len(self.base_find_elements(ele)) - 1)].click()

    # 生成随机年月日
    def base_random_date(self):
        return Faker().date()

    # 随机生成身份证号
    def base_random_identity(self):
        return Faker(locale='zh_CN').ssn()

    # 随机生成姓名
    def base_random_name(self):
        return Faker(locale='zh_CN').name()

    # 随机生成手机号
    def base_random_phone(self):
        return Faker(locale='zh_CN').phone_number()

    # 随机选择单选框
    def base_click_radio_button(self, loc):
        self.base_find_elements(loc)[random.randint(0, (len(self.base_find_elements(loc))
                                                        - 1))].click()

    def base_random_num(self):
        return random.randint(1, 1000)

