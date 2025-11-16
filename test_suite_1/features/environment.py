import behave_webdriver

def before_all(context):
    context.behave_driver = behave_webdriver.Chrome(
        headless=True,
        options=['--no-sandbox', '--disable-dev-shm-usage', '--disable-gpu']
    )

def after_all(context):
    context.behave_driver.quit()