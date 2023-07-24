from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("abcd")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("efgh")

email = driver.find_element(By.NAME, "email")
email.send_keys("abc@def.com")

signup_btn = driver.find_element(By.TAG_NAME, "button")
signup_btn.click()
