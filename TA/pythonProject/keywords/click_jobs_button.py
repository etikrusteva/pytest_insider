import time
from selenium.webdriver.common.by import By
import config.selectors as selectors

def click_jobs_button(driver):
    # click jobs button
    company_button = driver.find_element(By.CSS_SELECTOR, selectors.job_button_selector)
    company_button.click()