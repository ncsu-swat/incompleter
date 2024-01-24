# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61870153/typeerror-supertype-obj-obj-must-be-an-instance-or-subtype-of-type-error-w
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MetaDemo(_n_(700868, "type", lambda: type)):
    _l_(700924)

    def __new__(mcs, class_name: _n_(700869, "str", lambda: str), bases: Tuple[Type, ...], class_dict: Dict[_n_(700870, "str", lambda: str), Any]):
        _l_(700911)

        basis = _n_(700871, "bases", lambda: bases)[0]
        _l_(700872)
        c_attrs = _c_(700876, _n_(700873, "dict", lambda: dict), _a_(700875, _n_(700874, "basis", lambda: basis), "__dict__"))
        _l_(700877)
        prior_c_process_bases = _a_(700879, _n_(700878, "basis", lambda: basis), "__base__")
        _l_(700880)
        _n_(700881, "c_attrs", lambda: c_attrs)["__init__"] = lambda self, settings: _c_(700886, _a_(700883, _n_(700882, "prior_c_process_bases", lambda: prior_c_process_bases), "__init__"), _n_(700884, "self", lambda: self), _n_(700885, "settings", lambda: settings))
        _l_(700887)
        new_bases = _c_(700899, _a_(700889, _n_(700888, "types", lambda: types), "new_class"), _a_(700891, _n_(700890, "basis", lambda: basis), "__qualname__"), _a_(700893, _n_(700892, "basis", lambda: basis), "__bases__"),
                                    exec_body=lambda np: _c_(700898, _a_(700895, _n_(700894, "MetaDemo", lambda: MetaDemo), "populate_class_dict"), _n_(700896, "np", lambda: np), _n_(700897, "c_attrs", lambda: c_attrs)))
        _l_(700900)
        aux = _c_(700909, _a_(700904, _n_(700901, "super", lambda: super)(_n_(700902, "MetaDemo", lambda: MetaDemo), _n_(700903, "mcs", lambda: mcs)), "__new__"), _n_(700905, "mcs", lambda: mcs), _n_(700906, "class_name", lambda: class_name), (_n_(700907, "new_bases", lambda: new_bases),), _n_(700908, "class_dict", lambda: class_dict))
        _l_(700910)
        return aux

    @_n_(700912, "staticmethod", lambda: staticmethod)
    def populate_class_dict(namespace: Dict[_n_(700913, "str", lambda: str), Any], attr: Dict[_n_(700914, "str", lambda: str), Any]) -> None:
        _l_(700923)

        for key, value in _c_(700917, _a_(700916, _n_(700915, "attr", lambda: attr), "items")):
            _l_(700922)

            _n_(700918, "namespace", lambda: namespace)[_n_(700919, "key", lambda: key)] = _n_(700920, "value", lambda: value)
            _l_(700921)

class CustomLibraryDemo(_n_(700925, "LibraryDemo", lambda: LibraryDemo), metaclass=_n_(700926, "MetaDemo", lambda: MetaDemo)):
    _l_(700945)

    def __init__(self, test: Optional[_n_(700927, "str", lambda: str)] = None) -> None:
        _l_(700938)

        _c_(700933, _a_(700931, _n_(700928, "super", lambda: super)(_n_(700929, "CustomLibraryDemo", lambda: CustomLibraryDemo), _n_(700930, "self", lambda: self)), "__init__"), _n_(700932, "test", lambda: test))
        _l_(700934)
        _c_(700936, _n_(700935, "print", lambda: print), "At CustomDemo __init__ method: This message should appear")
        _l_(700937)

    def test(self) -> None:
        _l_(700944)

        _c_(700942, _n_(700939, "print", lambda: print), "In test method at CustomLibraryDemo class: %s" % _a_(700941, _n_(700940, "self", lambda: self), "test"))
        _l_(700943)