# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64342737/attributeerror-str-object-has-no-attribute-tk-in-tkinter-label
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(677531)

except ImportError:
    pass
try:
    import urllib.request
    _l_(677533)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(677535)

except ImportError:
    pass

root = _c_(677537, _n_(677536, "Tk", lambda: Tk))
_l_(677538)
_c_(677540, _n_(677539, "print", lambda: print), "Retrieving Source....")
_l_(677541)
site_data = _c_(677544, _a_(677543, _a_(677542, urllib, "request"), "urlopen"), "https://covidindia.org")
_l_(677545)
site_html = _c_(677548, _n_(677546, "BeautifulSoup", lambda: BeautifulSoup), _n_(677547, "site_data", lambda: site_data) , 'html.parser')
_l_(677549)

data = _c_(677552, _a_(677551, _n_(677550, "site_html", lambda: site_html), "find_all"), style = "text-align: center;")
_l_(677553)
data2= _c_(677556, _a_(677555, _n_(677554, "site_html", lambda: site_html), "find_all"), "h1")
_l_(677557)

# GUI Version

updated_as = _c_(677562, _n_(677558, "Label", lambda: Label), "Updated As:-", _c_(677561, _a_(677560, _n_(677559, "data", lambda: data)[0], "get_text"))[1:-1])
_l_(677563)
Total_Cases = _c_(677568, _n_(677564, "Label", lambda: Label), _c_(677567, _a_(677566, _n_(677565, "data2", lambda: data2)[1], "get_text")))
_l_(677569)
Active_Cases = _c_(677577, _n_(677570, "Label", lambda: Label), "Active Cases:", _c_(677573, _a_(677572, _n_(677571, "data", lambda: data)[2], "get_text")), "("+_c_(677576, _a_(677575, _n_(677574, "data", lambda: data)[3], "get_text"))+")")
_l_(677578)
Recov_Cases = _c_(677586, _n_(677579, "Label", lambda: Label), "Recovered Cases:", _c_(677582, _a_(677581, _n_(677580, "data", lambda: data)[5], "get_text")), "("+_c_(677585, _a_(677584, _n_(677583, "data", lambda: data)[6], "get_text"))+")")
_l_(677587)
Deaths = _c_(677595, _n_(677588, "Label", lambda: Label), "Deaths:", _c_(677591, _a_(677590, _n_(677589, "data", lambda: data)[8], "get_text")), "("+_c_(677594, _a_(677593, _n_(677592, "data", lambda: data)[9], "get_text"))+")")
_l_(677596)
Tests_Done = _c_(677604, _n_(677597, "Label", lambda: Label), "Tests Done:", _c_(677600, _a_(677599, _n_(677598, "data", lambda: data)[11], "get_text")), "("+_c_(677603, _a_(677602, _n_(677601, "data", lambda: data)[12], "get_text"))+")")
_l_(677605)

# Command Line Version

# print("Updated As:-", data[0].get_text()[1:-1])
# print(".................................................")
# print(data2[1].get_text())
# print("Active Cases:", data[2].get_text(), "("+data[3].get_text()+")")
# print("Recovered Cases:", data[5].get_text(), "("+data[6].get_text()+")")
# print("Deaths:", data[8].get_text(), "("+data[9].get_text()+")")
# print("Tests Done:", data[11].get_text(), "("+data[12].get_text()+")")
# input("Press Enter to Exit!")