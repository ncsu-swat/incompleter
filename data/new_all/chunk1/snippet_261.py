# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47044129/nameerror-name-self-is-not-defined-after-using-eval
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyApp(_n_(379267, "QMainWindow", lambda: QMainWindow)):
    _l_(379278)

    def __init__(self):
        _l_(379277)

        [...]
        _l_(379268)
        Schaltpunkte=["Aussen1","Innen1","Innen2","Innen","Alle"]
        _l_(379269)
        for Schaltpunkt in _n_(379270, "Schaltpunkte", lambda: Schaltpunkte):
            _l_(379276)

            _c_(379274, _n_(379271, "eval", lambda: eval), "self.ui.Button_"+_n_(379272, "Schaltpunkt", lambda: Schaltpunkt)+"Laden.clicked.connect(lambda: self.ladeZeitschaltung("+_n_(379273, "Schaltpunkt", lambda: Schaltpunkt)+"))")
            _l_(379275)