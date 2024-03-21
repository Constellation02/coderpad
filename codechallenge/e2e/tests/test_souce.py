import unittest
from selenium import webdriver
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.souce import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_information_page import CheckoutInformationPage
from pages.checkout_complete_page import CheckoutCompletePage


class SauceDemoLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        print("Page loaded")

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("standard_user")
        print("Login successful")
        login_page.enter_password("secret_sauce")
        print("password successful")
        login_page.click_login()

        products_page = ProductsPage(self.driver)
        products_page.add_product_to_cart('sauce-labs-backpack')
        products_page.add_product_to_cart('sauce-labs-bike-light')

        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
    
        checkout_info_page = CheckoutInformationPage(self.driver)
        checkout_info_page.fill_in_purchase_form('Test', 'User', '12345')
        
        checkout_overview_page = CheckoutOverviewPage(self.driver)
        checkout_overview_page.finish_purchase()
        
        checkout_complete_page = CheckoutCompletePage(self.driver)
        thank_you_text = checkout_complete_page.get_thank_you_message_text()
        self.assertIn("Thank you for your order!", thank_you_text)
        
        

    def tearDown(self):
        self.driver.quit()

