# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67660952/attributeerror-type-object-calculavariaciones-has-no-attribute-retornos-diar
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(559833)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(559835)

except ImportError:
    pass
try:
    import datetime as dt
    _l_(559837)

except ImportError:
    pass
try:
    import numpy as np
    _l_(559839)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(559841)

except ImportError:
    pass

class ImportaYahoo:
    _l_(559871)

    def __init__(self):
        _l_(559852)

        _n_(559842, "self", lambda: self).df_apple = _c_(559845, _a_(559844, _n_(559843, "pd", lambda: pd), "DataFrame"), {})
        _l_(559846)
        _n_(559847, "self", lambda: self).apple_close = _c_(559850, _a_(559849, _n_(559848, "pd", lambda: pd), "DataFrame"), {})    
        _l_(559851)    
    
    def importar_cotizaciones (self):
        _l_(559870)

        try:
            import yfinance
            _l_(559854)

        except ImportError:
            pass
        name = 'AAPL'
        _l_(559855)
        ticker = _c_(559859, _a_(559857, _n_(559856, "yfinance", lambda: yfinance), "Ticker"), _n_(559858, "name", lambda: name))
        _l_(559860)
        _n_(559861, "self", lambda: self).df_apple = _c_(559864, _a_(559863, _n_(559862, "ticker", lambda: ticker), "history"), interval="1d",start="2017-01-4",end="2021-04-10")
        _l_(559865)
        _n_(559866, "self", lambda: self).apple_close = _a_(559868, _n_(559867, "self", lambda: self), "df_apple")[["Close"]]
        _l_(559869)

class CalculaVariaciones:
    _l_(559913)

    
    def __init__(self, importar_yahoo):
        _l_(559885)

        _n_(559872, "self", lambda: self).df_yahoo = _n_(559873, "importar_yahoo", lambda: importar_yahoo)
        _l_(559874)
        _n_(559875, "self", lambda: self).retornos_diarios = _c_(559878, _a_(559877, _n_(559876, "pd", lambda: pd), "DataFrame"), {})
        _l_(559879)
        _n_(559880, "self", lambda: self).log_retornos_diarios = _c_(559883, _a_(559882, _n_(559881, "pd", lambda: pd), "DataFrame"), {})
        _l_(559884)
    def calc_retornos_diarios(self):
        _l_(559903)

        # Porcentaje de variación diaria
        _n_(559886, "self", lambda: self).retornos_diarios = _c_(559891, _a_(559890, _a_(559889, _a_(559888, _n_(559887, "self", lambda: self), "df_yahoo"), "apple_close"), "pct_change"))
        _l_(559892)
        _c_(559896, _a_(559895, _a_(559894, _n_(559893, "self", lambda: self), "retornos_diarios"), "fillna"), 0, inplace=True)
        _l_(559897)
        _c_(559901, _a_(559900, _a_(559899, _n_(559898, "self", lambda: self), "retornos_diarios"), "dropna"), inplace = True)
        _l_(559902)
    
    def calc_log_retornos_diarios(self):
        _l_(559912)

        _n_(559904, "self", lambda: self).log_retornos_diarios = _c_(559910, _a_(559906, _n_(559905, "np", lambda: np), "log"), _a_(559909, _a_(559908, _n_(559907, "self", lambda: self), "df_yahoo"), "retornos_diarios") + 1)
        _l_(559911)
class DibujaHistograma():
    _l_(559944)

    def __init__(self, CalculaVariaciones ):
        _l_(559917)

        _n_(559914, "self", lambda: self).variaciones = _n_(559915, "CalculaVariaciones", lambda: CalculaVariaciones)
        _l_(559916)
    def mostrar_histograma (self):
        _l_(559943)

        # Plot the histogram
        _c_(559919, _n_(559918, "print", lambda: print), "\n*******************************************************")        
        _l_(559920)        
        _c_(559925, _a_(559924, _a_(559923, _a_(559922, _n_(559921, "self", lambda: self), "variaciones"), "retornos_diarios"), "hist"), bins = 100, color='blue', figsize=(15, 8))
        _l_(559926)
        _c_(559929, _a_(559928, _n_(559927, "plt", lambda: plt), "ylabel"), 'Frecuencia')
        _l_(559930)
        _c_(559933, _a_(559932, _n_(559931, "plt", lambda: plt), "xlabel"), 'Retornos diarios')
        _l_(559934)
        _c_(559937, _a_(559936, _n_(559935, "plt", lambda: plt), "title"), 'Histograma de los retornos diarios')
        _l_(559938)
        _c_(559941, _a_(559940, _n_(559939, "plt", lambda: plt), "show"))        
        _l_(559942)        
importar_yahoo = _c_(559946, _n_(559945, "ImportaYahoo", lambda: ImportaYahoo))
_l_(559947)
_c_(559950, _a_(559949, _n_(559948, "importar_yahoo", lambda: importar_yahoo), "importar_cotizaciones")) 
_l_(559951) 

calcula_variaciones = _c_(559954, _n_(559952, "CalculaVariaciones", lambda: CalculaVariaciones), _n_(559953, "importar_yahoo", lambda: importar_yahoo))
_l_(559955)
_c_(559958, _a_(559957, _n_(559956, "calcula_variaciones", lambda: calcula_variaciones), "calc_retornos_diarios"))
_l_(559959)
#calcula_variaciones.calc_log_retornos_diarios()

histograma = _c_(559962, _n_(559960, "DibujaHistograma", lambda: DibujaHistograma), _n_(559961, "CalculaVariaciones", lambda: CalculaVariaciones))
_l_(559963)
_c_(559966, _a_(559965, _n_(559964, "histograma", lambda: histograma), "mostrar_histograma"))
_l_(559967)