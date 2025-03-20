import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up a headless browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Runs in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Open the game in Chrome
driver = webdriver.Chrome(options=options)
driver.get("https://bloxd.io/play/classic/ohio-state")
time.sleep(5)  # Wait for game to load

# Click inside the game to focus
webdriver.ActionChains(driver).move_by_offset(500, 500).click().perform()

# Simulate movement (walk forward and jump)
body = driver.find_element("tag name", "body")

while True:
    body.send_keys(Keys.W)  # Walk forward
    time.sleep(2)
    body.send_keys(Keys.SPACE)  # Jump
    time.sleep(2)

    # Send a chat message every 5 minutes
    body.send_keys(Keys.ENTER)  # Open chat
    time.sleep(1)
    body.send_keys("Welcome to the server!")  # Type message
    body.send_keys(Keys.ENTER)  # Send message
    time.sleep(300)  # Wait 5 minutes
