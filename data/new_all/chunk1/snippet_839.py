# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65012433/identifying-location-of-error-typeerror-nonetype-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(420390, _a_(420389, _n_(420388, "requests", lambda: requests), "post"), "http://localhost:5000/todo", 
                  json={"Title":"my first todo", 
                        "Description":"my first todo"})
_l_(420391)

_c_(420394, _a_(420393, _n_(420392, "requests", lambda: requests), "get"), "http://localhost:5000/todo", 
                      json={"Title":"my first todo", 
                            "Description":"my first todo"})
_l_(420395)