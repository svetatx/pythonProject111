from base.selenium_base import BasePage
from locators.main_locators import MainLocators

class TextboxPage(BasePage):
    textbox_locators = TextboxLocators()

    def elements_headers_button(self):
        return self.is_clickable(self.main_locators. ELEMENTS_HEADER_BUTTON)

    def text_box(self):
        return self.is_clickable(self.main_locators.TEXT_BOX)

    def full_name(self):
        return self.is_clickable(self.main_locators.FULL_NAME)

    def email(self):
        return self.is_clickable(self.main_locators.EMAIL)

    def current_address(self):
        return self.is_clickable(self.main_locators.CURRENT_ADDRESS)

    def permanent_address(self):
        return self.is_clickable(self.main_locators.PERMANENT_ADDRESS)

    def submit_button(self):
        return self.is_clickable(self.main_locators.SUBMIT_BUTTON)



