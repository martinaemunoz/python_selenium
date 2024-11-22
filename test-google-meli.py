import datetime
import os
from typing import Literal
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
import time
import pytest
# import allure

# -----------------
# variable preconfig
url_goo = 'https://www.google.com'
url_tsc = 'https://books.toscrape.com/'
url_sel = 'https://www.selenium.dev/selenium/web/dynamic.html'
url_din = 'https://54a1-2800-810-470-86ea-3b92-7c51-5d4f-d5e9.ngrok-free.app'  
url_moz = 'https://www.mozilla.org/es-AR/'
url_pyt = 'https://www.python.org'
url_ptl = 'https://practicetestautomation.com/practice-test-login/'
url_din = 'https://54a1-2800-810-470-86ea-3b92-7c51-5d4f-d5e9.ngrok-free.app'  
fill_text = 'mercado libre argentina'
exep_meli = 'Mercado Libre Argentina - Envíos Gratis en el día'
search = 'Pc Gamer Ryzen 7 5700g Rtx 3060 12gb 32gb Vega 8960gb Wifi'
exep_mo = 'Internet para las personas, no para las ganancias'

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    yield driver # yield is sort of an async return
    driver.quit()

@pytest.fixture()
def firefox_browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture()
def edge_browser():
    driver = webdriver.Edge()
    yield driver
    driver.quit()

# def allure_attach(image_bytes, name):
#     allure_attach(
#         image_bytes,
#         name = name,
#         attachment_type = allure.attachment_type.PNG)

@pytest.mark.smoke
@pytest.mark.chrome
@pytest.mark.case_1
# @allure.title('google/meli.ar de búsqueda específica')

def test_meli(chrome_browser):
    chrome_browser.get(url_goo)
    chrome_browser.find_element(By.NAME, 'q').send_keys(fill_text, Keys.ENTER)
    time.sleep(2)
    chrome_browser.find_element(
        By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3'
    ).click()
    time.sleep(2)
    # allure_attach(chrome_browser.get_screenshot_as_png(), 'meli1.png')
    assert chrome_browser.title in exep_meli