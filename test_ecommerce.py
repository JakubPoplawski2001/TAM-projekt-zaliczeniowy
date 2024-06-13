from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture()
def setup_and_close():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")

    yield
    driver.quit()

def test_open_site(setup_and_close):
    delay = 2
    time.sleep(delay)

