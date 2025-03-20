import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up headless Chrome for GitHub Actions
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # No GUI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
driver = webdriver.Chrome(options=options)
driver.get("https://bloxd.io/play/classic/ohio-state")
time.sleep(5)  # Wait for page to load

# Find the game canvas (this prevents clicking outside the window)
canvas = driver.find_element(By.TAG_NAME, "body")

# Control loop
while True:
    canvas.send_keys(Keys.W)  # Move forward
    time.sleep(2)
    canvas.send_keys(Keys.SPACE)  # Jump
    time.sleep(2)

    # Send a chat message every 5 minutes
    canvas.send_keys(Keys.ENTER)  # Open chat
    time.sleep(1)
    canvas.send_keys("Welcome to the server!")  # Type message
    canvas.send_keys(Keys.ENTER)  # Sen
