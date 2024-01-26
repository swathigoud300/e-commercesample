from selenium.webdriver.common.by import By


class Login:
    username_ID_txtbox = "loginusername"
    password_ID_txtbox = "loginpassword"
    Login_XPATH_button = "//button[normalize-space()='Log in']"
    nameofuser_LINKTEXT_link = "Welcome swa123"
    Logout_XPATH_link = "//a[@id='logout2']"

    def __init__(self, driver):
        self.driver = driver

    def login_username(self, Luser):
        self.driver.find_element(By.ID, self.username_ID_txtbox).send_keys(Luser)

    def login_password(self, Lpwd):
        self.driver.find_element(By.ID, self.password_ID_txtbox).send_keys(Lpwd)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.Login_XPATH_button).click()

    def nameofuser_link(self):
        self.driver.find_element(By.LINK_TEXT, self.nameofuser_LINKTEXT_link)

    def click_logout(self):
         self.driver.find_element(By.XPATH, self.Logout_XPATH_link).click()

