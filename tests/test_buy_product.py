from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pytest
import time


delay = 3


@pytest.fixture()
def setup_and_close():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://magento.softwaretestingboard.com/")

    yield
    driver.quit()

@pytest.fixture()
def product_page(setup_and_close):
    driver.get("https://magento.softwaretestingboard.com/rival-field-messenger.html")
    yield


def test_search_for_product(setup_and_close):
    product_name = "Rival Field Messenger"

    # Search bar
    search_form = driver.find_element(By.NAME, "q")
    search_form.send_keys(product_name)
    search_form.submit()

    # Product card
    driver.find_element(By.LINK_TEXT, product_name).click()
    # Product page
    title = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/h1/span').text

    assert  title == product_name

def fill_user_credentials(email, f_name, l_name, street, city, zip_code, country, phone):
    # Wait until form is loaded
    wait = WebDriverWait(driver, timeout=5)
    first_name_field = wait.until(EC.element_to_be_clickable((By.NAME, "firstname")))

    # Fill user credentials
    driver.find_element(By.ID, "customer-email").send_keys(email)
    first_name_field.send_keys(f_name)
    driver.find_element(By.NAME, "lastname").send_keys(l_name)
    driver.find_element(By.NAME, "telephone").send_keys(phone)
    # Country selector
    Select(driver.find_element(By.NAME, "country_id")).select_by_value(country)
    # State selector
    Select(driver.find_element(By.NAME, "region_id")).select_by_index(1)
    driver.find_element(By.NAME, "city").send_keys(city)
    driver.find_element(By.NAME, "postcode").send_keys(zip_code)
    driver.find_element(By.NAME, "street[0]").send_keys(street)
    time.sleep(delay)

def test_buy_product(product_page):
    # User credentials
    email = "user@email.not"
    f_name = "User"
    l_name = "Name"
    street = "Street"
    city = "City"
    zip_code = "12-345"
    country = "PL"
    phone = "123456789"

    # Add to Cart btn
    driver.find_element(By.ID, "product-addtocart-button").click()

    # Wait until success alert is shown
    wait = WebDriverWait(driver, timeout=5)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div')))
    time.sleep(0.5)

    # Cart btn
    driver.find_element(By.XPATH, '/html/body/div[2]/header/div[2]/div[1]/a').click()
    # Proceed to Checkout
    driver.find_element(By.ID, "top-cart-btn-checkout").click()

    fill_user_credentials(email, f_name, l_name, street, city, zip_code, country, phone)

    # Next btn
    driver.find_element(By.XPATH, '//*[@id="shipping-method-buttons-container"]/div/button').click()
    time.sleep(delay)

    # Place Order btn
    driver.find_element(
        By.XPATH,
        '//*[@id="checkout-payment-method-load"]/div/div/div[2]/div[2]/div[4]/div/button'
    ).click()

    # Wait until order label is loaded
    order_label = wait.until(EC.presence_of_element_located((
        By.XPATH,
        '//*[@id="maincontent"]/div[3]/div/div[2]/p[1]/span'
    )))

    # Order number
    assert order_label.is_displayed()