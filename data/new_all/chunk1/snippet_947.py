# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70946505/typeerror-when-trying-to-send-outlook-email-via-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import win32com.client
    _l_(408380)

except ImportError:
    pass

outlook = _c_(408383, _a_(408382, _a_(408381, win32com, "client"), "Dispatch"), 'outlook.application')
_l_(408384)

mail = _c_(408387, _a_(408386, _n_(408385, "outlook", lambda: outlook), "CreateItem"), 0)
_l_(408388)
_n_(408389, "mail", lambda: mail).To = 'mitchell.mcdonald@veeder.com;mmcdonald1575@gmail.com'
_l_(408390)
_n_(408391, "mail", lambda: mail).Subject = 'Sample Email'
_l_(408392)


for i in _c_(408394, _n_(408393, "range", lambda: range), 5):
    _l_(408404)

    try:
        _l_(408403)

        _c_(408397, _a_(408396, _n_(408395, "mail", lambda: mail), "send"))
        _l_(408398)

    except:
        _l_(408402)

        _c_(408400, _n_(408399, "print", lambda: print), "failed")
        _l_(408401)