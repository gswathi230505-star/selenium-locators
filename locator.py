import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)



search=driver.find_element(By.TAG_NAME,'input')
search.send_keys('swathi')
time.sleep(3)

search=driver.find_element(By.ID,'email')
search.send_keys('swathi@gmail.com')
time.sleep(3)


search=driver.find_element(By.XPATH,'//input[@maxlength="10"]')
search.send_keys('9048984789')
time.sleep(3)


search=driver.find_element(By.CSS_SELECTOR,'#textarea')
search.send_keys('Madurai')
time.sleep(3)



search=driver.find_element(By.XPATH,'//input[@id="male"]')
search.send_keys('Male')
time.sleep(3)