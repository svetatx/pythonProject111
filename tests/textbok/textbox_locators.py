from selenium.webdriver.common.by import By

# Text box  Page
class TextboxLocators():
    TEXT_BOX = (By.XPATH, '//*[@id="item-0"]')
    FULL_NAME = (By.XPATH, '//*[@id="userName"]')
    EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//*[@id="permanentAddress"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit"]')