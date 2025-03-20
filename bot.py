import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Set up headless Chrome for GitHub Actions
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # No GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://bloxd.io/play/classic/ohio-state")
time.sleep(5)  # Wait for page to load

# Simulate small movements to avoid AFK kick
actions = ActionChains(driver)
while True:
    actions.move_by_offset(5, 5).perform()  # Move mouse a little
    time.sleep(2)
    actions.move_by_offset(-5, -5).perform()  # Move back
    time.sleep(2)
