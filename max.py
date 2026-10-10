
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.maxfashion.in/in/en/")

wait = WebDriverWait(driver, 20)
time.sleep(3)

# Wait for the search box and enter the keyword
search = wait.until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "input[type='search']")
    )
)

search.send_keys("Womens Kurtas")
search.send_keys(Keys.ENTER)
time.sleep(10)

wait.until(
    EC.presence_of_element_located((By.ID, "product-1"))
)

# Locate all products
products = driver.find_elements(By.CSS_SELECTOR, "div[id^='product-']")

# Print total number of products
print("Number of products displayed:", len(products))

# Print first 5 products using index only
print("Product 1:", products[0].text)
print("Product 2:", products[1].text)
print("Product 3:", products[2].text)
print("Product 4:", products[3].text)
print("Product 5:", products[4].text)
time.sleep(5)

search = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "product-1000016776915-Red-RED")
    )
)
print("Product Page:",driver.title)
search.click()
time.sleep(8)


wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//*[normalize-space()='Size:']")
    )
)

# Locate size M (change M to S, L, XL, or XXL if needed)
size = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='details-size']/div/div[3]/div/div[2]/button")
    )
)
# Click the size
size.click()
print("Selected size:", size.text)

time.sleep(6)
driver.quit()
