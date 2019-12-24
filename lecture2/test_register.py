import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.register import RegisterPage
from pages.Dashboard import DashboardPage

class EdxRegister(unittest.TestCase):

    def setUp(self):
        #Initialize webdriver
        self.driver = webdriver.Chrome("C:\Shehroz\Softwares\Dev Tools\chromedriver_win32\chromedriver.exe")
        self.register = RegisterPage(self.driver)
        self.dashboard = DashboardPage(self.driver)

    def test_login(self):
        # Open the target page
        self.driver.get('https://stage.edx.org/register')
        # Assert that 'edX' is present in browser title
        self.assertTrue(self.register.is_browser_on_the_page())
        # Find and fill the email field
        self.register.fill_form()
        # Find and click the submit button
        self.register.submit_form()
        # Assert that 'Dashboard' is present in target pages browser title
        self.dashboard.is_browser_on_the_page()

    # def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()