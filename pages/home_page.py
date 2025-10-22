from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    # Locators
    PRODUCTS_HEADER = (By.CLASS_NAME, "product_label")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_primary") # Used for any product
    CART_ICON = (By.ID, "shopping_cart_container")
    REMOVE_BUTTON = (By.CLASS_NAME, "btn_secondary")
    
    # Specific locators for demo product
    SAUCE_LABS_BACKPACK = (By.XPATH, "//div[text()='Sauce Labs Backpack']")
    
    def is_logged_in(self):
        """Verifies if the user is successfully on the product page."""
        # Checks for the 'Products' header
        return self.find_element(self.PRODUCTS_HEADER).is_displayed()

    def add_item_to_cart(self):
        """Adds the first available item to the shopping cart."""
        # Find the first 'Add to Cart' button and click it
        self.find_element(self.ADD_TO_CART_BUTTON).click()

    def get_cart_count(self):
        """Returns the number of items currently in the cart."""
        # Check for the number displayed next to the cart icon
        try:
            cart_badge = self.find_element((By.CLASS_NAME, "shopping_cart_badge"))
            return int(cart_badge.text)
        except:
            return 0

    def navigate_to_cart(self):
        """Clicks the shopping cart icon to view the cart."""
        self.click(self.CART_ICON)