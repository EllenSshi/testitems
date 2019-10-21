import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_contains_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements_by_class_name("btn-add-to-basket")) > 0, "add-to-basket button is absent"
