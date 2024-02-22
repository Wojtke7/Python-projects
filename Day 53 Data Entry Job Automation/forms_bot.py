from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SHEET_URL = "https://docs.google.com/forms/d/e/1FAIpQLScyypl_2y-7VvguQzlE8uh3AN-9NMOoeGQWknpF9VWvxnh9qg/viewform?usp=sf_link"


class FormsBot:

    def __init__(self):
        self.url = SHEET_URL

    def set_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url=self.url)

        return driver

    def fill_form(self, property_addresses, property_prices, property_links):
        driver = self.set_driver()

        for i in range(0, len(property_addresses)):
            time.sleep(7)
            adress_input = driver.find_element(by=By.XPATH,
                                               value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_input = driver.find_element(by=By.XPATH,
                                              value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_input = driver.find_element(by=By.XPATH,
                                             value='/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = driver.find_element(by=By.XPATH,
                                                value='/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')
            adress_input.send_keys(property_addresses[i])
            time.sleep(1)
            price_input.send_keys(property_prices[i])
            time.sleep(1)
            link_input.send_keys(property_links[i])
            time.sleep(1)
            submit_button.click()
            time.sleep(7)
            next_answer = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            next_answer.click()
