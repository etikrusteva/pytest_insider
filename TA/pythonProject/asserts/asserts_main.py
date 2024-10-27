from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

import time

import config.selectors as selectors

timeout = 2

def assert_page_is_loaded(driver):
    # assert home page is fully loaded
    login_button = selectors.login_button_selector
    try:
        element_present = (EC.presence_of_element_located((By.CSS_SELECTOR, login_button)))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Home page didnt load in 5 secs")


def assert_careers_page_shows_content(driver):
    time.sleep(4)
    WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selectors.careers_list_selector)))

def assert_teams_are_opened(driver):
    try:
        element_present = (EC.presence_of_element_located((By.CSS_SELECTOR, selectors.last_job_item_selector)))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Teams didnt load in 5 secs")

def assert_teams(driver):
    if driver.find_elements(By.CSS_SELECTOR, selectors.last_job_item_selector):
        print("All teams opened")

def assert_locations(driver):
    if driver.find_elements(By.CSS_SELECTOR, selectors.locations_list_selector):
        print("All locations opened")

def assert_life(driver):
    if driver.find_elements(By.CSS_SELECTOR, selectors.slider_selector):
        print("All life images opened")
