from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3660142320&f_LF=f_AL&geoId=102257491&"
           "keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in = driver.find_element(By.CLASS_NAME, value="nav__button-secondary")
sign_in.click()

username = driver.find_element(By.CSS_SELECTOR, value="#username")
username.send_keys("jonasadjintettey@gmail.com")

password = driver.find_element(By.CSS_SELECTOR, value="#password")
password.send_keys("Niiadu1@!")

login = driver.find_element(By.CSS_SELECTOR, value="div button")
login.click()

easy_apply = driver.find_element(By.CSS_SELECTOR, value="div button")
easy_apply.click()

phone_number = driver.find_element(By.CLASS_NAME, value="artdeco-text-input--input")
phone_number.send_keys("269485755")

first_next = driver.find_element(By.CSS_SELECTOR, value="div button")
first_next.click()

second_next = driver.find_element(By.CSS_SELECTOR, value="#ember526")
second_next.click()

third_next = driver.find_element(By.CSS_SELECTOR, value="#ember553")
third_next.click()

forth_next = driver.find_element(By.CSS_SELECTOR, value="#ember553")
forth_next.click()

review = driver.find_element(By.CSS_SELECTOR, value="#ember582")
review.click()
