# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73452408/how-to-fix-my-attributeerror-in-python-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import http.client as client
  _l_(350456)

except ImportError:
  pass
try:
  from tkinter import *
  _l_(350458)

except ImportError:
  pass
try:
  import json
  _l_(350460)

except ImportError:
  pass

root = _c_(350462, _n_(350461, "Tk", lambda: Tk))
_l_(350463)
_c_(350466, _a_(350465, _n_(350464, "root", lambda: root), "geometry"), '500x500')
_l_(350467)

conn = _c_(350470, _a_(350469, _n_(350468, "client", lambda: client), "HTTPSConnection"), "realstonks.p.rapidapi.com")
_l_(350471)

headers = {
    'X-RapidAPI-Key': "[CLASSIFIED]",
    'X-RapidAPI-Host': "realstonks.p.rapidapi.com"
}
_l_(350472)
_c_(350475, _a_(350474, _n_(350473, "root", lambda: root), "destroy"))
_l_(350476)
root = _c_(350478, _n_(350477, "Tk", lambda: Tk))
_l_(350479)
_c_(350482, _a_(350481, _n_(350480, "root", lambda: root), "geometry"), '500x500')
_l_(350483)
inputbox = _c_(350488, _a_(350487, _c_(350486, _n_(350484, "Text", lambda: Text), _n_(350485, "root", lambda: root), padx = 40, pady = 30), "pack"))
_l_(350489)
name = ""
_l_(350490)

def layout(data_obj):
  _l_(350539)

  vol = _n_(350491, "data_obj", lambda: data_obj)['total_vol']
  _l_(350492)
  price = _n_(350493, "data_obj", lambda: data_obj)['price']
  _l_(350494)
  percent = _n_(350495, "data_obj", lambda: data_obj)['change_percentage']
  _l_(350496)
  if _n_(350497, "percent", lambda: percent) < 0:
    _l_(350505)

    fg = 'red'
    _l_(350498)
  elif _n_(350499, "percent", lambda: percent) > 0:
    _l_(350504)

    fg = 'green'
    _l_(350500)
  elif _n_(350501, "percent", lambda: percent) == 0:
    _l_(350503)

    fg = 'gray'
    _l_(350502)
  title_widget = _c_(350511, _a_(350510, _c_(350509, _n_(350506, "Label", lambda: Label), _n_(350507, "root", lambda: root), text = _n_(350508, "name", lambda: name), font = ("arial bold", 50), underline = True), "pack"))
  _l_(350512)
  vol_widget = _c_(350518, _a_(350517, _c_(350516, _n_(350513, "Label", lambda: Label), _n_(350514, "root", lambda: root), text = _n_(350515, "vol", lambda: vol) + " in total.", font = ("arial bold", 40)), "pack"))
  _l_(350519)
  price_widget = _c_(350527, _a_(350526, _c_(350525, _n_(350520, "Label", lambda: Label), _n_(350521, "root", lambda: root), text = _c_(350524, _n_(350522, "str", lambda: str), _n_(350523, "price", lambda: price)) + " dollars per share.", font = ("arial bold", 30)), "pack"))
  _l_(350528)
  percent_widget = _c_(350537, _a_(350536, _c_(350535, _n_(350529, "Label", lambda: Label), _n_(350530, "root", lambda: root), text = _c_(350533, _n_(350531, "str", lambda: str), _n_(350532, "percent", lambda: percent)) + "%", font = ("arial bold", 20), fg = _n_(350534, "fg", lambda: fg)), "pack"))
  _l_(350538)

def search_function():
  _l_(350571)

  name = _c_(350542, _a_(350541, _n_(350540, "inputbox", lambda: inputbox), "get"), "1.0","end-1c")
  _l_(350543)
  _c_(350550, _a_(350545, _n_(350544, "conn", lambda: conn), "request"), "GET", "/" + _c_(350548, _a_(350547, _n_(350546, "name", lambda: name), "upper")), headers=_n_(350549, "headers", lambda: headers))
  _l_(350551)
  res = _c_(350554, _a_(350553, _n_(350552, "conn", lambda: conn), "getresponse"))
  _l_(350555)
  data = _c_(350558, _a_(350557, _n_(350556, "res", lambda: res), "read"))
  _l_(350559)
  # print(data)
  data_obj = _c_(350565, _a_(350561, _n_(350560, "json", lambda: json), "loads"), _c_(350564, _a_(350563, _n_(350562, "data", lambda: data), "decode"), 'utf-8'))
  _l_(350566)
  _c_(350569, _n_(350567, "layout", lambda: layout), _n_(350568, "data_obj", lambda: data_obj))
  _l_(350570)

search = _c_(350577, _a_(350576, _c_(350575, _n_(350572, "Button", lambda: Button), _n_(350573, "root", lambda: root), text = "Search Info", background = "gray", command = _n_(350574, "search_function", lambda: search_function)), "pack"))
_l_(350578)

_c_(350581, _a_(350580, _n_(350579, "root", lambda: root), "mainloop"))
_l_(350582)