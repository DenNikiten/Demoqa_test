import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    # service = FirefoxService(executable_path=GeckoDriverManager().install())
    # options = webdriver.FirefoxOptions()
    # # options.add_argument("--headless")
    # driver = webdriver.Firefox(service=service, options=options)
    # driver.maximize_window()
    # yield driver
    # driver.quit()

    service = Service()
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()