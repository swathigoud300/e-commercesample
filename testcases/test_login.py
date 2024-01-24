import time
from pageobjects.homepage import Homepage
from pageobjects.signup import signup
from pageobjects.login import Login


class TestMainPage:

    base_url = "https://www.demoblaze.com/"
    Luser = "swa1234"
    Lpwd = "swa1234"

    def test_002(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.hp = Homepage(self.driver)
        self.hp.login()

        self.login = Login(self.driver)
        self.login.login_username(self.Luser)
        self.login.login_password(self.Lpwd)
        self.login.login_button()
        time.sleep(4)
        self.hp.click_next_arrow()
        time.sleep(3)


