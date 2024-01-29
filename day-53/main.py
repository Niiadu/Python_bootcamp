from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
app_webpage = response.text

soup = BeautifulSoup(app_webpage, "html.parser")
link = soup.findAll(class_="property-card-link")
# print(link)
listing_link = []
for tags in link:
    listing_link.append(tags.get("href"))
# print(listing_address)

price = soup.findAll(class_="PropertyCardWrapper__StyledPriceLine")
only_price = []
for prices in price:
    only_price.append(prices.getText().split("+")[0].split("/")[0])
# print(only_price)

home_address = soup.findAll(name="address")
address = []
for home in home_address:
    address.append(home.getText().strip().replace("|", ""))
# print(address)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://forms.gle/JwzM3Fwjdd2FzBBJ8")

# for task in range(len(only_price)):
num = 0

while num < len(only_price):
    for task in range(len(only_price)):
        time.sleep(1)
        add_property = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]'
                                                           '/div/div[1]/div/div[1]/input')
        add_property.send_keys(address[task])

        monthly_price = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                            '/div/div[1]/div/div[1]/input')
        monthly_price.send_keys(only_price[task])

        webpage_link = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/'
                                                           'div[2]/div/div[1]/div/div[1]/input')
        webpage_link.send_keys(listing_link[task])

        submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()

        another_request = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_request.click()

        num += 1

