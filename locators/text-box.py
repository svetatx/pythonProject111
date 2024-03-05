from selenium.webdriver.common.by import By

# Text box  Page
class TextboxLocators():

    ELEMENTS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
    ELEMENTS_HEADER_BUTTON = (By.XPATH, '///*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')
    TEXT_BOX = (By.XPATH, '//*[@id="item-0"]')
    FULL_NAME = (By.XPATH, '//*[@id="userName"]')
    EMAIL = (By.XPATH, '//*[@id="userEmail"]')
    CURRENT_ADDRESS = (By.XPATH, '//*[@id="currentAddress"]')
    PERMANENT_ADDRESS = (By.XPATH, '//*[@id="permanentAddress"]')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="submit"]')



    CHECK_BOX = (By.XPATH, '//*[@id="item-1"]')
    RADIO_BUTTON = (By.XPATH, '//*[@id="item-2"]')
    WEB_TABLES = (By.XPATH, '//*[@id="item-3"]')
    BUTTONS = (By.XPATH, '//*[@id="item-4"]')
    LINKS = (By.XPATH, '//*[@id="item-5"]')
    BROKEN_LINKS = (By.XPATH, '//*[@id="item-6"]')
    UPLOAD_AND_DOWNLOAD = (By.XPATH, '//*[@id="item-7"]')
    DYNAMIC_PROPERTIES = (By.XPATH, '//*[@id="item-8"]')