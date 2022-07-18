import time
from select import select
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.firefox import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest


@pytest.fixture()
def driver():
    # chrome_driver_binary = r"./chromedriver"
    # ser_chrome = ChromeService(chrome_driver_binary)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    yield driver
    driver.close()


def test_search_product(driver):
    driver.get('http://localhost:8000/')
    driver.maximize_window()
    time.sleep(5)
    product = driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div:nth-child(4) > div > div:nth-child(1) > div > div > a").text
    driver.find_element(By.CSS_SELECTOR,"#navbarScroll > form > input").send_keys(product)
    driver.find_element(By.CSS_SELECTOR,"#navbarScroll > form > button").click()
    time.sleep(2)
    Expected = driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > div > div > div > a").text
    assert Expected == product


def test_add_product_to_cart(driver):
    driver.get('http://localhost:8000/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div:nth-child(4) > div > div:nth-child(3) > div > div > a").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    name = driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div.col-md-8 > h1").text
    assert name == "SHOPPING CART"

def test_buy_product(driver):
    driver.get('http://localhost:8000/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#navbarScroll > div > a:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("amar.abs35@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Amar1234&*")
    driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div:nth-child(4) > div > div:nth-child(2) > div > div > a").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div.col-md-4 > div > div.list-group-item > button").click()
    driver.find_element(By.CSS_SELECTOR,"#address").send_keys("Shefa-amr,Elien")
    driver.find_element(By.CSS_SELECTOR,"#city").send_keys("Shefa-amr")
    driver.find_element(By.CSS_SELECTOR,"#postalCode").send_keys("202000")
    driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Israel")
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > form > button").click()
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > form > button").click()
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div.row > div.col-md-4 > div > div > div:nth-child(7) > button").click()
    time.sleep(2)
    # driver.find_element(By.CSS_SELECTOR,"#buttons-container > div > div.paypal-button-row.paypal-button-number-0.paypal-button-layout-vertical.paypal-button-shape-rect.paypal-button-number-multiple.paypal-button-env-sandbox.paypal-button-color-gold.paypal-button-text-color-black.paypal-logo-color-blue > div > div.paypal-button-spinner").click()



