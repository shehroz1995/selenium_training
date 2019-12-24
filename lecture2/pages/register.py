from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class RegisterPage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True
    
    def fill_form(self):
        #Find and fill the email field
        email_elem = self.driver.find_element_by_css_selector('#register-email')
        email_elem.send_keys("m.shehroz+1@arbisoft.com")
        #Find and fill the name field
        name_elem = self.driver.find_element_by_css_selector('#register-name')
        name_elem.send_keys('Muhammad Shehroz Hassan')
        #Find and fill the user name field
        user_name_elem = self.driver.find_element_by_css_selector('#register-username')
        user_name_elem.send_keys('mshehroz')
        #Find and fill the password field
        password_elem = self.driver.find_element_by_css_selector('#register-password')
        password_elem.send_keys('iamsecure4')
        #Find and fill the country name field
        country_elem = Select(self.driver.find_element_by_css_selector('#register-country'))
        country_elem.select_by_visible_text('Pakistan')

    def submit_form(self):
        subnit_elem = self.driver.find_element_by_css_selector('#register > button')
        subnit_elem.click()