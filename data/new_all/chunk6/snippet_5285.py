# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73452408/how-to-fix-my-attributeerror-in-python-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import http.client as client
  _l_(354621)

except ImportError:
  pass
try:
  from tkinter import *
  _l_(354623)

except ImportError:
  pass
try:
  import json
  _l_(354625)

except ImportError:
  pass

root = _c_(354627, _n_(354626, "Tk", lambda: Tk))
_l_(354628)
_c_(354631, _a_(354630, _n_(354629, "root", lambda: root), "geometry"), '500x500')
_l_(354632)

conn = _c_(354635, _a_(354634, _n_(354633, "client", lambda: client), "HTTPSConnection"), "realstonks.p.rapidapi.com")
_l_(354636)

headers = {
    'X-RapidAPI-Key': "[CLASSIFIED]",
    'X-RapidAPI-Host': "realstonks.p.rapidapi.com"
}
_l_(354637)
_c_(354640, _a_(354639, _n_(354638, "root", lambda: root), "destroy"))
_l_(354641)
root = _c_(354643, _n_(354642, "Tk", lambda: Tk))
_l_(354644)
_c_(354647, _a_(354646, _n_(354645, "root", lambda: root), "geometry"), '500x500')
_l_(354648)
inputbox = _c_(354653, _a_(354652, _c_(354651, _n_(354649, "Text", lambda: Text), _n_(354650, "root", lambda: root), padx = 40, pady = 30), "pack"))
_l_(354654)
name = ""
_l_(354655)

def layout(data_obj):
  _l_(354704)

  vol = _n_(354656, "data_obj", lambda: data_obj)['total_vol']
  _l_(354657)
  price = _n_(354658, "data_obj", lambda: data_obj)['price']
  _l_(354659)
  percent = _n_(354660, "data_obj", lambda: data_obj)['change_percentage']
  _l_(354661)
  if _n_(354662, "percent", lambda: percent) < 0:
    _l_(354670)

    fg = 'red'
    _l_(354663)
  elif _n_(354664, "percent", lambda: percent) > 0:
    _l_(354669)

    fg = 'green'
    _l_(354665)
  elif _n_(354666, "percent", lambda: percent) == 0:
    _l_(354668)

    fg = 'gray'
    _l_(354667)
  title_widget = _c_(354676, _a_(354675, _c_(354674, _n_(354671, "Label", lambda: Label), _n_(354672, "root", lambda: root), text = _n_(354673, "name", lambda: name), font = ("arial bold", 50), underline = True), "pack"))
  _l_(354677)
  vol_widget = _c_(354683, _a_(354682, _c_(354681, _n_(354678, "Label", lambda: Label), _n_(354679, "root", lambda: root), text = _n_(354680, "vol", lambda: vol) + " in total.", font = ("arial bold", 40)), "pack"))
  _l_(354684)
  price_widget = _c_(354692, _a_(354691, _c_(354690, _n_(354685, "Label", lambda: Label), _n_(354686, "root", lambda: root), text = _c_(354689, _n_(354687, "str", lambda: str), _n_(354688, "price", lambda: price)) + " dollars per share.", font = ("arial bold", 30)), "pack"))
  _l_(354693)
  percent_widget = _c_(354702, _a_(354701, _c_(354700, _n_(354694, "Label", lambda: Label), _n_(354695, "root", lambda: root), text = _c_(354698, _n_(354696, "str", lambda: str), _n_(354697, "percent", lambda: percent)) + "%", font = ("arial bold", 20), fg = _n_(354699, "fg", lambda: fg)), "pack"))
  _l_(354703)

def search_function():
  _l_(354736)

  name = _c_(354707, _a_(354706, _n_(354705, "inputbox", lambda: inputbox), "get"), "1.0","end-1c")
  _l_(354708)
  _c_(354715, _a_(354710, _n_(354709, "conn", lambda: conn), "request"), "GET", "/" + _c_(354713, _a_(354712, _n_(354711, "name", lambda: name), "upper")), headers=_n_(354714, "headers", lambda: headers))
  _l_(354716)
  res = _c_(354719, _a_(354718, _n_(354717, "conn", lambda: conn), "getresponse"))
  _l_(354720)
  data = _c_(354723, _a_(354722, _n_(354721, "res", lambda: res), "read"))
  _l_(354724)
  # print(data)
  data_obj = _c_(354730, _a_(354726, _n_(354725, "json", lambda: json), "loads"), _c_(354729, _a_(354728, _n_(354727, "data", lambda: data), "decode"), 'utf-8'))
  _l_(354731)
  _c_(354734, _n_(354732, "layout", lambda: layout), _n_(354733, "data_obj", lambda: data_obj))
  _l_(354735)

search = _c_(354742, _a_(354741, _c_(354740, _n_(354737, "Button", lambda: Button), _n_(354738, "root", lambda: root), text = "Search Info", background = "gray", command = _n_(354739, "search_function", lambda: search_function)), "pack"))
_l_(354743)

_c_(354746, _a_(354745, _n_(354744, "root", lambda: root), "mainloop"))
_l_(354747)