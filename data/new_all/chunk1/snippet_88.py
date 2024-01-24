# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/33792582/typeerror-getresponse-got-an-unexpected-keyword-argument-buffering
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(387312)

except ImportError:
    pass
try:
    from requests_file import FileAdapter
    _l_(387314)

except ImportError:
    pass

s = _c_(387317, _a_(387316, _n_(387315, "requests", lambda: requests), "Session")) 
_l_(387318) 
_c_(387323, _a_(387320, _n_(387319, "s", lambda: s), "mount"), 'file://', _c_(387322, _n_(387321, "FileAdapter", lambda: FileAdapter))) 
_l_(387324) 
resp = _c_(387327, _a_(387326, _n_(387325, "s", lambda: s), "get"), 'file:///local_package_name') 
_l_(387328) 
urldst = 'Upload URL' 
_l_(387329) 
rdst = _c_(387335, _a_(387331, _n_(387330, "requests", lambda: requests), "post"), _n_(387332, "urldst", lambda: urldst), files={'filename': _a_(387334, _n_(387333, "resp", lambda: resp), "content")}) 
_l_(387336) 
_c_(387339, _n_(387337, "print", lambda: print), _n_(387338, "rdst", lambda: rdst))
_l_(387340)