from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from db import CONN
from datetime import datetime
import psycopg2
import json



class GetCodeSnippetFromPosts:
    def __init__(self):
        self.links = self.getListofLinksNeedToGetDetails()
        self.getCodeSnippet()

    def getCodeSnippet(self):
        driver = webdriver.Chrome()
        for link in self.links:
            post_id = link[0]
            post_link = link[1]
            print(post_link)
            driver.get(post_link)
            postcell_elements = driver.find_elements(By.CLASS_NAME,'postcell')
            count = 0
            snippets = []
            for postcell_element in postcell_elements:
                postcell_eleme = postcell_element.find_elements(By.CSS_SELECTOR, 'pre code')
                for element in postcell_eleme:
                    count +=1
                    snippets.append(element.text)
            self.insertSnipppetInDatabase(post_id,snippets,count)
            time.sleep(2)

    def insertSnipppetInDatabase(self, post_id, snippets, count):
        current_timestamp = datetime.now()
        snippets = json.dumps(snippets)
        try:
            with CONN.cursor() as cursor:
                cursor.execute("INSERT INTO post_details (post_id, message, parent_id, created_on, snippets, snippet_count) VALUES (%s, 'none', 0 , %s,  %s, %s)",
                               (post_id, current_timestamp, snippets, count ))

                print("Data inserted successfully")
            CONN.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error inserting data into the database")
            print(error)

    def getListofLinksNeedToGetDetails(self):

        with CONN.cursor() as cursor:
            cursor.execute("SELECT MAX(post_id) FROM post_details")
            max_value = cursor.fetchone()[0]
            if max_value == None :
                max_value = 0
            cursor.execute("SELECT post_id,post_link from posts where post_id > (%s)",(max_value,))
            links = cursor.fetchall()
            return links


x =  GetCodeSnippetFromPosts()


