from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_list = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events = event_list.find_elements(by=By.TAG_NAME, value="a")
dates = event_list.find_elements(by= By.TAG_NAME, value="time")

# for date in dates:
#    print(date.text)
# for event in events:
#    print(event.text)
events_dict = {}

for n in range(len(events)):
    events_dict[n] = {
        "time": dates[n].text,
        "event": events[n].text
    }

print(events_dict)

driver.quit()
