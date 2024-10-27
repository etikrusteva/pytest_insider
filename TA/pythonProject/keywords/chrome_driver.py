import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from chromedriver_py import binary_path


def chrome_driver_instance():
    # instance of chrome web driver
    #chromedriver_autoinstaller.install()
    hub_url = "http://172.17.0.2:4444"

    options = Options()
    options.add_argument("--disable-search-engine-choice-screen --window-size=1920,1080 --no-sandbox")
    options.headless = True
    #options.binary_location = '/usr/local/app/google-chrome-stable_current_amd64.deb'
    #svc = webdriver.ChromeService(executable_path='/usr/local/app/chromedriver.exe', options=options)
    #svc = webdriver.ChromeService(executable_path='/chromedriver.exe', options=options)
    #driver = webdriver.Chrome(service=svc, options=options)
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Remote(command_executor=hub_url, options=options)

    driver.maximize_window()
    return driver
