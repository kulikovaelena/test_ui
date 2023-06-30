from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"


driver.get(URL)

input_username = driver.find_element(By.ID, "user-name")
input_password = driver.find_element(By.ID, "password")
input_username.send_keys(USERNAME)
input_password.send_keys(PASSWORD)

register_button = driver.find_element(By.ID, "login-button")
register_button.click()
