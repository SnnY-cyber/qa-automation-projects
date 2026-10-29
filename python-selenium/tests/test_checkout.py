from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = 'https://www.saucedemo.com/'
WAIT_SECONDS = 30

def sign_in(driver, username='standard_user', password='secret_sauce'):
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, WAIT_SECONDS)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="username"]'))).send_keys(username)
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()
    return wait

def test_standard_user_completes_checkout(driver):
    wait = sign_in(driver)
    wait.until(EC.url_contains('inventory.html'))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]'))).click()
    badge = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    wait.until(EC.text_to_be_present_in_element(badge, '1'))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'))).click()
    wait.until(EC.url_contains('cart.html'))
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="checkout"]'))).click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="firstName"]'))).send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys('Engineer')
    driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys('06000')
    driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="finish"]'))).click()
    confirmation = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="complete-header"]')))
    assert confirmation.text == 'Thank you for your order!'

def test_invalid_credentials_show_validation_message(driver):
    wait = sign_in(driver, username='wrong_user', password='wrong_password')
    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]')))
    assert 'Username and password do not match' in error.text
