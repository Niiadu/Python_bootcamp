from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep the chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# print(price_dollar.text)

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")

# first_data = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# # data = first_data.text.strip()

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements((By.CSS_SELECTOR), value=".event-widget li a")
events= {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)





# driver.close()
driver.quit()