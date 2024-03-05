from selenium.webdriver.common.by import By

# Main Page
class MainLocators():

   TITLE_BUTTON = (By.XPATH, '//*[@id="app"]/header/a')
   ELEMENTS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]')
   FORMS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]')
   ALERTS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[3]')
   WIDGETS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[4]')
   INTERACTIONS_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[5]')
   BOOK_STORE_BUTTON = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[6]')