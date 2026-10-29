from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = 'https://www.saucedemo.com/'
WAIT_SECONDS = 12


def test_invalid_credentials_show_validation_message(driver):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, WAIT_SECONDS)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="username"]'))).send_keys('wrong_user')
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys('wrong_password')
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()

    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]')))
    assert 'Username and password do not match' in error.text
