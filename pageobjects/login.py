from selenium.webdriver.common.by import By


class Login:
    username_ID_txtbox = "loginusername"
    password_ID_txtbox = "loginpassword"
    Login_XPATH_button = "//button[normalize-space()='Log in']"

    def __init__(self, driver):
        self.driver = driver

    def login_username(self, Luser):
        self.driver.find_element(By.ID, self.username_ID_txtbox).send_keys(Luser)

    def login_password(self, Lpwd):
        self.driver.find_element(By.ID, self.password_ID_txtbox).send_keys(Lpwd)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.Login_XPATH_button).click()


