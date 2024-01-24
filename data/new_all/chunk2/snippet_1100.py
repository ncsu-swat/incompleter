#Source: https://stackoverflow.com/questions/53781253/web-scraping-filenotfounderror-when-saving-to-pdf
import requests
from bs4 import BeautifulSoup

def _getUrls_(res):
    hrefs = []
    soup = BeautifulSoup(res.text, 'lxml')
    main_content = soup.find('div',{'id' : 'content-core'})
    table = main_content.find("table")
    for a in table.findAll('a', href=True):
        hrefs.append(a['href'])
    return(hrefs)

bidurl = 'https://www.codot.gov/business/bidding/bid-tab-archives/bid-tabs-2017-1'
r = requests.get(bidurl)
hrefs = _getUrls_(r)

def _getPdfs_(hrefs, basedir):
    for i in range(len(hrefs)):
        print(hrefs[i])
        respdf = requests.get(hrefs[i])
        pdffile = basedir + "/pdf_dot/" + hrefs[i].split("/")[-1] + ".pdf"
        try:
            with open(pdffile, 'wb') as p:
                p.write(respdf.content)
                p.close()
        except FileNotFoundError:
            print("No PDF produced")

basedir= "/Users/ABC/Desktop"
_getPdfs_(hrefs, basedir)