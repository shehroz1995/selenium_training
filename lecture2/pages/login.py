from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        login_link_elem = self.driver.find_element_by_css_selector('#page > header > div > div > div > div.js-edx-header-ui.edx-header-ui > nav > a:nth-child(1)')
        login_link_elem.click()

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
        return True


    def fill_form(self):
        email_elem = self.driver.find_element_by_css_selector('#login-email')
        email_elem.send_keys("m.shehroz@arbisoft.com")
        #Find and fill the password field
        pwd_elem = self.driver.find_element_by_css_selector('#login-password')
        pwd_elem.send_keys('iamsecure4')

    def submit_form(self):
        subnit_elem = self.driver.find_element_by_css_selector('button[type="submit"]')
        subnit_elem.click()