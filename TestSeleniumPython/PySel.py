'''
Created on Dec 25, 2023

@author: Rakesh Singh
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def login_and_scrape():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    username = "student"
    password = "Password123"
    #button_selector = "your_button_selector"
    driver.get('https://practicetestautomation.com/practice-test-login/')
    time.sleep(2)
    # Perform login
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    # Wait for the page to load

    time.sleep(2)
    driver.find_element(By.LINK_TEXT, "Log out").click()

    driver.close()
    driver.quit()


# Call the function to execute the script
login_and_scrape()