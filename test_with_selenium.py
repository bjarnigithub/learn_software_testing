# following tutorials: 
#   https://www.youtube.com/watch?v=9ye7srmAnMU
#   https://www.youtube.com/watch?v=NB8OceGZGjA
#   https://www.selenium.dev/documentation/webdriver/browsers/firefox/

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

options = webdriver.FirefoxOptions()
service = Service(executable_path="firefox_geckodriver/geckodriver.exe")
driver = webdriver.Firefox(options=options, service=service)

def test_getting_google_dot_com():

    """test if Selenium works for the first time after being installed 
       test by opening the Firefox browser and getting going to google.com, wait for 10 seconds and then close the browser"""
    
    driver.get("https://www.google.com/")
    time.sleep(10)
    driver.quit()

if __name__ == "__main__": 
    test_getting_google_dot_com()
