from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://pl.wikipedia.org/wiki/Wikipedia:Strona_g%C5%82%C3%B3wna")

# amountOfArticles = driver.find_element(by=By.XPATH, value='//*[@id="main-page-intro"]/p/a[4]')
# amountOfArticles.click()

# another_good_articles = driver.find_element(by=By.LINK_TEXT, value="Inne Dobre Artykuły")
# another_good_articles.click()

# Find the search <input> by name
# search = driver.find_element(by=By.NAME, value="search")

# Sending keyboard key to selenium
# search.send_keys("Python", Keys.ENTER)
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Wojtek")

last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Marcela")

e_mail = driver.find_element(by=By.NAME, value="email")
e_mail.send_keys("lol@op.pl")

button = driver.find_element(by=By.XPATH, value="/html/body/form/button")
button.send_keys(Keys.ENTER)
