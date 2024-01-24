#Source: https://stackoverflow.com/questions/44996255/typeerror-object-of-type-nonetype-has-no-len-when-iterating-through-files
import os
import time
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def Quora_bot():

    username = None
    password = None

    chromedriver  = 'F:\All  Folders\chromedriver\shit.exe'

#Uncomment this block if you don't want images to load(makes the procss a little bit faster)
    '''
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    chromeOptions.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chromedriver, chrome_options=chromeOptions)
    '''

    browser = webdriver.Chrome(chromedriver)
    browser.get("http://www.quora.com")       # Quora home page
    time.sleep(10)

    # Logging into Quora
    form = browser.find_element_by_class_name('regular_login')
    email = form.find_element_by_name("email")
    password = form.find_element_by_name("password")
    button_element = browser.find_element_by_xpath("//*[@value='Login']")
    email.send_keys(username)
    password.send_keys(password)


with open('newfile.txt') as u:
      for line in u:
        rr = line


with open('password.txt') as p:
     for linee in p:
       pp = linee

Quora_bot()
username = rr
password = pp