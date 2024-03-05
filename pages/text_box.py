from base.selenium_base import BasePage
from locators.textbox_locators import TextboxLocators

class TextboxPage(BasePage):
    textbox_locators = TextboxLocators()



    def full_name(self):
        return self.is_clickable(self.textbox_locators.FULL_NAME)

    def email(self):
        return self.is_clickable(self.textbox_locators.EMAIL)

    def current_address(self):
        return self.is_clickable(self.textbox_locators.CURRENT_ADDRESS)

    def permanent_address(self):
        return self.is_clickable(self.textbox_locators.PERMANENT_ADDRESS)

    def submit_button(self):
        return self.is_clickable(self.textbox_locators.SUBMIT_BUTTON)



