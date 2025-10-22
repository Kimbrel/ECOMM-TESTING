from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

VALID_USERNAME = "standard_user"
VALID_PASSWORD = "secret_sauce"

def test_e2e_add_item_to_cart_and_verify(driver):
    # 1. Initialize Pages
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    # 2. Login (Prerequisite)
    login_page.navigate_to_login()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    
    # Assertion to ensure successful login before proceeding
    assert home_page.is_logged_in(), "Login failed: could not reach the home page."

    # 3. Add Item to Cart
    initial_cart_count = home_page.get_cart_count()
    assert initial_cart_count == 0, "Cart was not empty before starting the test."
    
    home_page.add_item_to_cart()
    
    # 4. Verification (Cart Count)
    new_cart_count = home_page.get_cart_count()
    assert new_cart_count == 1, f"Expected cart count to be 1, but found {new_cart_count}"
    
    # 5. Navigate and Final Verification (Optional deeper verification)
    home_page.navigate_to_cart()
    assert "cart.html" in driver.current_url
    
    # Check that the item added is displayed in the cart page
    cart_item_name_locator = (By.CLASS_NAME, "inventory_item_name")
    cart_item_name = home_page.find_element(cart_item_name_locator).text
    # Note: The item added is the first one, which is typically the 'Sauce Labs Backpack'
    assert "Sauce Labs" in cart_item_name, "Item name verification failed in the cart."