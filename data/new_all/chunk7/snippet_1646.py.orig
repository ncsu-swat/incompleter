#Source: https://stackoverflow.com/questions/67154104/exception-has-occurred-attributeerror-webdriver-object-has-no-attribute-link
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import webbrowser
import time
import os

urls = [
    "URL 1",
    "URL 2"
]

PATH = "C:\Program Files (x86)\chromedriver.exe"

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(PATH, chrome_options=options)

def main():
    
    # stuff
    while True:
        for i in range(0, len(urls)):
            url = urls[i]
            time.sleep(2)
            print(url)
            wait = WebDriverWait(driver, 10)
            driver.link(url)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="availability"]/span')))
            print(driver.title)
            availablility = driver.find_element_by_xpath('//*[@id="availability"]/span')
            print(availablility.text)

main()