import time
import config.config as config
import keywords.chrome_driver as ch
import asserts.asserts_main as asserts
import keywords.accept_cookies as cookies
import keywords.click_company_dropdown as company_dropdown
import keywords.click_careers_tab as careers_tab
import  keywords.click_teams_button as teams_button
import keywords.scroll_to as scroll
import keywords.tear_down as tear_down


def test_check_insider_home_page():

#region HOME PAGE

    # instance of chrome web driver
    driver = ch.chrome_driver_instance()

    # navigate to home page insider
    driver.get(config.HOME_PAGE_URL)

    # assert page loaded
    asserts.assert_page_is_loaded(driver)

    #accept cookies to not intercept
    cookies.accept_cokies(driver)

    # click company dropdown in nav
    company_dropdown.click_company_dropdown(driver)

    # click careers tab
    careers_tab.click_careers_tab(driver)

#endregion

#region Careers

    # assert page loaded
    asserts.assert_page_is_loaded(driver)
    asserts.assert_careers_page_shows_content(driver)

    # scroll to teams
    scroll.scroll_to_teams(driver)

    # click teams button
    teams_button.click_teams_button(driver)

    # assert teams
    asserts.assert_teams_are_opened(driver)

    # scroll down to last item
    scroll.scroll_to_last_team(driver)

    # assert all teams are shown
    asserts.assert_teams_are_opened(driver)

    # scroll to location
    scroll.scroll_to_locations(driver)

    # assert locations are shown
    asserts.assert_locations(driver)

    # scroll to life
    scroll.scroll_to_life(driver)

    # assert life
    asserts.assert_life(driver)

    # tear down
    #tear_down.tear_down()
    time.sleep(2)
    driver.close()
    time.sleep(20)

#endregion

