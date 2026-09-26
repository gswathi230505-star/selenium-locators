from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get("https://www.zepto.com/")

driver.maximize_window()

time.sleep(10)

print(driver.title)
print(driver.current_url)
sweet = driver.find_element(
    By.XPATH, "//img[@alt='Sweet Cravings']"
)

sweet.click()
time.sleep(3)
product = driver.find_element(
    By.XPATH,
    "//img[@alt='Kinder Joy Blue | Chocolate | Assorted']"
)
product.click()
time.sleep(3)

add_cart = driver.find_element(
    By.XPATH,
    "//button[text()='Add to Cart']"
)
add_cart.click()
time.sleep(3)