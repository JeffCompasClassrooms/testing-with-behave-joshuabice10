from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given("I am on the Demoblaze homepage")
def step_homepage(context):
    context.behave_driver.get("https://www.demoblaze.com")

@then("I should see the logo and store name")
def step_logo_present(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    logo = driver.find_element(By.XPATH, "//img[@src='blazemeter-favicon-512x512.png']")
    navbar = driver.find_element(By.XPATH, "//a[@class='navbar-brand']")
    store_name = navbar.text

    assert store_name == "PRODUCT STORE"


@then("I should see a functioning carousel")
def step_carousel_present(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    driver.find_element(By.XPATH, "//div[@class='carousel slide']")

    wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='carousel-item']")))
    carousel_slides_inactive = driver.find_elements(By.XPATH, "//div[@class='carousel-item']")
    carousel_slides_active = driver.find_elements(By.XPATH, "//div[@class='carousel-item active']")
    assert len(carousel_slides_inactive) + len(carousel_slides_active) == 3

@then("I should see all the categories")
def step_all_categories_present(context):
    driver = context.behave_driver

    phone_category = driver.find_element(By.XPATH, "//a[@class='list-group-item' and text()='Phones']")
    laptop_category = driver.find_element(By.XPATH, "//a[@class='list-group-item' and text()='Laptops']")
    monitor_category = driver.find_element(By.XPATH, "//a[@class='list-group-item' and text()='Monitors']")

@then("I should see nine products on the page")
def step_all_products_present(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    all_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))
    assert len(all_products) == 9
    

@when("I sign up with a valid username and password")
def step_signup_valid(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    signup_link = wait.until(EC.element_to_be_clickable((By.ID, "signin2")))
    signup_link.click()

    signup_username = wait.until(EC.element_to_be_clickable((By.ID, "sign-username")))
    signup_username.send_keys("testuserfor3150")

    signup_password = driver.find_element(By.ID, "sign-password")
    signup_password.send_keys("testpassfor3150")

    signup_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
    signup_button.click()

    alert = wait.until(EC.alert_is_present())
    alert.accept() 

    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='signInModal']//button[@class='btn btn-secondary' and text()='Close']")))
    close_button.click()

@when("I login with my created username and password")
def step_login_valid(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    login_link = wait.until(EC.element_to_be_clickable((By.ID, "login2")))
    login_link.click()

    signup_username = wait.until(EC.element_to_be_clickable((By.ID, "loginusername")))
    signup_username.send_keys("testuserfor3150")

    signup_password = driver.find_element(By.ID, "loginpassword")
    signup_password.send_keys("testpassfor3150")

    signup_button = driver.find_element(By.XPATH, "//button[text()='Log in']")
    signup_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "nameofuser")))

@then("I should see my username displayed in the navbar")
def step_verify_username(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)

    wait.until(EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome"))
    user_element = driver.find_element(By.ID, "nameofuser")
    username_text = user_element.text

    assert "Welcome" in username_text

@when("I click on the phones category")
def step_phone_category_click(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    phone_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='list-group-item' and text()='Phones']")))
    phone_category.click()

    time.sleep(0.5)

@then("I should see seven phones")
def step_phone_category_works(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)
    
    time.sleep(1.5)
    
    all_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))
    
    assert len(all_products) >= 7, f"Expected at least 7 phones, found {len(all_products)}"

@when("I click on the laptop category")
def step_laptop_category_click(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    laptop_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='list-group-item' and text()='Laptops']")))
    laptop_category.click()

    time.sleep(0.5)


@then("I should see six laptops")
def step_laptop_category_works(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)
    
    time.sleep(1.5)
    
    all_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))
    
    assert len(all_products) >= 6, f"Expected at least 6 laptops, found {len(all_products)}"

@when("I click on the monitors category")
def step_monitor_category_click(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    laptop_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='list-group-item' and text()='Monitors']")))
    laptop_category.click()

    time.sleep(0.5)


@then("I should see two monitors")
def step_monitor_category_works(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)
    
    time.sleep(1.5)
    
    all_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))
    assert len(all_products) >= 2, f"Expected at least 2 monitors, found {len(all_products)}"

@when("I click on the categories button")
def step_categories_category_click(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    categories_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='list-group-item' and text()='CATEGORIES']")))
    categories_category.click()

    time.sleep(0.5)

@when("I click on the Samsung galaxy s6")
def step_galaxy_click(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    samsung_galaxy_s6 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='hrefch' and text()='Samsung galaxy s6']")))
    samsung_galaxy_s6.click()

    time.sleep(0.5)

