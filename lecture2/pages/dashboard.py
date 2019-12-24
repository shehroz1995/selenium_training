from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DashboardPage(object):

    def __init__(self, driver):
        self.driver = driver

    def is_browser_on_the_page(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#course-title-course-v1\:PennX\+SD4x\+3T2019 > a')))
        return True