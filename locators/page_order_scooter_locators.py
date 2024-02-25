from selenium.webdriver.common.by import By

class PageOrderScooterLocators:
    FIELD_NAME = By.XPATH, '//input[@ placeholder = "* Имя"]'
    FIELD_FIRSTNAME = By.XPATH, '//input[@ placeholder = "* Фамилия"]'
    FIELD_ADDRESS = By.XPATH, '//input[@ placeholder = "* Адрес: куда привезти заказ"]'
    FIELD_METRO = By.XPATH, '//input[@class="select-search__input"]'
    METRO = By.XPATH, "//button[@value='2']"
    FIELD_TELEPHONE = By.XPATH, '//input[@ placeholder = "* Телефон: на него позвонит курьер"]'
    BUTTON_FORTH = By.XPATH, '//button[text() = "Далее"]'

    #DD = By.XPATH, '// div[text() = "Про аренду"]'
    FIELD_DATE = By.XPATH, '//input[@ placeholder = "* Когда привезти самокат"]'
    FIELD_RETAIL_PERIOD = By.XPATH, '//div[text() = "* Срок аренды"]'
    TWO_DAYS = By.XPATH, '//div[text() = "двое суток"]'
    COLOUR_SCOOTER = By.XPATH, '//input[@id = "black"]'
    COMMENT = By.XPATH, '//input[@ placeholder = "Комментарий для курьера"]'
    BUTTON_ORDER = By.XPATH, '(//button[text() = "Заказать"])[2]'
    BUTTON_YES = By.XPATH, '//button[text() = "Да"]'
    BUTTON_STATUS = By.XPATH, '//button[text() = "Посмотреть статус"]'
    DATA = By.XPATH, '//div[@aria-label="Choose пятница, 1-е марта 2024 г."]'



