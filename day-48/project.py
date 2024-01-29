from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
cursor = driver.find_element(By.ID, value="cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5   # 5 minutes

while True:
    # time.sleep(0.1)
    cursor.click()

    if time.time() > timeout:

        money = driver.find_element(By.ID, value="money")
        my_money = int(money.text.replace(",", ""))

        buy_time_machine = driver.find_element(By.ID, value="buyTime machine")
        time_machine_price = int(buy_time_machine.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        buy_portal = driver.find_element(By.ID, value="buyPortal")
        portal_price = int(buy_portal.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        alchemy_lab = driver.find_element(By.ID, value="buyAlchemy lab")
        alchemy_lab_price = int(alchemy_lab.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        buy_shipment = driver.find_element(By.ID, value="buyShipment")
        shipment_price = int(buy_shipment.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        buy_mine = driver.find_element(By.ID, value="buyMine")
        mine_price = int(buy_mine.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        buy_factory = driver.find_element(By.ID, value="buyFactory")
        factory_price = int(buy_factory.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        buy_grandma = driver.find_element(By.ID, value="buyGrandma")
        grandma_price = int(buy_grandma.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        buy_cursor = driver.find_element(By.ID, value="buyCursor")
        cursor_price = int(buy_cursor.text.split("-")[1].split("\n")[0].strip().replace(",", ""))

        if my_money >= time_machine_price:
            buy_time_machine.click()
        elif my_money >= portal_price:
            buy_portal.click()
        elif my_money >= alchemy_lab_price:
            alchemy_lab.click()
        elif my_money >= shipment_price:
            buy_shipment.click()
        elif my_money >= mine_price:
            buy_mine.click()
        elif my_money >= factory_price:
            buy_factory.click()
        elif my_money >= grandma_price:
            buy_grandma.click()
        elif my_money >= cursor_price:
            buy_cursor.click()

        timeout = time.time() + 5

    # after 5 minutes stop the bot and check the cookies per second count
    if time.time() > five_min:
        cookies_per_second = driver.find_element(By.ID, value="cps").text
        print(cookies_per_second)
        break



