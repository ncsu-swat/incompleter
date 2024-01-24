# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49267558/typeerror-expected-str-bytes-or-os-pathlike-object-not-io-bytesio
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from io import BytesIO
    _l_(401390)

except ImportError:
    pass
try:
    import requests
    _l_(401392)

except ImportError:
    pass
try:
    import pysftp
    _l_(401394)

except ImportError:
    pass
url = 'https://vignette.wikia.nocookie.net/disney/images/d/db/Donald_Duck_Iconic.png'
_l_(401395)

cnopts = _c_(401398, _a_(401397, _n_(401396, "pysftp", lambda: pysftp), "CnOpts"))
_l_(401399)
_n_(401400, "cnopts", lambda: cnopts).hostkeys = None 
_l_(401401) 
response = _c_(401405, _a_(401403, _n_(401402, "requests", lambda: requests), "get"), _n_(401404, "url", lambda: url))
_l_(401406)
netimage = _c_(401410, _n_(401407, "BytesIO", lambda: BytesIO), _a_(401409, _n_(401408, "response", lambda: response), "content")) #imagefromurl
_l_(401411) #imagefromurl

srv = _c_(401415, _a_(401413, _n_(401412, "pysftp", lambda: pysftp), "Connection"), host="12.34.567.89", username="root123",
password="password123",cnopts=_n_(401414, "cnopts", lambda: cnopts))
_l_(401416)

with _c_(401419, _a_(401418, _n_(401417, "srv", lambda: srv), "cd"), '/var/www'):
    _l_(401425)

    #srv.put('C:\Program Files\Python36\LICENSE.txt') #local file test
    _c_(401423, _a_(401421, _n_(401420, "srv", lambda: srv), "put"), _n_(401422, "netimage", lambda: netimage)) 
    _l_(401424) 

_c_(401427, _n_(401426, "print", lambda: print), 'Complete')
_l_(401428)