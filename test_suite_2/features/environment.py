from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    context.behave_driver = webdriver.Chrome(service=service, options=options)

def after_all(context):
    if hasattr(context, "behave_driver"):
        context.behave_driver.quit()
