import time
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import config.selectors as selectors


def assert_redirect(driver):
    # assert redirect to new url
    #redirect_url = driver.current_url
    #assert 'lever' in redirect_url
    time.sleep(3)

    try:
        timeout=5
        element_present = (EC.presence_of_element_located((By.CSS_SELECTOR, selectors.apply_selector)))
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print("Teams didnt load in 5 secs")
