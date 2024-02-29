import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser_firefox():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox( options=options)
    driver.set_window_size(1200, 800)
    yield driver
    driver.quit()
