#Source: https://stackoverflow.com/questions/44884830/typeerror-must-be-str-not-int-in-python-3
import os
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

while True:
    chromedriver  = 'F:\All  Folders\chromedriver\chrome.exe'

#Uncomment this block if you don't want images to load(makes the procss a little bit faster)
    '''
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
    '''

    browser = webdriver.Chrome(chromedriver)
    browser.get("http://www.website.com")       # website's home page
    time.sleep(10)

    # Logging into website
    form = browser.find_element_by_class_name('regular_login')
    email = form.find_element_by_name("email")
    password = form.find_element_by_name("password")
    button_element = browser.find_element_by_xpath("//*[@value='Login']")

    #List of emails
    email_list = ['na23b9@gmail.com', '25g65b@gmail.si', 'gfdebfk@gmail.jp']
    for emails, emails in enumerate(email_list):
      email.send_keys(emails)
      emails = emails + 1
      print("success")