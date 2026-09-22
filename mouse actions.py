from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Edge()
driver.get("https://vinothqaacademy.com/mouse-event/")
driver.maximize_window()
time.sleep(3)
element = driver.find_element(By.ID, "doubleBtn")
actions = ActionChains(driver)
actions.double_click(element).perform()
time.sleep(3)

element = driver.find_element(By.ID, "rightBtn")
actions = ActionChains(driver)
actions.context_click(element).perform()
time.sleep(3)

source = driver.find_element(By.ID, "dragItem")
target = driver.find_element(By.ID, "dropZone")
actions.drag_and_drop(source, target).perform()
driver.quit()