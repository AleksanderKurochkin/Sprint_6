from selenium.webdriver.common.by import By


class HeaderPageOrderLocators:
    HEADER_SCOOTER = By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"
    HEADER_YANDEX = By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]"
