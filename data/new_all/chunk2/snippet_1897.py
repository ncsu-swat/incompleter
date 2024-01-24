# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41754786/nameerror-name-qwebpage-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import sys
  _l_(464856)

except ImportError:
  pass
try:
  from PyQt5.QtGui import *
  _l_(464858)

except ImportError:
  pass
try:
  from PyQt5.QtCore import *
  _l_(464860)

except ImportError:
  pass
try:
  from PyQt5.QtWebEngineWidgets import *
  _l_(464862)

except ImportError:
  pass
try:
  from lxml import html
  _l_(464864)

except ImportError:
  pass

#Take this class for granted.Just use result of rendering.
class Render(_n_(464865, "QWebPage", lambda: QWebPage)):
  _l_(464910)

  def __init__(self, url):
    _l_(464898)

    _n_(464866, "self", lambda: self).app = _c_(464870, _n_(464867, "QApplication", lambda: QApplication), _a_(464869, _n_(464868, "sys", lambda: sys), "argv"))  
    _l_(464871)  
    _c_(464875, _a_(464873, _n_(464872, "QWebPage", lambda: QWebPage), "__init__"), _n_(464874, "self", lambda: self))  
    _l_(464876)  
    _c_(464882, _a_(464879, _a_(464878, _n_(464877, "self", lambda: self), "loadFinished"), "connect"), _a_(464881, _n_(464880, "self", lambda: self), "_loadFinished"))  
    _l_(464883)  
    _c_(464891, _a_(464887, _c_(464886, _a_(464885, _n_(464884, "self", lambda: self), "mainFrame")), "load"), _c_(464890, _n_(464888, "QUrl", lambda: QUrl), _n_(464889, "url", lambda: url)))  
    _l_(464892)  
    _c_(464896, _a_(464895, _a_(464894, _n_(464893, "self", lambda: self), "app"), "exec_"))  
    _l_(464897)  

  def _loadFinished(self, result):
    _l_(464909)

    _n_(464899, "self", lambda: self).frame = _c_(464902, _a_(464901, _n_(464900, "self", lambda: self), "mainFrame"))  
    _l_(464903)  
    _c_(464907, _a_(464906, _a_(464905, _n_(464904, "self", lambda: self), "app"), "quit"))  
    _l_(464908)  

url = 'http://pycoders.com/archive/'  
_l_(464911)  
r = _c_(464914, _n_(464912, "Render", lambda: Render), _n_(464913, "url", lambda: url))  
_l_(464915)  
result = _c_(464919, _a_(464918, _a_(464917, _n_(464916, "r", lambda: r), "frame"), "toHtml"))
_l_(464920)
#This step is important.Converting QString to Ascii for lxml to process
archive_links = _c_(464928, _a_(464922, _n_(464921, "html", lambda: html), "fromstring"), _c_(464927, _n_(464923, "str", lambda: str), _c_(464926, _a_(464925, _n_(464924, "result", lambda: result), "toAscii"))))
_l_(464929)
_c_(464932, _n_(464930, "print", lambda: print), _n_(464931, "archive_links", lambda: archive_links))
_l_(464933)