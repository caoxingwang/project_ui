from page.page_login import PageLogin
from base.get_driver import GetDriver
from base.base import Base
import page

class Demo(Base):

    def demo(self):
        self.base_click(page.approveManagement)
        index = self.base_get_texts(page.approveOrderList, "孔强")
        print(index)
        page.index = index
        print(page.approveButton)
        self.base_click(page.approveButton)


if __name__ == "__main__":
    p = PageLogin(GetDriver().get_driver())
    p.page_login('lianyouchao', '888888')
    Demo(GetDriver().get_driver()).demo()