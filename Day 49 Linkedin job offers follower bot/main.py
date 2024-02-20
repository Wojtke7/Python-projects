from selenium import webdriver
from selenium.webdriver.common.by import By
import time

passwd = "lol123passwd"
mail = "wojciechmarcela7@gmail.com"

url = "https://www.linkedin.com/jobs/search/?currentJobId=3829879442&f_AL=true&f_E=2&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER"
# url2 = "https://www.linkedin.com/jobs/search/?currentJobId=3813713952&f_AL=true&f_E=1&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER"
chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_settings)
driver.get(url)

log_in_button = driver.find_element(by=By.XPATH, value='/html/body/div[3]/header/nav/div/a[2]')
log_in_button.click()
time.sleep(5)

username_input = driver.find_element(by=By.ID, value="username")
username_input.send_keys(mail)
time.sleep(1)

password_input = driver.find_element(by=By.ID, value="password")
password_input.send_keys(passwd)
time.sleep(1)

log_in_button2 = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
log_in_button2.click()

time.sleep(5)
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
    save_button.click()
    time.sleep(2)
