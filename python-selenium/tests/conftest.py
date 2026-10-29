import pytest
from pathlib import Path
from selenium import webdriver

ARTIFACTS = Path(__file__).parent.parent / 'artifacts'

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1440, 1000)
    yield browser
    browser.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        browser = item.funcargs.get('driver')
        if browser:
            ARTIFACTS.mkdir(exist_ok=True)
            browser.save_screenshot(str(ARTIFACTS / f'{item.name}.png'))
