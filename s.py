import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
driver.maximize_window()
time.sleep(5)