# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76207404/kivy-python3-attributeerror-super-object-has-no-attribute-getattr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivymd.app import MDApp
    _l_(620724)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(620726)

except ImportError:
    pass
try:
    from kivymd.uix.datatables import MDDataTable
    _l_(620728)

except ImportError:
    pass
try:
    from kivy.metrics import dp
    _l_(620730)

except ImportError:
    pass
class Datatable(_n_(620731, "MDDataTable", lambda: MDDataTable)):
    _l_(620740)

    column_data = [('col1',_c_(620733, _n_(620732, "dp", lambda: dp), 30)),('col2',_c_(620735, _n_(620734, "dp", lambda: dp), 30)),('col3',_c_(620737, _n_(620736, "dp", lambda: dp), 30)),]
    _l_(620738)
    row_data = [('data1'),('data2'),('data3')]
    _l_(620739)
class app(_n_(620741, "MDApp", lambda: MDApp)):
    _l_(620747)

    def build(self):
        _l_(620746)

        aux = _c_(620744, _a_(620743, _n_(620742, "Builder", lambda: Builder), "load_file"), 'lab.kv')
        _l_(620745)
        return aux
_c_(620751, _a_(620750, _c_(620749, _n_(620748, "app", lambda: app)), "run")) 
_l_(620752) 