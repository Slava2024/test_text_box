import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(executable_path="./geckodriver")
    yield driver
    driver.quit()
