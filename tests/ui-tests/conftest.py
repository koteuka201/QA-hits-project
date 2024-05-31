import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

HEADLESS=False

BASE_URL="http://127.0.0.1:5000/"

@pytest.fixture
def browser():
    option = ChromeOptions()
    if HEADLESS:
        option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-gpu')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('--disable-infobars')

    driver = webdriver.Chrome(options=option)
    driver.maximize_window()
    driver.implicitly_wait(2)
    driver.get(BASE_URL)

    yield driver

    driver.quit()