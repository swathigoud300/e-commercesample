from selenium.webdriver.common.by import By


class signup:
    username_ID_txtbox = "sign-username"
    password_ID_txtbox = "sign-password"
    signup_XPATH_button = "//button[@onclick='register()']"

    def __init__(self, driver):
        self.driver = driver

    def signup_username(self, user):
        self.driver.find_element(By.ID, self.username_ID_txtbox).send_keys(user)

    def signup_password(self, pwd):
        self.driver.find_element(By.ID, self.password_ID_txtbox).send_keys(pwd)

    def signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_XPATH_button).click()
