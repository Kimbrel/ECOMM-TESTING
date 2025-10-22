import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    
    # Setup phase
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10) 
    driver.maximize_window()
    
    yield driver 
    
 
    driver.quit()