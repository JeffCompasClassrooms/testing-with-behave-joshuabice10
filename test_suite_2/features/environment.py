from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    # Selenium 3.x syntax - NO service parameter
    context.behave_driver = webdriver.Chrome(options=chrome_options)
    context.behave_driver.implicitly_wait(10)

def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()
