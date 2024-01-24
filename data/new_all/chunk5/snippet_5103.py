# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64342737/attributeerror-str-object-has-no-attribute-tk-in-tkinter-label
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from bs4 import BeautifulSoup
    _l_(683425)

except ImportError:
    pass
try:
    import urllib.request
    _l_(683427)

except ImportError:
    pass
try:
    from tkinter import *
    _l_(683429)

except ImportError:
    pass

root = _c_(683431, _n_(683430, "Tk", lambda: Tk))
_l_(683432)
_c_(683434, _n_(683433, "print", lambda: print), "Retrieving Source....")
_l_(683435)
site_data = _c_(683438, _a_(683437, _a_(683436, urllib, "request"), "urlopen"), "https://covidindia.org")
_l_(683439)
site_html = _c_(683442, _n_(683440, "BeautifulSoup", lambda: BeautifulSoup), _n_(683441, "site_data", lambda: site_data) , 'html.parser')
_l_(683443)

data = _c_(683446, _a_(683445, _n_(683444, "site_html", lambda: site_html), "find_all"), style = "text-align: center;")
_l_(683447)
data2= _c_(683450, _a_(683449, _n_(683448, "site_html", lambda: site_html), "find_all"), "h1")
_l_(683451)

# GUI Version

updated_as = _c_(683456, _n_(683452, "Label", lambda: Label), "Updated As:-", _c_(683455, _a_(683454, _n_(683453, "data", lambda: data)[0], "get_text"))[1:-1])
_l_(683457)
Total_Cases = _c_(683462, _n_(683458, "Label", lambda: Label), _c_(683461, _a_(683460, _n_(683459, "data2", lambda: data2)[1], "get_text")))
_l_(683463)
Active_Cases = _c_(683471, _n_(683464, "Label", lambda: Label), "Active Cases:", _c_(683467, _a_(683466, _n_(683465, "data", lambda: data)[2], "get_text")), "("+_c_(683470, _a_(683469, _n_(683468, "data", lambda: data)[3], "get_text"))+")")
_l_(683472)
Recov_Cases = _c_(683480, _n_(683473, "Label", lambda: Label), "Recovered Cases:", _c_(683476, _a_(683475, _n_(683474, "data", lambda: data)[5], "get_text")), "("+_c_(683479, _a_(683478, _n_(683477, "data", lambda: data)[6], "get_text"))+")")
_l_(683481)
Deaths = _c_(683489, _n_(683482, "Label", lambda: Label), "Deaths:", _c_(683485, _a_(683484, _n_(683483, "data", lambda: data)[8], "get_text")), "("+_c_(683488, _a_(683487, _n_(683486, "data", lambda: data)[9], "get_text"))+")")
_l_(683490)
Tests_Done = _c_(683498, _n_(683491, "Label", lambda: Label), "Tests Done:", _c_(683494, _a_(683493, _n_(683492, "data", lambda: data)[11], "get_text")), "("+_c_(683497, _a_(683496, _n_(683495, "data", lambda: data)[12], "get_text"))+")")
_l_(683499)

# Command Line Version

# print("Updated As:-", data[0].get_text()[1:-1])
# print(".................................................")
# print(data2[1].get_text())
# print("Active Cases:", data[2].get_text(), "("+data[3].get_text()+")")
# print("Recovered Cases:", data[5].get_text(), "("+data[6].get_text()+")")
# print("Deaths:", data[8].get_text(), "("+data[9].get_text()+")")
# print("Tests Done:", data[11].get_text(), "("+data[12].get_text()+")")
# input("Press Enter to Exit!")