import time
from pageobjects.homepage import Homepage
from pageobjects.signup import signup


class TestMainPage:

    base_url = "https://www.demoblaze.com/"
    user = "swa1234"
    pwd = "swa1234"

    def test_001(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.hp = Homepage(self.driver)
        self.hp.signup()

        self.reg = signup(self.driver)
        self.reg.signup_username(self.user)
        self.reg.signup_password(self.pwd)
        self.reg.signup_button()



