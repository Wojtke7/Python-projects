from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

timeout = time.time() + 5*60
last_checked = time.time()

dirver = webdriver.Chrome()
dirver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_button = dirver.find_element(by=By.XPATH, value='//*[@id="cookie"]')
# store = dirver.find_element(by=By.ID, value="store")
# boosts = store.find_elements(by=By.CSS_SELECTOR, value="b")
# for boost in boosts[:-1]:
#    print(boost.text.split("-")[1])

while True:
    cookie_button.click()

    if time.time() > timeout:
        break

    if time.time() - last_checked >= 5:

        cookies_number = dirver.find_element(by=By.XPATH, value='//*[@id="money"]').text
        print(f"Number of cookies earned: {cookies_number}")

        store = dirver.find_element(by=By.ID, value="store")
        boosts = store.find_elements(by=By.CSS_SELECTOR, value="b")
        boosts.reverse()

        for boost in boosts[1:]:
           # print(boost.text.split("-")[1])
           # print(cookies_number.replace(",", ""))

            if int(boost.text.split("-")[1].replace(",", "").strip()) < int(cookies_number.replace(",", "")):
                print(f"Choosed boost is {boost.text}")
                boost.click()
                break

        print("Checking")
        last_checked = time.time()

dirver.quit()
