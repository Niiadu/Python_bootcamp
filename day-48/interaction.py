from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")

# data = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# data.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Jonas")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Tettey")

email = driver.find_element(By.NAME, value="email")
email.send_keys("jonas@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.send_keys(Keys.ENTER)

# driver.quit()