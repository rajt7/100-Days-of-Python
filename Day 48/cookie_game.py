import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on
cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 5*60

while True:
    cookie.click()

    # After every 5 seconds
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # getting the price of each item
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split('-')[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary to store item and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get the current cookie money
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element.replace(",", "")
        cookie_count = int(money_element)

        # Creating a dictionary of items which are affordable
        affordable_prices = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_prices[cost] = id

        # Purchase the most expensive affordable item
        highest_price_affordable_upgrade = max(affordable_prices)
        to_purchase_id = affordable_prices[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps")
        print(cookie_per_sec)
        break
