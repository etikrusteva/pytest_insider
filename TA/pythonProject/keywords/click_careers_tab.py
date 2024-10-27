from selenium.webdriver.common.by import By
import config.selectors as selectors
import time

def click_careers_tab(driver):
    # click careers tab
    # careers_button = driver.find_element(By.XPATH, selectors.careers_button_selector)
    # careers_button.click()

    careers_button = driver.find_element(By.XPATH, selectors.careers_button_selector)
    driver.execute_script("arguments[0].click();", careers_button)
