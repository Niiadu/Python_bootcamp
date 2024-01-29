from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.tinder.com")

# time.sleep(5)
# cookies = driver.find_element(By.XPATH, value='//*[@id="s-547617529"]/div/div[2]/div/div/div[1]/div[1]/button')
# cookies.click()

# english = driver.find_element(By.XPATH, value='//*[@id="s2018968691"]/main/div[1]/div[2]/ul/li[1]/a')
# english.click()

time.sleep(3)
# base_window = driver.window_handles[1]
# driver.switch_to.window(base_window)
create_account = driver.find_element(By.XPATH, value='//*[@id="q488047873"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
create_account.click()

time.sleep(5)
facebook = driver.find_element(By.XPATH, value='//*[@id="q-1240333203"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook.click()

login = driver.find_element(By.XPATH, value='//*[@id="q-1240333203"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
login.click()
# base_window = driver.window_handles[1]


base_window = driver.window_handles[0]
facebook_window = driver.window_handles[1]
driver.switch_to.window(facebook_window)
print(driver.title)

email = driver.find_element(By.NAME, value="email")
email.send_keys("jonas@yahoo.com")

password = driver.find_element(By.NAME, value="pass")
password.send_keys("12345")