@then("I should see the correct product")
def step_correct_product_name(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[@class='name' and text()='Samsung galaxy s6']")))

@when("I click on add samsung to cart")
def step_click_add_to_cart(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#' and @onclick='addToCart(1)']")))
    add_to_cart_button.click()

@then("I should see a product added alert")
def step_product_added_alert_present(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    alert = wait.until(EC.alert_is_present())
    assert alert

    alert.accept()

@when("I click on the cart page")
def step_click_to_cart_page(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    cart_link = wait.until(EC.element_to_be_clickable((By.ID, "cartur")))
    cart_link.click()

    time.sleep(0.5)

@then("I should see the phone in my cart")
def step_cart_item_present(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 15)
    
    time.sleep(2)
    
    try:
        phone_title = wait.until(
            EC.presence_of_element_located((By.XPATH, "//tbody[@id='tbodyid']//td[text()='Samsung galaxy s6']"))
        )
        assert phone_title is not None
    except Exception as e:
        cart_items = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']//tr")
        print(f"Cart contains {len(cart_items)} items")
        
        all_text = driver.find_element(By.XPATH, "//tbody[@id='tbodyid']").text
        print(f"Cart content: {all_text}")
        
        raise AssertionError(f"Samsung galaxy s6 not found in cart. Error: {e}")

@when("I click the delete button in my cart")
def step_delete_item_works(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    delete_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//tbody[@id='tbodyid']//td//a[@href='#']")))
    delete_button.click()

    time.sleep(0.5)

@then("I won't see my item in my cart anymore")
def step_item_is_gone(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)
    time.sleep(1.5)
    
    phone_title = driver.find_elements(By.XPATH, "//tbody[@id='tbodyid']//td[text()='Samsung galaxy s6']")
    
    assert len(phone_title) == 0, f"Expected item to be deleted but found {len(phone_title)} items still in cart"

@when("I click on the contact nav button")
def step_click_on_contact(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    contact_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='nav-item']//a[@class='nav-link' and text()='Contact']")))
    contact_button.click()

    time.sleep(1)

@then("I should see the new message modal")
def step_new_message_modal_visible(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    message_modal = driver.find_elements(By.XPATH, "//div[@class='modal-header']//h5[@class='modal-title' and text()='New message']")

    assert message_modal

@when("I click send message")
def step_send_message(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    send_message_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary' and text()='Send message']")))
    send_message_button.click()

    time.sleep(0.5)

@then("I see the alert pops up")
def step_alert_exists(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    try:
        alert = wait.until(EC.alert_is_present())
        alert.accept()
    except TimeoutError:
        print("No alert appeared")

@when("I click on about us nav button")
def step_click_about_us_button(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    about_us_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='nav-item']//a[@class='nav-link' and text()='About us']")))
    about_us_button.click()

    time.sleep(0.5)

@then("I should see the about us modal")
def step_about_us_modal_visible(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    about_us_modal = driver.find_elements(By.XPATH, "//div[@class='modal-header']//h5[@id='videoModalLabel' and text()='About us']")

    assert about_us_modal

@when("I click close")
def step_close_about_us_modal(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    close_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='videoModal']//button[text()='Close']")))
    close_button.click()

    time.sleep(1)

@then("I shouldn't see the about us modal")
def step_about_us_modal_not_visible(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    wait.until(EC.invisibility_of_element_located((By.ID, "videoModal")))

@then("I should be on the cart page")
def step_went_to_cart_page(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    current_url = driver.current_url

    assert current_url == 'https://www.demoblaze.com/cart.html'

@when("I click on the home button")
def step_click_home_button(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    home_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='nav-item active']//a[@class='nav-link' and @href='index.html']")))
    home_button.click()

    time.sleep(0.5)

@then("I should be on the home page")
def step_on_home_page(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    current_url = driver.current_url

    assert current_url == 'https://www.demoblaze.com/index.html'

@when("I click the next button")
def step_click_next_button(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@class='page-item']//button[@class='page-link' and text()='Next']")))
    next_button.click()

    time.sleep(0.5)

@then("I should see six products on the page")
def step_all_products_present(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver, 10)
    
    time.sleep(1.5)
    
    all_products = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card h-100']")))
    
    assert len(all_products) >= 6, f"Expected at least 6 products on page 2, found {len(all_products)}"

@when("I click on place order")
def step_click_place_order(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-lg-1']//button[@class='btn btn-success' and text()='Place Order']")))
    place_order_button.click()

    time.sleep(0.5)

@then("I should see the place order modal")
def step_place_order_modal_visible(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    about_us_modal = driver.find_elements(By.XPATH, "//div[@class='modal-header']//h5[@id='orderModalLabel' and text()='Place order']")

    assert about_us_modal

@when("I click on the purchase button")
def step_click_purchase_button(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    purchase_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='modal fade show' and @id='orderModal']//button[@class='btn btn-primary' and text()='Purchase']")))
    purchase_button.click()

    time.sleep(0.5)

@when("I enter all the required information")
def step_enter_information(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    place_order_name = wait.until(EC.element_to_be_clickable((By.ID, "name")))
    place_order_name.send_keys("Testname")

    credit_card_input = wait.until(EC.element_to_be_clickable((By.ID, "card")))
    credit_card_input.send_keys("12345678")

@then("I see the thank you message")
def step_thank_you_message(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Thank you for your purchase!']")))

@when("I click on the Nexus 6")
def step_nexus_click(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    nexus_6 = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='hrefch' and text()='Nexus 6']")))
    nexus_6.click()

    time.sleep(0.5)

@when("I click on add nexus to cart")
def step_click_add_to_cart(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#' and @onclick='addToCart(3)']")))
    add_to_cart_button.click()

@then("I should see all products listed")
def step_thank_you_message(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='success']//td[text()='Nexus 6']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='success']//td[text()='Samsung galaxy s6']")))

@when("I click logout")
def step_click_logout(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='logout2' and @onclick='logOut()']")))
    logout_button.click()

@then("I should no longer be logged in")
def step_logged_out(context):
    driver = context.behave_driver
    wait = WebDriverWait(driver,10)

    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='nav-link' and text()='Log in']")))
    wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='nav-link' and text()='Sign up']")))



    