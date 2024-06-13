from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

delay = 2

@pytest.fixture()
def setup_and_close():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")

    yield
    driver.quit()

def test_search_for_product(setup_and_close):
    product_name = "Rival Field Messenger"

    search_form = driver.find_element(By.NAME, "q")
    search_form.send_keys(product_name)
    search_form.submit()

    driver.find_element(By.LINK_TEXT, product_name).click()
    time.sleep(delay)
    title = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/h1/span').text
    assert  title == product_name

