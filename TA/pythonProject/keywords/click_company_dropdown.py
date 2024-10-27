import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
import keywords.tear_down as tear_down
from selenium.webdriver.common.by import By
import config.selectors as selectors



def click_company_dropdown(driver):
    # timeout = 5
    # element_present = (EC.presence_of_element_located((By.XPATH, selectors.jobs_list_xpath)))
    # # click company dropdown in nav
    # if element_present:
    #     try:
    #         WebDriverWait(driver, timeout).until(element_present)
    #         company_button = driver.find_element(By.CSS_SELECTOR, selectors.company_button_selector)
    #         company_button.click()
    #     except TimeoutException:
    #         tear_down.tear_down()
    #         print("qa jobs didnt load in 5 secs")

    company_button = driver.find_element(By.XPATH, selectors.company_button_selector)
    driver.execute_script("arguments[0].click();", company_button)
    #company_button = driver.find_element(By.XPATH, selectors.company_button_selector)
    #company_button.click()


