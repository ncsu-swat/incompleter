# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54199187/error-when-trying-to-send-text-to-application-with-pywinauto-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pywinauto as pwa
    _l_(569681)

except ImportError:
    pass
try:
    from pywinauto import application
    _l_(569683)

except ImportError:
    pass
try:
    from pywinauto import keyboard
    _l_(569685)

except ImportError:
    pass

app = _c_(569688, _a_(569687, _n_(569686, "application", lambda: application), "Application"))
_l_(569689)
app = _c_(569692, _a_(569691, _n_(569690, "app", lambda: app), "Connect"), path=r"C:\path\program.exe")                 
_l_(569693)                 
_c_(569697, _a_(569696, _a_(569695, _n_(569694, "win", lambda: win), "Part"), "Click")) #not completely sure why i do this
_l_(569698) #not completely sure why i do this
_c_(569701, _a_(569700, _n_(569699, "app", lambda: app)['Insert password']['Edit'], "send"), 'password')
_l_(569702)