import time
from pageobjects.homepage import Homepage
from pageobjects.signup import signup
from utilities.readproperties import ReadConfig

class TestMainPage:

    baseURL = ReadConfig.getApplicationURL()
    suser = ReadConfig.signupusername()
    spwd = ReadConfig.signuppassword()

    def test_001(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.hp = Homepage(self.driver)
        self.hp.signup()

        self.reg = signup(self.driver)
        self.reg.signup_username(self.suser)
        self.reg.signup_password(self.spwd)
        self.reg.signup_button()



