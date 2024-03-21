from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver
        self.thank_you_message = (By.CLASS_NAME, 'complete-header')

    def get_thank_you_message_text(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.thank_you_message)).text
