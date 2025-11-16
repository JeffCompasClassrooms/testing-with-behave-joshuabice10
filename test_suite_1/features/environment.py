from behave_webdriver.driver import BehaveDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    # Create plain Selenium driver
    selenium_driver = webdriver.Chrome(options=chrome_options)
    
    # Wrap it with BehaveDriver for behave-webdriver compatibility
    context.behave_driver = BehaveDriver(selenium_driver)

def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()