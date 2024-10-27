from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import config.selectors as selectors
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
import keywords.tear_down as tear_down
import time

def scroll_to_teams(driver):
    time.sleep(3)
    #ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,selectors.careers_list_selector)).perform()

    teams_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selectors.careers_list_selector)))

    driver.execute_script("arguments[0].scrollIntoView()", teams_list)
    time.sleep(1)

def scroll_to_last_team(driver):
    time.sleep(3)
    #ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR,selectors.last_job_item_selector)).perform()
    last_teams_list = WebDriverWait(driver, 12).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selectors.last_job_item_selector)))

    driver.execute_script("arguments[0].scrollIntoView()", last_teams_list)

def scroll_to_locations(driver):
    time.sleep(1)
    #ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, selectors.slider_selector)).perform()
    location_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selectors.slider_selector)))

    driver.execute_script("arguments[0].scrollIntoView()", location_list)


def scroll_to_life(driver):
    #ActionChains(driver).move_to_element(driver.find_element(By.CSS_SELECTOR, selectors.life_list_locator)).perform()
    life_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, selectors.life_list_locator)))

    driver.execute_script("arguments[0].scrollIntoView()", life_list)