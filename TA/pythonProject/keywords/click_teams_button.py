from selenium.webdriver.common.by import By
import config.selectors as selectors

def click_teams_button(driver):
    teams_button = driver.find_element(By.CSS_SELECTOR, selectors.teams_button_selector)
    teams_button.click()


