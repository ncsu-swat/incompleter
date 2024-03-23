#Source: https://stackoverflow.com/questions/54045102/filenotfounderrorwhen-trying-to-replace-existing-csv-file
database = "E:\Stock Database\Historical Data\Historical Stock List\\"

chrome_options      = webdriver.ChromeOptions()
prefs               = {'download.default_directory': database}
chrome_options.add_experimental_option(name='prefs', value= prefs)
stocks              = webdriver.Chrome(r"E:\Python Programs\chromedriver", chrome_options = chrome_options)

#Website
stocks.get(universe_data_site)

#Navigate Web Page
stocks.find_element_by_css_selector('#ui-id-4').click()
stocks.find_element_by_css_selector('#stocks > a.blue_button.factbutton').click()
stocks.find_element_by_css_selector('body > a:nth-child(3)').click()

#Download and renaiming of File
filename = 'allstocks.csv'

#removes existing file if already exists
if os.path.exists(r"%s%s"%(database,filename)) is True:
         os.remove(r"%s%s"%(database,filename))
         os.rename(r"%s"%database+ "stockfactsheet.csv ",r"%s%s"%(database,filename))
else:
        os.rename(r"%s"%database+ "stockfactsheet.csv ",r"%s%s"%(database,filename))