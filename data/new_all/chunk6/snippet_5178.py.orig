#Source: https://stackoverflow.com/questions/61208342/attributeerror-trying-to-automate-whatsapp-using-selenium-in-python
from selenium import webdriver
from selenium.webdriver.support.ui  import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(r"C:\Users\Manan\Downloads\edgedriver_win64\msedgedriver") 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)
target = "Dad"
string = "message send from manan!!"
x_arg ='//span[contains(@title,'+ target + ')]'
target = wait.until(EC.presence_of_all_elements_located((By.XPATH, x_arg)))
target.click()