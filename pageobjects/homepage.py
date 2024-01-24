from selenium.webdriver.common.by import By


class Homepage:
    Home_XPATH_link = "(//span[@class= 'sr-only'])[1]"
    Contact_XPATH_link = "//a[text()='Contact']"
    About_XPATH_link = "//a[text()='About us']"
    Cart_ID_link = "cartur"
    Login_ID_link = "login2"
    Signup_ID_link = "signin2"

    Next_XPATH_arrow = "//span[@class='carousel-control-next-icon']"



    def __init__(self, driver):
        self.driver = driver

    def home(self):
        self.driver.find_element(By.XPATH, self.Home_XPATH_link).click()

    def contact(self):
        self.driver.find_element(By.XPATH, self.Contact_XPATH_link).click()

    def about(self):
        self.driver.find_element(By.XPATH, self.About_XPATH_link).click()

    def cart(self):
        self.driver.find_element(By.ID, self.Cart_ID_link).click()

    def login(self):
        self.driver.find_element(By.ID, self.Login_ID_link).click()

    def signup(self):
        self.driver.find_element(By.ID, self.Signup_ID_link).click()


    def click_next_arrow(self):
        self.driver.find_element(By.XPATH, self.Next_XPATH_arrow).click()



