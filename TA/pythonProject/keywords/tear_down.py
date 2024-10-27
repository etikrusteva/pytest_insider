import keywords.chrome_driver as chrome_driver

def tear_down():
    chrome_driver.chrome_driver_instance().close()