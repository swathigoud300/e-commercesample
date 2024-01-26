import os
import time
from pageobjects.homepage import Homepage
from pageobjects.signup import signup
from pageobjects.login import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen

class TestMainPage:
    baseURL = ReadConfig.getApplicationURL()
    Luser = ReadConfig.loginuser()
    Lpwd = ReadConfig.loginPassword()
    Logger = LogGen.loggen()

    def test_002(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Logger.info("Application launching")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = Homepage(self.driver)
        self.hp.login()
        self.Logger.info("Clicked on login button")

        self.login = Login(self.driver)
        self.Logger.info("Giving correct credentials")
        self.login.login_username(self.Luser)
        self.login.login_password(self.Lpwd)
        self.login.login_button()
        self.Logger.info("Successfully logged in")
        time.sleep(4)
        self.hp.click_next_arrow()
        time.sleep(3)




