import time
from selenium.webdriver.common.by import By
import config.selectors as selectors


def accept_cokies(driver):

    # accept
    time.sleep(2)
    accept_button = driver.find_element(By.CSS_SELECTOR, selectors.accept_button_selector)
    accept_button.click()