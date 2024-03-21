from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.XPATH, "//button[@id='finish']")

    def finish_purchase(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.finish_button)).click()
