# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77195885/pywinauto-menu-select-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pywinauto.application import Application
    _l_(583672)

except ImportError:
    pass

app = _c_(583674, _n_(583673, "Application", lambda: Application), backend="uia")
_l_(583675)
_c_(583679, _a_(583677, _n_(583676, "app", lambda: app), "start"), _n_(583678, "app_path", lambda: app_path))
_l_(583680)
dlg = _c_(583683, _a_(583682, _n_(583681, "app", lambda: app), "window"))
_l_(583684)
_c_(583687, _a_(583686, _n_(583685, "dlg", lambda: dlg), "wait"), "visible")
_l_(583688)
_c_(583691, _a_(583690, _n_(583689, "dlg", lambda: dlg), "print_control_identifiers"))
_l_(583692)
_c_(583695, _a_(583694, _n_(583693, "dlg", lambda: dlg), "menu_select"), "File->Exit")
_l_(583696)