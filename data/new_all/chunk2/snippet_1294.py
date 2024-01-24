# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55113041/attributeerror-module-flask-app-has-no-attribute-route
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  from flask import Flask, render_template, Blueprint, jsonify, session
  _l_(447006)

except ImportError:
  pass
try:
  import jinja2
  _l_(447008)

except ImportError:
  pass

class MyApp(_n_(447009, "Flask", lambda: Flask)):
  _l_(447047)

  def __init__(self):
    _l_(447046)

    _c_(447014, _a_(447011, _n_(447010, "Flask", lambda: Flask), "__init__"), _n_(447012, "self", lambda: self), _n_(447013, "__name__", lambda: __name__))
    _l_(447015)
    _n_(447016, "self", lambda: self).jinja_loader = _c_(447024, _a_(447018, _n_(447017, "jinja2", lambda: jinja2), "ChoiceLoader"), [_a_(447020, _n_(447019, "self", lambda: self), "jinja_loader"),_c_(447023, _a_(447022, _n_(447021, "jinja2", lambda: jinja2), "PrefixLoader"), {}, delimiter = ".")])
    _l_(447025)
    def create_global_jinja_loader(self):
      _l_(447029)

      aux = _a_(447027, _n_(447026, "self", lambda: self), "jinja_loader")
      _l_(447028)
      return aux

    def register_blueprint(self, bp):
      _l_(447045)

      _c_(447034, _a_(447031, _n_(447030, "Flask", lambda: Flask), "register_blueprint"), _n_(447032, "self", lambda: self), _n_(447033, "bp", lambda: bp))
      _l_(447035)
      _a_(447039, _a_(447038, _a_(447037, _n_(447036, "self", lambda: self), "jinja_loader"), "loaders")[1], "mapping")[_a_(447041, _n_(447040, "bp", lambda: bp), "name")] = _a_(447043, _n_(447042, "bp", lambda: bp), "jinja_loader")
      _l_(447044)

app = _c_(447049, _n_(447048, "MyApp", lambda: MyApp))
_l_(447050)
try:
  from xyzapp.autocomplete import autocomplete
  _l_(447052)

except ImportError:
  pass
try:
  from xyzapp.blueprint_folder_1.some_file import bp_1
  _l_(447054)

except ImportError:
  pass

_c_(447058, _a_(447056, _n_(447055, "app", lambda: app), "register_blueprint"), _n_(447057, "bp_1", lambda: bp_1))
_l_(447059)