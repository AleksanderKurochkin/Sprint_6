from selenium.webdriver.common.by import By

class MainPageLocators:

    QUESTION = By.XPATH, "//div[@aria-controls='accordion__panel-{}']"
    ANSWER = By.XPATH, "//div[@aria-labelledby='accordion__heading-{}']"
    BUTTON_ORDER_HIGH = By.XPATH, "//button[@class='Button_Button__ra12g']"
    BUTTON_ORDER_LOWER = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"
