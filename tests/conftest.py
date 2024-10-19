from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='function')
def driver():
    # service = FirefoxService(executable_path=GeckoDriverManager().install())
    # options = webdriver.FirefoxOptions()
    # options.add_argument("--headless")
    # options.add_argument('--no-sandbox')
    # driver = webdriver.Firefox(service=service, options=options)
    # driver.maximize_window()
    # yield driver
    # attach = driver.get_screenshot_as_png()
    # allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    # driver.quit()

    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    attach = driver.get_screenshot_as_png()
    allure.attach(attach, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()