from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
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
    cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')))
    cart_href = cart_link.get_attribute('href')
    cart_link.click()
    try:
        checkout = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="checkout"]')))
    except TimeoutException as exc:
        page_text = driver.find_element(By.TAG_NAME, 'body').text.replace('\n', ' | ')[:500]
        raise AssertionError(
            f'Cart page did not appear. URL={driver.current_url}; '
            f'cart_link={cart_href}; page={page_text}'
        ) from exc
    cart_item = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-item-name"]')))
    assert cart_item.text == 'Sauce Labs Backpack'
    checkout.click()
    try:
        first_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="firstName"]')))
    except TimeoutException as exc:
        page_text = driver.find_element(By.TAG_NAME, 'body').text.replace('\n', ' | ')[:500]
        raise AssertionError(
            f'Checkout form did not appear. URL={driver.current_url}; '
            f'title={driver.title}; page={page_text}'
        ) from exc
    first_name.send_keys('QA')
    last_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="lastName"]')))
    last_name.send_keys('Engineer')
    postal_code = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="postalCode"]')))
    postal_code.send_keys('06000')
    assert (first_name.get_attribute('value'), last_name.get_attribute('value'), postal_code.get_attribute('value')) == ('QA', 'Engineer', '06000')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="continue"]'))).click()
    try:
        finish = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="finish"]')))
    except TimeoutException as exc:
        page_text = driver.find_element(By.TAG_NAME, 'body').text.replace('\n', ' | ')[:500]
        error_nodes = driver.find_elements(By.CSS_SELECTOR, '[data-test="error"]')
        error_text = error_nodes[0].text if error_nodes else 'none'
        raise AssertionError(
            f'Order overview did not appear. URL={driver.current_url}; '
            f'title={driver.title}; form_values={first_name.get_attribute("value")},'
            f'{last_name.get_attribute("value")},{postal_code.get_attribute("value")}; '
            f'error={error_text}; page={page_text}'
        ) from exc
    finish.click()
    confirmation = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="complete-header"]')))
    assert confirmation.text == 'Thank you for your order!'

def test_invalid_credentials_show_validation_message(driver):
    wait = sign_in(driver, username='wrong_user', password='wrong_password')
    error = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]')))
    assert 'Username and password do not match' in error.text
