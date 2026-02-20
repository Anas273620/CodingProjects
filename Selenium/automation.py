from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.qaplayground.com/practice")
driver.maximize_window()

print(driver.find_element(By.ID, 'button-clickHold'))


time.sleep(30)