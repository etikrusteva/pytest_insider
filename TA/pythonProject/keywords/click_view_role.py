from selenium.webdriver.common.by import By
import config.selectors as selectors


def click_view_role(driver):
    # click view role
    role = driver.find_element(By.XPATH, selectors.view_role_selector)
    driver.execute_script("arguments[0].click();", role)