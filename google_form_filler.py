from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GoogleFormFiller:
    _chrome_options = webdriver.ChromeOptions()
    _chrome_options.add_experimental_option("detach", True)

    def __init__(self, url: str):
        self.driver = webdriver.Chrome(options=GoogleFormFiller._chrome_options)
        self.driver.get(url)


    def enter_data_into_form(self, data_set):
        """Enters the data set argument into the Google Form fields"""
        for rent_property in data_set:
            address_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            rent_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            url_field = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

            address_field.send_keys(rent_property['address'])
            rent_field.send_keys(rent_property['price'])
            url_field.send_keys(rent_property['url'])
            submit_button.click()

            self.driver.find_element(By.LINK_TEXT, 'Submit another response').click()
            time.sleep(1)

