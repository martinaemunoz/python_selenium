from typing import Literal
from selenium import webdriver # WebDriver to automate browsers
from selenium.webdriver.common.by import By # Locate elements (ID, name, etc.)
from selenium.webdriver.common.keys import Keys # Simulate keyboard inputs
from selenium.webdriver.support.ui import WebDriverWait # Handle wait conditions
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.common import NoSuchElementException # Exception handling
import time # Introduce delays
import pytest # Testing framework
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
fill_text = 'Hello World '
res_exctsc = 'All products | Books to Scrape - Sandbox'
res_exc = 'Hello World'

# simple web scrapping with Chrome
def test_webscrapping_simple_Cromium():
    driver = webdriver.Chrome() # launches Chrome browser
    driver.get(url_goo) # go to google
    time.sleep(2)
    driver.quit() # close browser 

# from web scrapping to testing with Edge
def test_selenium_Edge():
    driver = webdriver.Edge()
    driver.get(url_goo)
    time.sleep(2)
    assert driver.title in 'Google' # check that the title contains 'Google'
    driver.quit()

@pytest.mark.confixture # mark the function as a fixture
# testing to web scrapping books with Firefox
def test_topscrape_Firefox():
    driver = webdriver.Firefox()
    driver.get(url_tsc)
    time.sleep(2)
    assert driver.title == res_exctsc # verify the page title
    driver.quit()
    

def test_title():
# testing input field on Google with Firefox
    driver = webdriver.Firefox()
    driver.get(url_goo)
    time.sleep(2)
    add = driver.find_element(By.ID, 'APjFqb') # locate the search box by ID
    add.send_keys(res_exc)  # type "Hello World" into the search box
    assert add.get_property('value') == res_exc # verify the input value
    driver.quit()

def test_selenium_Firefox():
# filling of inputs
    pass

def test_add():
# parametrics
    pass

def test_sleep():
# clicking
    pass

def test_explicit():
# fill in a field, click on it and have selenium to wait
    pass

def test_topscrape_link():
    pass

def test_login_functionality():
    pass

def test_login_functional():
    pass