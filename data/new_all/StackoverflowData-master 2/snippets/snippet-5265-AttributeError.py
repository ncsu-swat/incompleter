#Source: https://stackoverflow.com/questions/76429200/attributeerror-nonetype-object-has-no-attribute-send-keys-plz-rply
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r"C:\Users\ram.sn\Desktop\New folder\chromedriver_win32 (2)\chromedriver.exe")

driver.get("https://www.nopcommerce.com/en/login")

driver.find_element_by_id("Username").send_keys("test")