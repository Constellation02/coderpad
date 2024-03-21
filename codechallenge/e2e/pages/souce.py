from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[contains(@id,'user-name')]")
        self.password_input = (By.XPATH, "//input[contains(@id,'password')]")
        self.login_button = (By.XPATH, "//input[contains(@id,'login-button')]")
        self.product01 = (By.XPATH, "//button[contains(@id,'add-to-cart-sauce-labs-backpack')]")
        self.product02 = (By.XPATH, "//button[contains(@id,'add-to-cart-sauce-labs-bike-light')]")

    def enter_username(self, username):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input)).send_keys(
                username)
        except (NoSuchElementException, TimeoutException):
            print("Error: Username input not found.")
            return False

    def enter_password(self, password):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input)).send_keys(
                password)
        except (NoSuchElementException, TimeoutException):
            print("Error: Password input not found.")
            return False

    def click_login(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()
        except (NoSuchElementException, TimeoutException):
            print("Error: Login button not found.")
            return False
