from urls import TEXT_BOX
from data import FULL_NAMER, EMAIL, CURRENT_ADDRESS, PERMANENT_ADDRESS
import pytest
from pages.text_box import TextboxPage

class TestTextbox():
  def textbox_positive(self, driver):
        page = TextboxPage(driver, url=TEXT_BOX)

        # Open URL
        driver.get(TEXT_BOX)

        #Enter name
        page.full_name().clear()
        page.full_name().send_keys(FULL_NAME)

        # Enter email
        page.email_field().clear()
        page.email_field().send_keys(EMAIL)

        # Enter current address
        page.current_address().clear()
        page.current_address().send_keys(CURRENT_ADDRESS)

        # Enter permament address
        page.permanent_address().clear()
        page.permanent_address().send_keys(PERMANENT_ADDRESS)

        # Cklick submit button
        page.submit_button().cklick()

