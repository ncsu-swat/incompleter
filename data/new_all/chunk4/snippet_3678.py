# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69839628/attributeerror-nonetype-object-has-no-attribute-dropna
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import streamlit as st
  _l_(620038)

except ImportError:
  pass
try:
  from dataclasses import dataclass
  _l_(620040)

except ImportError:
  pass
try:
  import pandas as pd
  _l_(620042)

except ImportError:
  pass
try:
  import matplotlib.pyplot as plt
  _l_(620044)

except ImportError:
  pass
try:
  import seaborn as sns
  _l_(620046)

except ImportError:
  pass

@_n_(620047, "dataclass", lambda: dataclass)
class NumericColumn:
  _l_(620073)

  col_name: _n_(620048, "str", lambda: str) = None
  _l_(620049)
  serie: _a_(620051, _n_(620050, "pd", lambda: pd), "Series") = None
  _l_(620052)


  def get_name(self):
    _l_(620056)

    """
    Return name of selected column
    """
    aux = _a_(620054, _n_(620053, "self", lambda: self), "col_name")
    _l_(620055)
    return aux

  def get_unique(self):
    _l_(620064)

    """
    Return number of unique values for selected column
    """
    aux = _a_(620062, _a_(620061, _c_(620060, _a_(620059, _a_(620058, _n_(620057, "self", lambda: self), "serie"), "dropna")), "unique"), "size")
    _l_(620063)
    return aux

  def get_missing(self):
    _l_(620072)

    """
    Return number of missing values for selected column
    """
    aux = _c_(620070, _a_(620069, _c_(620068, _a_(620067, _a_(620066, _n_(620065, "self", lambda: self), "serie"), "isna")), "sum"))
    _l_(620071)
    return aux