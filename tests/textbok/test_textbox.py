from urls import TEXT_BOX
from data import FULL_NAME, EMAIL, CURRENT_ADDRESS, PERMANENT_ADDRESS
import pytest
from pages.text_box import TextboxPage

class TestTextbox():
  def test_textbox(self, driver):
        page = TextboxPage(driver, url=TEXT_BOX)

        # Open URL
        driver.get(TEXT_BOX)

        # Enter name
        page.full_name().clear()
        page.full_name().send_keys(FULL_NAME)

        # Enter email
        page.email().clear()
        page.email().send_keys(EMAIL)

        # Enter current address
        page.current_address().clear()
        page.current_address().send_keys(CURRENT_ADDRESS)

        # Enter permament address
        page.permanent_address().clear()
        page.permanent_address().send_keys(PERMANENT_ADDRESS)

        # Click submit button
        page.submit_button().click()

