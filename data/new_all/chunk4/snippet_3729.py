# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69006489/downloading-image-from-url-filenotfounderror-errno-2-no-such-file-or-direct
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(620605)

except ImportError:
    pass
try:
    import os
    _l_(620607)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(620609)

except ImportError:
    pass
try:
    from downloader import download
    _l_(620611)

except ImportError:
    pass

url = 'https://urltoimage.com/123456/apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty/'
_l_(620612)
model_name = 'Coolname'
_l_(620613)

album_name = _c_(620620, _a_(620619, _c_(620618, _a_(620614, ' ', "join"), _c_(620617, _a_(620616, _n_(620615, "url", lambda: url), "split"), "/")), "split"))[-1] #apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty
_l_(620621) #apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty
_c_(620624, _n_(620622, "print", lambda: print), "Album name: " + _n_(620623, "album_name", lambda: album_name))
_l_(620625)
location = "C:/Users/Dave/Desktop/" + _n_(620626, "model_name", lambda: model_name) + "/" + _n_(620627, "album_name", lambda: album_name) + "/"
_l_(620628)

_c_(620631, _n_(620629, "print", lambda: print), 'Location: ' + _n_(620630, "location", lambda: location)) #C:/Users/Dave/Desktop/Coolname/apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty/
_l_(620632) #C:/Users/Dave/Desktop/Coolname/apple-banana-carrot-dog-electric-fish-gorilla-horse-igloo-jackrabbit-kangaroo-long-maze-nickel-octopus-pretty/

reqs = _c_(620636, _a_(620634, _n_(620633, "requests", lambda: requests), "get"), _n_(620635, "url", lambda: url))
_l_(620637)
soup = _c_(620641, _n_(620638, "BeautifulSoup", lambda: BeautifulSoup), _a_(620640, _n_(620639, "reqs", lambda: reqs), "text"), 'html.parser')
_l_(620642)

for link in _c_(620645, _a_(620644, _n_(620643, "soup", lambda: soup), "find_all"), 'img'):
    _l_(620666)

    if _n_(620646, "album_name", lambda: album_name) in _c_(620651, _a_(620650, _c_(620649, _a_(620648, _n_(620647, "link", lambda: link), "get"), 'src'), "lower")):
        _l_(620665)

        _c_(620656, _n_(620652, "print", lambda: print), _c_(620655, _a_(620654, _n_(620653, "link", lambda: link), "get"), 'src'))
        _l_(620657)
        _c_(620663, _n_(620658, "download", lambda: download), _c_(620661, _a_(620660, _n_(620659, "link", lambda: link), "get"), 'src'), _n_(620662, "location", lambda: location))
        _l_(620664)