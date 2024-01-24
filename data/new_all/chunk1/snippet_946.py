# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70946505/typeerror-when-trying-to-send-outlook-email-via-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client
    _l_(398736)

except ImportError:
    pass

outlook = _c_(398739, _a_(398738, _a_(398737, win32com, "client"), "Dispatch"), 'outlook.application')
_l_(398740)

mail = _c_(398743, _a_(398742, _n_(398741, "outlook", lambda: outlook), "CreateItem"), 0)
_l_(398744)
_n_(398745, "mail", lambda: mail).To = 'mitchell.mcdonald@veeder.com;mmcdonald1575@gmail.com'
_l_(398746)
_n_(398747, "mail", lambda: mail).Subject = 'Sample Email'
_l_(398748)

_c_(398751, _a_(398750, _n_(398749, "mail", lambda: mail), "send"))
_l_(398752)