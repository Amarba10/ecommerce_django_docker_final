import time
from select import select
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest


@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver"
    ser_firefox = FirefoxService(firefox_driver_binary)


    browser_name = "chrome"

    # if isinstance(browserName,list):
    #     for browser_name in browserName:
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        dc = {
            "browserName": "firefox",
            # "browserVersion": "101.0.1(x64)",
            "platformName": "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc)

    elif browser_name == "safari":
        dc = {
            "browserName": "safari",
            "platformName": "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc)

    elif browser_name == "chrome":
        dc = {
            "browserName": "chrome",
            "platformName": "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    elif browser_name == "firefox-mobile":
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")
        firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
                                                                     "(iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
                                                                     "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
        # firefox_options.set_preference("general.useragent.override", "Nexus 7")

        driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)



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
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys("amar.barake.1910sadas@gmail.com")
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

