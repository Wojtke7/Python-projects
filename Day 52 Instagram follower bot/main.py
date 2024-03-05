from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

LOGIN = "username"
PASSWORD = "pass#"
ACCOUNT = "cookiesbydesign"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(4)
try:
    cookie_button = driver.find_element(by=By.CSS_SELECTOR, value='._a9_0')
    cookie_button.click()
    print("Cookie button clicked")
except NoSuchElementException:
    print("No cookies popup")

time.sleep(3)

username_input = driver.find_element(by=By.NAME, value="username")
username_input.send_keys(LOGIN)

password_input = driver.find_element(by=By.NAME, value="password")
password_input.send_keys(PASSWORD)

log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
log_in_button.click()
time.sleep(10)

search_button = driver.find_element(by=By.XPATH,
                                    value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a')
search_button.click()
time.sleep(6)

search_input = driver.find_element(by=By.XPATH,
                                   value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
search_input.send_keys(ACCOUNT)
time.sleep(4)

accounts_div = driver.find_element(by=By.XPATH,
                                   value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div')
target_acc = accounts_div.find_element(by=By.TAG_NAME, value="a")
print(target_acc.text)
target_acc.click()
time.sleep(5)

followers_amount = driver.find_element(by=By.XPATH,
                                       value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers_amount.click()
time.sleep(7)

dialog_window = driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div')
buttons = dialog_window.find_elements(by=By.CSS_SELECTOR, value='._acan')

i = 0
for button in buttons:
#    print(button.text)
    button.click()
    if i == 50:
        break
    i += 1
    time.sleep(1)
