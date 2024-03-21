from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        # Agrega aquí más localizadores según necesites

    def add_product_to_cart(self, product_id):
        add_button = (By.XPATH, f"//button[contains(@id,'add-to-cart-{product_id}')]")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(add_button)).click()