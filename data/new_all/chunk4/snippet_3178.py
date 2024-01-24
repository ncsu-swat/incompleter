# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/23570549/beautiful-soup-error-nameerror-name-htmltext-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        from bs4 import BeautifulSoup
        _l_(642480)

except ImportError:
        pass
try:
        import urllib
        _l_(642482)

except ImportError:
        pass
try:
        import urllib.parse
        _l_(642484)

except ImportError:
        pass

url = "http://nytimes.com"
_l_(642485)

urls = [_n_(642486, "url", lambda: url)]
_l_(642487)
visited = [_n_(642488, "url", lambda: url)]
_l_(642489)

while _c_(642492, _n_(642490, "len", lambda: len), _n_(642491, "urls", lambda: urls)) > 0:
        _l_(642521)

        try:
                _l_(642505)

                htmltext = _c_(642498, _a_(642497, _c_(642496, _a_(642494, _n_(642493, "urllib", lambda: urllib), "urlopen"), _n_(642495, "urls", lambda: urls)[0]), "read"))
                _l_(642499)
        except:
                _l_(642504)

                _c_(642502, _n_(642500, "print", lambda: print), _n_(642501, "urls", lambda: urls)[0])      
                _l_(642503)      

        soup = _c_(642508, _n_(642506, "BeautifulSoup", lambda: BeautifulSoup), _n_(642507, "htmltext", lambda: htmltext))    
        _l_(642509)    
        _c_(642512, _a_(642511, _n_(642510, "urls", lambda: urls), "pop"), 0)
        _l_(642513)

        _c_(642519, _n_(642514, "print", lambda: print), _c_(642518, _a_(642516, _n_(642515, "soup", lambda: soup), "findAll"), 'a',href = _n_(642517, "true", lambda: true)))
        _l_(642520)