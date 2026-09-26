import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Open Chrome
driver = webdriver.Chrome()

# Open website
driver.get("https://www.tutorialspoint.com/selenium/practice/webtables.php")

# Maximize browser
driver.maximize_window()


# Locate table
table = driver.find_element(By.TAG_NAME, "table")


# Find row count
row_count = len(
    driver.find_elements(By.XPATH, "//table/tbody/tr")
)


# Find column count
col_count = len(
    driver.find_elements(By.XPATH, "//table/thead/tr/th")
)


# Print row and column count
print("Rows:", row_count)
print("Columns:", col_count)


# Get all rows
rows = table.find_elements(
    By.XPATH, ".//tbody/tr"
)


print("Total Rows:", len(rows))


# Loop through rows
for row in rows:

    cols = row.find_elements(
        By.TAG_NAME, "td"
    )

    for col in cols:
        print(col.text, "|", end=" ")

    print()
time.sleep(5)

# Close browser
driver.quit()