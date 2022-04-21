import os
import time
import random

from pathlib import Path
from decouple import AutoConfig



from selenium import webdriver
from selenium.webdriver.common.keys import Keys


config = AutoConfig('../')
LUFA_EMAIL = config('LUFA_EMAIL')
LUFA_PW = config('LUFA_PW')

def cancel_order(email:str, password:str, driver_path:str='../drivers/chromedriver.exe'):
    """_summary_

    Args:
        email (str): Email used to login on lufa.com
        password (str): Password used to login on lufa.com
        driver_path (str): Path or location of the chrome webdriver.exe file
    """
    driver = webdriver.Chrome('../drivers/chromedriver.exe')
    
    driver.get('https://montreal.lufa.com/en/login')
    
    user_email_element = driver.find_element_by_id('LoginForm_user_email')
    
    user_email = driver.find_element_by_id('LoginForm_user_email')
    for letter in LUFA_EMAIL:
        time.sleep(random.random())
        user_email.send_keys(letter)
    
    user_pw = driver.find_element_by_id('LoginForm_password')
    for letter in LUFA_PW:
        time.sleep(random.random())
        user_pw.send_keys(letter)
    
    user_pw.send_keys(Keys.RETURN)
    
    time.sleep(2)
    
    driver.get('https://montreal.lufa.com/en/account')
    
    time.sleep(1)
    
    cancel_order = driver.find_element_by_xpath('//div[contains(@class, "order-details-buttons")]/*/span[contains(text(), "Cancel order")]')
    cancel_order.click()
    
    time.sleep(2)
    
    confirm_cancel = driver.find_element_by_xpath('//div[contains(@class, "cancel-buttons-pop-up")]/*/div[contains(text(), "Cancel my basket")]')
    confirm_cancel.click()
    
    driver.close()
    
    
cancel_order(LUFA_EMAIL, LUFA_PW)