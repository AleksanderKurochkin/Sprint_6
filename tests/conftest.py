import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope="function")
def browser_firefox():
    #service = Service(executable_path=GeckoDriverManager().install())
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox( options=options)
    driver.set_window_size(1200, 800)
    yield driver
    driver.quit()
