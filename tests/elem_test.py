import time
from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, 'https://translate.google.ru/?hl=ru&tab=TT')
    page.open()
    time.sleep(5)