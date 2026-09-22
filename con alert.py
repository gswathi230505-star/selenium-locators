from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Edge()
driver.get("https://www.hyrtutorials.com/p/alertsdemo.html")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.ID,"confirmBox").click()
time.sleep(3)
alert = driver.switch_to.alert
print("Alert Message:",alert.text)
time.sleep(3)
alert.accept()
time.sleep(3)
driver.quit()