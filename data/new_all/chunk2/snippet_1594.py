# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73402817/typeerror-googleauth-localwebserverauth-missing-1-required-positional-argumen
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pydrive.drive import GoogleDrive
    _l_(427838)

except ImportError:
    pass

gauth = _n_(427839, "GoogleAuth", lambda: GoogleAuth)
_l_(427840)
_c_(427843, _a_(427842, _n_(427841, "gauth", lambda: gauth), "LocalWebserverAuth"))
_l_(427844)
drive = _c_(427847, _n_(427845, "GoogleDrive", lambda: GoogleDrive), _n_(427846, "gauth", lambda: gauth))
_l_(427848)