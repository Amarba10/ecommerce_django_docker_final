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




# Positive Scenario
def test_Registration(driver):
    driver.get('http://localhost:8000/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#navbarScroll > div > a:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a").click()
    driver.find_element(By.CSS_SELECTOR, "#name").send_keys("amaroo")
    Actual = driver.find_element(By.CSS_SELECTOR, "#name").text
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("amar.abs3dssfaddsfssf5@gmail.com")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Amar1234&*")
    driver.find_element(By.CSS_SELECTOR, "#passwordConfirm").send_keys("Amar1234&*")
    driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#username").click()
    driver.find_element(By.LINK_TEXT, "Profile").click()
    name = driver.find_element(By.CSS_SELECTOR, "#name")
    Expected = name.text
    assert Expected == Actual


# def test_login(driver):
#     driver.get('http://localhost:8000/')
#     driver.maximize_window()
#     driver.find_element(By.CSS_SELECTOR, "#navbarScroll > div > a:nth-child(2)").click()
#     driver.find_element(By.CSS_SELECTOR, "#email").send_keys("amar.abs3dsfsf5@gmail.com")
#     driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Amar1234&*")
#     driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button").click()
#     time.sleep(2)
#     # driver.find_element(By.CSS_SELECTOR, "#username").click()
#     # driver.find_element(By.LINK_TEXT, "Profile").click()
#     # result = driver.find_element(By.CSS_SELECTOR, "#name").text
#     # assert result == 'amaroo'

def test_Invalid_username(driver):
    driver.get('http://localhost:8000/')
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR,"#navbarScroll > div > a:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR,"#email").send_keys("asasdasd@gmail.com")
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys("as13213")
    driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > form > button").click()
    time.sleep(3)
    message = driver.find_element(By.CSS_SELECTOR,"#root > div > main > div > div > div > div.fade.alert.alert-danger.show").text
    assert message == "No active account found with the given credentials"

