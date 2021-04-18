from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriver_path =r"your chromedriver path"
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_css_selector("#cookie")
timeout = time.time() + 5
five_min = time.time() + 60*5

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

while True:
    cookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector('#store b')
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        timeout = time.time() + 5

        




