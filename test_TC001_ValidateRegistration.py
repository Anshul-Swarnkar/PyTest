from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pytest

def test_registration_validate():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.thetestingworld.com/testings/")
    driver.maximize_window()
