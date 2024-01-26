import os
import time
from pageobjects.homepage import Homepage
from pageobjects.login import Login
from utilities.readproperties import ReadConfig
from utilities.customlogger import LogGen
from utilities import Excelutils

class Test_login_ddt:
    baseURL = ReadConfig.getApplicationURL()
    path = os.path.abspath(os.curdir)+"\\testdata\\login_data.xlsx"
    Logger = LogGen.loggen()

    def test_003(self, setup):
        self.Logger.info("Testing ddt Login data")
        self.rows = Excelutils.getRowCount(self.path, 'Sheet1')
        lst_status=[]

        self.driver = setup
        self.driver.get(self.baseURL)
        self.Logger.info("Application launching")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = Homepage(self.driver)
        for r in range(2, self.rows+1):

            self.hp.login()
            self.Logger.info("Clicked on login button")

            self.login = Login(self.driver)
            self.Logger.info("Giving credentials")

            self.username = Excelutils.readData(self.path, "Sheet1", r, 1)
            self.password = Excelutils.readData(self.path, "Sheet1", r, 2)
            self.exp = Excelutils.readData(self.path, "Sheet1", r, 3)

            self.login.login_username(self.username)
            self.login.login_password(self.password)
            self.login.login_button()
            self.Logger.info("Successfully logged in")
            time.sleep(5)
            self.targetpage = self.login.click_logout()


        if self.exp == 'Valid':
            if self.targetpage == True:
                lst_status.append('Pass')
                self.login.click_logout()
            else:
                lst_status.append('Fail')
        elif self.exp == 'Invalid':
            if self.targetpage == True:
                lst_status.append('Fail')
                self.login.click_logout()
            else:
                lst_status.append('Pass')
        self.driver.close()
        # final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.Logger.info("******* End of test_003_login_Datadriven **********")





