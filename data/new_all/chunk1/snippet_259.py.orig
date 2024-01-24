#Source: https://stackoverflow.com/questions/49267558/typeerror-expected-str-bytes-or-os-pathlike-object-not-io-bytesio
from io import BytesIO
import requests
import pysftp
url = 'https://vignette.wikia.nocookie.net/disney/images/d/db/Donald_Duck_Iconic.png'

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None 
response = requests.get(url)
netimage = BytesIO(response.content) #imagefromurl

srv = pysftp.Connection(host="12.34.567.89", username="root123",
password="password123",cnopts=cnopts)

with srv.cd('/var/www'): #srvdir
    #srv.put('C:\Program Files\Python36\LICENSE.txt') #local file test
    srv.put(netimage) 

print('Complete')