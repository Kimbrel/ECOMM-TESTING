import pytest
import json
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

# Helper to load data from the JSON file
def load_test_data(filename):
    with open(f"test_data/{filename}", 'r') as f:
        return json.load(f)

# Pytest Parameterization for Data-Driven Testing
@pytest.mark.parametrize("user_data", load_test_data("login_creds.json"))
def test_user_login(driver, user_data):
    login_page = LoginPage(driver)
    login_page.navigate_to_login()
    
    login_page.login(user_data['username'], user_data['password'])
    
    if user_data['expected_result'] == "success":
        # Assert successful login (e.g., check for a specific URL or element)
        assert "/inventory.html" in driver.current_url
        
    elif user_data['expected_result'] == "failure":
        # Assert failure (e.g., check for the error message element)
        error_element = login_page.find_element(login_page.ERROR_MESSAGE)
        assert error_element.is_displayed()