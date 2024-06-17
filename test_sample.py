from selenium import webdriver
from sample.google_page import GooglePage
from sample.naver_page import NaverPage
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_google(driver):
    google_page = GooglePage(driver=driver)
    google_page.goto()
    assert driver.title == "Google"


def test_naver(driver):
    naver_page = NaverPage(driver=driver)
    naver_page.goto()
    assert driver.title == "NAVER"
