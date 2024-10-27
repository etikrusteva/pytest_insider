import config.selectors as selectors
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

timeout = 5


def click_locations_dropdown(driver):
    # choose location
    filter_loaction = driver.find_element(By.CSS_SELECTOR, selectors.all_locations_dropdown_selector)
    filter_loaction.click()

def cick_departments_dropdown(driver):
    # choose department
    filter_department = driver.find_element(By.CSS_SELECTOR, selectors.all_departments_dropdown_selector)
    filter_department.click()


def chose_turkey_drodown(driver):
    # choose turkey as location
    try:
        element_present = (EC.presence_of_element_located((By.XPATH, selectors.turkey_dropdown_tab_selector)))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("qa jobs didnt load in 5 secs")
    filter_loaction = driver.find_element(By.XPATH, selectors.turkey_dropdown_tab_selector)
    filter_loaction.click()


def chose_qa_department_dropdown(driver):
    try:
        element_present = (EC.presence_of_element_located((By.XPATH, selectors.qa_dropdown_tab_selector)))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("qa jobs didnt load in 5 secs")

    filter_department_qa = driver.find_element(By.XPATH, selectors.qa_dropdown_tab_selector)
    filter_department_qa.click()
    filter_department_qa.click()