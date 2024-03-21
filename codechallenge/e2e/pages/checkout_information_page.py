from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class CheckoutInformationPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.XPATH, "//input[@id='continue']")

    def fill_in_purchase_form(self, first_name, last_name, postal_code):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.postal_code_input)).send_keys(postal_code)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error filling in purchase form.")
            return False
