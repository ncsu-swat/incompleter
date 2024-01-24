# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74953823/python-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(469264)

except ImportError:
    pass

def print_name():
    _l_(469277)

    with _c_(469266, _n_(469265, "open", lambda: open), file=r"test.json",mode='r') as json_file :
        _l_(469272)

        py_dict = _c_(469270, _a_(469268, _n_(469267, "json", lambda: json), "load"), _n_(469269, "json_file", lambda: json_file))
        _l_(469271)
    _c_(469275, _n_(469273, "print", lambda: print), _n_(469274, "py_dict", lambda: py_dict)["name"])
    _l_(469276)

_c_(469279, _n_(469278, "print_name", lambda: print_name))
_l_(469280)