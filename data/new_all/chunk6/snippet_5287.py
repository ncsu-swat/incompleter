# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73067007/typeerror-params-my-params-is-expected-to-be-class-params-myparams-but-val
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(361861)

except ImportError:
    pass
try:
    from dataclasses import dataclass
    _l_(361863)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(361865)

except ImportError:
    pass
try:
    import yaml
    _l_(361867)

except ImportError:
    pass
try:
    from decouple import config
    _l_(361869)

except ImportError:
    pass
try:
    from typed_json_dataclass import TypedJsonMixin
    _l_(361871)

except ImportError:
    pass


@_n_(361872, "dataclass", lambda: dataclass)
class MyParams(_n_(361873, "TypedJsonMixin", lambda: TypedJsonMixin)):
    _l_(361905)

    host: _n_(361874, "str", lambda: str)
    _l_(361875)
    project: _n_(361876, "str", lambda: str)
    _l_(361877)
    roi_term: _n_(361878, "str", lambda: str)
    _l_(361879)

    def __post_init__(self):
        _l_(361904)

        _n_(361880, "self", lambda: self).public_key = _c_(361882, _n_(361881, "config", lambda: config), 'KEY')
        _l_(361883)
        assert _c_(361888, _n_(361884, "isinstance", lambda: isinstance), _a_(361886, _n_(361885, "self", lambda: self), "public_key"), _n_(361887, "str", lambda: str))
        _l_(361889)
        _n_(361890, "self", lambda: self).private_key = _c_(361892, _n_(361891, "config", lambda: config), 'SECRET')
        _l_(361893)
        assert _c_(361898, _n_(361894, "isinstance", lambda: isinstance), _a_(361896, _n_(361895, "self", lambda: self), "private_key"), _n_(361897, "str", lambda: str))
        _l_(361899)
        _c_(361902, _a_(361901, _n_(361900, "super", lambda: super)(), "__post_init__"))
        _l_(361903)

# ...
@_n_(361906, "dataclass", lambda: dataclass)
class Params(_n_(361907, "TypedJsonMixin", lambda: TypedJsonMixin)):
    _l_(361910)

    my_params: _n_(361908, "MyParams", lambda: MyParams)
    _l_(361909)


def load_params_dict():
    _l_(361945)

    parameter_file = 'params.yaml'
    _l_(361911)
    cwd = _c_(361916, _n_(361912, "Path", lambda: Path), _c_(361915, _a_(361914, _n_(361913, "os", lambda: os), "getcwd")))
    _l_(361917)
    params_path = _n_(361918, "cwd", lambda: cwd) / _n_(361919, "parameter_file", lambda: parameter_file)
    _l_(361920)
    if _c_(361923, _a_(361922, _n_(361921, "params_path", lambda: params_path), "exists")):
        _l_(361942)

        params = _c_(361929, _a_(361925, _n_(361924, "yaml", lambda: yaml), "safe_load"), _c_(361928, _n_(361926, "open", lambda: open), _n_(361927, "params_path", lambda: params_path)))
        _l_(361930)
    else:  # If this script is being called from the path directory
        params_path = _a_(361932, _n_(361931, "cwd", lambda: cwd), "parent") / _n_(361933, "parameter_file", lambda: parameter_file)
        _l_(361934)
        params = _c_(361940, _a_(361936, _n_(361935, "yaml", lambda: yaml), "safe_load"), _c_(361939, _n_(361937, "open", lambda: open), _n_(361938, "params_path", lambda: params_path)))
        _l_(361941)
    aux = _n_(361943, "params", lambda: params)
    _l_(361944)
    return aux


params_dict = _c_(361947, _n_(361946, "load_params_dict", lambda: load_params_dict))
_l_(361948)
_c_(361951, _n_(361949, "print", lambda: print), _n_(361950, "params_dict", lambda: params_dict))
_l_(361952)
project_params = _c_(361956, _a_(361954, _n_(361953, "Params", lambda: Params), "from_dict"), _n_(361955, "params_dict", lambda: params_dict))
_l_(361957)