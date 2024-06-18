from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


def test_create_existing_account(setup_and_close):
    """
    ! Because of the demo environment this test can fail on first run after website reset
    :param setup_and_close:
    :return:
    """
    # User credentials
    email = "user@email.not"
    f_name = "User"
    l_name = "Name"
    password = "Password1234"

    # Create an Account btn
    driver.find_element(By.LINK_TEXT, "Create an Account").click()

    # Fill user credentials
    driver.find_element(By.NAME, "firstname").send_keys(f_name)
    driver.find_element(By.NAME, "lastname").send_keys(l_name)
    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password_confirmation").send_keys(password)

    # Create Account btn
    driver.find_element(By.XPATH, '//*[@id="form-validate"]/div/div[1]/button').click()

    # Error warning
    wait = WebDriverWait(driver, timeout=5)
    error_alert = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')))
    assert error_alert.is_displayed()

def test_login(setup_and_close):
    # User credentials
    email = "user@email.not"
    password = "Password1234"

    # Sign In btn
    driver.find_element(By.LINK_TEXT, "Sign In").click()

    # Fill user credentials
    driver.find_element(By.NAME, "login[username]").send_keys(email)
    driver.find_element(By.NAME, "login[password]").send_keys(password)

    # Sign In btn
    driver.find_element(By.ID, "send2").click()
    time.sleep(delay)

    # User menu toggle
    user_menu = driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/span/button')
    assert user_menu.is_displayed()

def test_login_with_invalid_password(setup_and_close):
    # User credentials
    email = "user@email.not"
    invalid_password = "InvalidPassword"

    # Sign In btn
    driver.find_element(By.LINK_TEXT, "Sign In").click()

    # Fill user credentials
    driver.find_element(By.NAME, "login[username]").send_keys(email)
    driver.find_element(By.NAME, "login[password]").send_keys(invalid_password)

    # Sign In btn
    driver.find_element(By.ID, "send2").click()
    time.sleep(delay)

    # Error alert
    wait = WebDriverWait(driver, timeout=5)
    error_alert = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="maincontent"]/div[2]/div[2]/div/div/div')))
    assert error_alert.is_displayed()
