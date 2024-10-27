import time

import config.config as config
import keywords.chrome_driver as ch
import asserts.asserts_main as asserts
import keywords.accept_cookies as cookies
import  keywords.click_jobs_button as jobs_button
import keywords.click_dropdown as dropdown
import asserts.asserts_careers_page as assert_careers_page
import keywords.click_view_role as view_role
import asserts.asserts_redirect as redirect
import keywords.tear_down as tear_down


def test_check_careers_page():

#region HOME PAGE
    # instance of chrome web driver
    driver = ch.chrome_driver_instance()

    # navigate to home page insider
    driver.get(config.CAREERS_PAGE_URL)

    # assert page loaded
    asserts.assert_page_is_loaded(driver)

    #accept cookies to not intercept
    cookies.accept_cokies(driver)
#endregion

#region JOBS

    # click jobs button
    jobs_button.click_jobs_button(driver)

    # assert jobs list is shown
    assert_careers_page.asser_jobs_are_loaded(driver)

    # choose location
    dropdown.click_locations_dropdown(driver)

    # choose turkey as location
    dropdown.chose_turkey_drodown(driver)

    # choose department
    dropdown.cick_departments_dropdown(driver)

    # choose qa department
    dropdown.chose_qa_department_dropdown(driver)

    # find jobs list
    assert_careers_page.assert_jobs_list(driver)

    # assert jobs are loaded
    assert_careers_page.asser_jobs_are_loaded(driver)

    # assert text QA
    assert_careers_page.assert_text_qa(driver)

    # assert text Department
    assert_careers_page.assert_text_department(driver)

    # assert text LOCATION
    assert_careers_page.assert_text_location(driver)

    # click view role
    view_role.click_view_role(driver)

    # assert page loaded
    asserts.assert_page_is_loaded(driver)

    # assert redirect to new url
    redirect.assert_redirect(driver)

# tear down
    time.sleep(2)
    driver.close()
#endregion
