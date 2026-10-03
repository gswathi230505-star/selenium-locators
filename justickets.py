import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

driver.get("https://justickets.in/chennai")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

sigma = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[normalize-space()='Sigma']")
    )
)

# Scroll down until Sigma is visible
driver.execute_script(
    "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    sigma
)

time.sleep(2)
sigma.click()

driver.save_screenshot('booking_page.png')
time.sleep(3)



time.sleep(3)