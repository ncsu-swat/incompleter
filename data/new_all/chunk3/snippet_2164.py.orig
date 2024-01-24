#Source: https://stackoverflow.com/questions/60574127/typeerror-nonetype-object-is-not-callable-selenium
from selenium import webdriver

from bs4 import BeautifulSoup

driver=webdriver.Chrome('H:\datascience-python\selinium\chromedriver.exe')

driver.get('https://www.aljazeera.com/news/')

button = driver.find_element_by_id('btn_showmore_b1_418')

driver.execute_script("arguments[0].click();", button)

content = driver.page_source

soup = BeautifulSoup(content, 'html.parser')

container = soup.select('div.topics-sec-item-cont')

titlelist = []

urllist = []

for items in  container:

    if items is not None:

        title = items.find_element_by_xpath('//div[@class="col-sm-7 topics-sec-item-cont"]/a/h2').text

        url = items.find_element_by_xpath('//div[@class="col-sm-7 topics-sec-item-cont"]/a')

        titlelist.append(title)

        urllist.append(url.get_attribute('href'))

        print(str(titlelist) + '\n')

        print(str(urllist) + '\n')