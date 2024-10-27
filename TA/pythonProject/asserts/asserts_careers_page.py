from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import time

import config.selectors as selectors


timeout = 5
def asser_jobs_are_loaded(driver):
    # assert jobs are loaded
    try:
        element_present = (EC.presence_of_element_located((By.XPATH, selectors.jobs_list_xpath)))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("qa jobs didnt load in 5 secs")

def assert_jobs_list(driver):
    driver.find_element(By.CSS_SELECTOR, selectors.list_qa_jobs_selector)

def assert_jobs_are_loaded(driver):
    time.sleep(4)
    # assert jobs are loaded
    try:
        element_present = (EC.presence_of_element_located((By.XPATH, selectors.card_qa_jobs_selector)))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("qa jobs didnt load in 5 secs")

def assert_text_qa(driver):
    # assert text QA
    time.sleep(3)
    position_titles = (driver.find_elements(By.CSS_SELECTOR, selectors.position_title_selector))
    for i in range(len(position_titles)):
        name_position = position_titles[i].text
        assert 'Quality Assurance' in name_position


def assert_text_department(driver):
    # assert text Department
    position_department = (driver.find_elements(By.CSS_SELECTOR, selectors.position_department_selector))
    for i in range(len(position_department)):
        name_department = position_department[i].text
        assert 'Quality Assurance' in name_department

def assert_text_location(driver):
    # assert text LOCATION
    position_location = (driver.find_elements(By.CSS_SELECTOR, selectors.position_location_selector))
    for i in range(len(position_location)):
        name_location = position_location[i].text
        assert 'Istanbul' and 'Turkey' in name_location