############################################################################################################
#impoting necessary modules - packages
############################################################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # it is used for explicit wait in Selenium - used like this for example: WebDriverWait(driver,10).until(cond.alert_is_present())
import time

############################################################################################################
#Variables determination
############################################################################################################
driver = webdriver.Chrome()#(service=service_obj) #the instance of Chrome WebDriver is created.
driver.get("https://www.saucedemo.com")
print(driver.title)
user_name = "standard_user"
password = "secret_sauce"
#determined invalid user_name and password
invalid_user_name = 'branimir.stulic@azra.edu'
invalid_password = 'johhny '
first_name = 'Zarko'
last_name = 'Novicic'
postal_code = '11070'

############################################################################################################
#Functions determination
############################################################################################################
#Login function
def login():
    time.sleep(1)
    element = driver.find_element(By.ID, 'user-name')  # calling email text box
    element.click()
    time.sleep(1)
    element.send_keys(user_name)
    time.sleep(1)
    element = driver.find_element(By.ID, 'password')  # calling password text box
    element.send_keys(password)
    time.sleep(1)

    driver.find_element(By.ID, 'login-button').click()  # click on Login  button
    wait = WebDriverWait(driver, 10)  # make webdriver waits for some time (10) in seconds
# Successful_login function is created - checking if logging was successful (by availability of Products button - using text content with CLASS_NAME selector)
def successful_login():
    after_logging_content = driver.find_element(By.CLASS_NAME, 'title').get_attribute("textContent")
    if after_logging_content == 'Products':
        print('###############################################\nLogging in was successful!')
    else:
        raise Exception('###############################################\nUnsuccessful logging!')
#buying an item function
def buying_an_item():
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    driver.find_element(By.ID, 'shopping_cart_container').click()
    time.sleep(1)
    driver.find_element(By.ID, 'checkout').click()

    driver.find_element(By.ID, 'first-name').click()
    time.sleep(1)
    driver.find_element(By.ID, 'first-name').send_keys(first_name)

    driver.find_element(By.ID, 'last-name').click()
    time.sleep(1)
    driver.find_element(By.ID, 'last-name').send_keys(last_name)

    driver.find_element(By.ID, 'postal-code').click()
    time.sleep(1)
    driver.find_element(By.ID, 'postal-code').send_keys(postal_code)

    time.sleep(1)
    driver.find_element(By.ID, 'continue').click()
    print("###############################################\nShopping finieshed!")

# successful_shopping function is created - checking if shopping was successful (by availability of Checkout: Overview - using text content with CLASS_NAME selector)
def successful_shopping():
    time.sleep(2)
    after_shopping_content = driver.find_element(By.CLASS_NAME, 'header_secondary_container').get_attribute("textContent")
    if after_shopping_content == 'Checkout: Overview':
        print('###############################################\nShopping process was  successful!')
    else:
        raise Exception('###############################################\nUnsuccessful shopping process!')

# shopping_verification function is created - checking after shopping we have available notification (by availability of Thank you for your order! - using text content with CLASS_NAME selector)
def shopping_verification():
    time.sleep(1)
    verified_shopping = driver.find_element(By.CLASS_NAME, 'complete-header').get_attribute("textContent")
    if verified_shopping == 'Thank you for your order!':
        print('###############################################\nShopping verification was  successful!')
    else:
        raise Exception('###############################################\nUnsuccessful shopping verification!')
def logout():
    driver.find_element(By.ID, 'react-burger-menu-btn').click()
    time.sleep(1)
    driver.find_element(By.ID, 'logout_sidebar_link').click()
    time.sleep(1)
    print('###############################################\nUser logged out!')

def logout_verification():
    time.sleep(2)
    verified_logout = driver.find_element(By.ID, 'login-button').get_attribute("value")
    if verified_logout == 'Login':
        print('###############################################\nLogout verification was  successful!\nTest finished.\nFinal veridict - PASSED!')
    else:
        raise Exception('###############################################\nUnsuccessful logout verification!')


############################################################################################################
#calling login function
login()
#calling successful login function
successful_login()
#buying an item
buying_an_item()
#verification of loaded page after buying an item
successful_shopping()

driver.find_element(By.ID, 'finish').click()

#verification of completed order
shopping_verification()
#returning back to product list web page
driver.find_element(By.ID, 'back-to-products').click()

#calling logout function
logout()

#logout verification
logout_verification()

#closing browser
driver.close()