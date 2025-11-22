from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 1️⃣ Launch Firefox
driver = webdriver.Firefox()

# 2️⃣ Open local HTML page (replace with your full path)
driver.get("file:///home/anil/Desktop/Code/Python/PY/Lib/test_page.html")

time.sleep(1)  # wait for page load

# 3️⃣ Check for dynamic text before clicking
try:
    print("Before clicking:", driver.find_element(By.ID, "newText").text)
except:
    print("Before clicking: No dynamic text yet")

# 4️⃣ Click the button
driver.find_element(By.ID, "btn").click()
time.sleep(1)  # wait for JS to execute

# 5️⃣ Read the dynamically added text
print("After clicking:", driver.find_element(By.ID, "newText").text)

# 6️⃣ Close browser
driver.quit()
