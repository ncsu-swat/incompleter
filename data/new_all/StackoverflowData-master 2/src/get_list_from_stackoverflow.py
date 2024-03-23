from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from db import CONN
from datetime import datetime
import psycopg2



class GetListFromStackOverflow:
    def __init__(self):
        self.current_page_number = self.getLatestPageNumber()
        self.maximum_page_number = 6851
        self.intented_error_text = ["typeerror", "attributeerror", "filenotfounderror", "modulenotfoundError", "nameerror"]
    def getRowResponse(self):
        driver = webdriver.Chrome()
        while self.current_page_number < self.maximum_page_number :
            driver.get('https://stackoverflow.com/questions/tagged/python-3.x?tab=votes&page=' + str(
                self.current_page_number) + '&pagesize=50')
            elements_with_specific_class = driver.find_elements(By.CLASS_NAME,'s-post-summary--content-title a')
            for element in elements_with_specific_class:
                converted_string = element.text.replace(" ", "").lower()
                if any(error_str in converted_string for error_str in self.intented_error_text):
                    self.insertLinkIntoTable(element.get_attribute("href"))
            self.current_page_number += 1
            time.sleep(1)
        driver.quit()

    def getLatestPageNumber(self):
        with CONN.cursor() as cursor:
            cursor.execute("SELECT MAX(page_number) FROM posts")
            max_value = cursor.fetchone()[0]
            if max_value == None:
                max_value = 0
            return max_value+1

    def insertLinkIntoTable(self,link):
        current_timestamp = datetime.now()
        try:
            with CONN.cursor() as cursor:
                cursor.execute("INSERT INTO posts (post_link, created_on, page_number) VALUES (%s, %s, %s)",
                               (link, current_timestamp, self.current_page_number))
                print("Data inserted successfully")
            CONN.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error inserting data into the database")
            print(error)

