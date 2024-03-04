#Source: https://stackoverflow.com/questions/65250730/typeerror-str-object-is-not-callable-in-driver-title
from selenium import webdriver
path = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get() # in the parentheses is a link like https://link.com/
print(driver.title())
driver.quit()