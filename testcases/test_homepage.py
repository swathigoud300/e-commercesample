import time
from pageobjects.homepage import Homepage
from pageobjects.signup import signup
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class TestMainPage:

    baseURL = ReadConfig.getApplicationURL()
    suser = ReadConfig.signupusername()
    spwd = ReadConfig.signuppassword()
    Logger = LogGen.loggen()

    def test_001(self, setup):
        self.Logger.info("***Testing Homepage test case started***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Logger.info("Launching application")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.hp = Homepage(self.driver)
        self.hp.signup()
        self.Logger.info("***clicking on signup***")

        self.reg = signup(self.driver)
        self.Logger.info("***providing details for signup")
        self.reg.signup_username(self.suser)
        self.reg.signup_password(self.spwd)
        self.reg.signup_button()
        self.Logger.info("Sign in successful")



