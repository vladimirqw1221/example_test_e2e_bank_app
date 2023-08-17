from selenium import webdriver

from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture(scope='class', autouse=True)
def driver(request):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=2560,1600")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage ")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument('--disable-extensions')



    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver

    yield driver

    driver.quit()
