import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(3)

search=driver.find_element(By.ID,'name')
search.send_keys('swathi')
time.sleep(3)

search=driver.find_element(By.CLASS_NAME,'form-control')
search.send_keys('swathi@gmail.com')
time.sleep(3)

search=driver.find_element(By.XPATH,'//input[@maxlength="10"]')
search.send_keys('4330489202')
time.sleep(3)

search=driver.find_element(By.ID,'country')
search.send_keys('India')
time.sleep(3)


search=driver.find_element(By.XPATH,'//input[@id="male"]')
search.send_keys('Male')
time.sleep(3)

search=driver.find_element(By.XPATH,'//input[@value="sunday"]')
search.send_keys('Sunday')
time.sleep(3)

button = driver.find_element(By.CLASS_NAME, "submit-btn")
button.click()
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Home")
link.click()
time.sleep(3)

search=driver.find_element(By.CSS_SELECTOR,"#datepicker")
search.send_keys('05/23/2005')
time.sleep(3)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Udemy Courses")
link.click()
time.sleep(3)
