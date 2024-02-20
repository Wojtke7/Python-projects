from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_UP = 150
PROMISED_DOWN = 10
TWITTER_EMAIL = "MY MAIL"
TWITTER_PASSWORD = "MY PASS"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = None
        self.up = None
        self.speed_test_driver = "https://www.speedtest.net/pl"
        self.twitter_dirver = "https://twitter.com/home"

    def get_internet_speed(self):
        driver = webdriver.Chrome()
        driver.get(self.speed_test_driver)

        start_button = driver.find_element(by=By.XPATH,
                                           value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        time.sleep(60)

        self.down = driver.find_element(by=By.CSS_SELECTOR, value=".download-speed").text
        self.up = driver.find_element(by=By.CSS_SELECTOR, value=".upload-speed").text

        if int(float(self.down)) < PROMISED_DOWN or int(float(self.up)) < PROMISED_UP:
            return False

    def tweet_at_provider(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(self.twitter_dirver)
        time.sleep(7)

        username_input = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        username_input.send_keys(TWITTER_EMAIL)
        next_button = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        time.sleep(7)

        password_input = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        log_in_button = driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        log_in_button.click()
        time.sleep(7)

        tweet_input = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        tweet_input.send_keys(f"Hey Internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")

        tweet_button = driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]')
        tweet_button.click()


bot = InternetSpeedTwitterBot()
if bot.get_internet_speed() is False:
    bot.tweet_at_provider()
