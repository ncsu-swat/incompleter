# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58829152/docker-nameerror-name-app-is-not-defined
#importing dependencies
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(396722)

except ImportError:
    pass

#initializing the name of the application
app = _c_(396725, _n_(396723, "Flask", lambda: Flask), _n_(396724, "__name__", lambda: __name__))
_l_(396726)

@_c_(396729, _a_(396728, _n_(396727, "app", lambda: app), "route"), '/')

def hello(parameter_list):
    _l_(396731)

    aux = 'Hello, this is my first try on Docker'
    _l_(396730)
    return aux

if _n_(396732, "__name__", lambda: __name__) == "__main__":
    _l_(396737)

    _c_(396735, _a_(396734, _n_(396733, "app", lambda: app), "run"), host="0.0.0.0", debug= True)
    _l_(396736)