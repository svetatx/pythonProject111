from base.selenium_base import BasePage
from locators.main_locators import MainLocators

class MainPage(BasePage):
    main_locators = MainLocators()

    def title_button(self):
        return self.is_clickable(self.main_locators.TITLE_BUTTON)

    def elements_button(self):
        return self.is_clickable(self.main_locators.ELEMENTS_BUTTON)

    def forms_button(self):
        return self.is_clickable(self.main_locators.FORMS_BUTTON)

    def alerts_button(self):
        return self.is_clickable(self.main_locators.ALERTS_BUTTON)

    def widgets_button(self):
        return self.is_clickable(self.main_locators.WIDGETS_BUTTON)

    def interactions_button(self):
        return self.is_clickable(self.main_locators.INTERACTIONS_BUTTON)

    def book_store_button(self):
        return self.is_clickable(self.main_locators.BOOK_STORE_BUTTON)
