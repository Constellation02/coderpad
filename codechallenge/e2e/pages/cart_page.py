from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.XPATH, "//a[contains(@class,'shopping_cart_link')]")
        self.checkout_button2 = (By.XPATH, "//button[contains(@id,'checkout')]")

    def click_checkout(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkout_button)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.checkout_button2)).click()
