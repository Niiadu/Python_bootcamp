from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cursor = driver.find_element(By.ID, value="cookie")

all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
for price in all_prices:
    print(price.text)