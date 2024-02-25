from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.get_attribute("textContent")

    def enter_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)








