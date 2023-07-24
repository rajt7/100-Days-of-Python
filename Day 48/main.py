from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.python.org/")

upcoming_events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
event_times = upcoming_events.find_elements(By.TAG_NAME, "time")
event_names = upcoming_events.find_elements(By.TAG_NAME, "a")

upcoming_events_dict = {}

for i, (time, name) in enumerate(zip(event_times, event_names)):
    upcoming_events_dict[i] = {
        'time': time.text,
        'name': name.text
    }

print(upcoming_events_dict)
