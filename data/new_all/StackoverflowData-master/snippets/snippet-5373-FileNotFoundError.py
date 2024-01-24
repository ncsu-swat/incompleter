#Source: https://stackoverflow.com/questions/61286342/python3-x-attributeerror-nonetype-object-has-no-attribute-get-a-one-scrip
from bs4 import BeautifulSoup
filename = "F:\Test\ErrorFolder\ErrorFile.html"

with open(filename, "r") as f:
    soup = BeautifulSoup(f, 'html.parser')
    resources = soup.find(['ix:references', 'references'])
    #print(resources)
    for s in resources.find_all(['link:schemaRef', 'schemaRef', 'schemaref', 'link:schemaref']):
        x = s.get('xlink:href')
        print(x)