# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76921332/attributeerror-strbatch-object-has-no-attribute-stores-as
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import Optional, Tuple, List, Mapping
    _l_(614692)

except ImportError:
    pass

def stores_as(self, data: 'HeteroData'):
    _l_(614711)

    for node_type in _a_(614694, _n_(614693, "data", lambda: data), "node_types"):
        _l_(614700)

        _c_(614698, _a_(614696, _n_(614695, "self", lambda: self), "get_node_store"), _n_(614697, "node_type", lambda: node_type))
        _l_(614699)
    for edge_type in _a_(614702, _n_(614701, "data", lambda: data), "edge_types"):
        _l_(614708)

        _c_(614706, _a_(614704, _n_(614703, "self", lambda: self), "get_edge_store"), *_n_(614705, "edge_type", lambda: edge_type))
        _l_(614707)
    aux = _n_(614709, "self", lambda: self)
    _l_(614710)
    return aux

def collate(cls, data_list: _n_(614712, "List", lambda: List)[_n_(614713, "BaseData", lambda: BaseData)], increment: _n_(614714, "bool", lambda: bool) = True, add_batch: _n_(614715, "bool", lambda: bool) = True, follow_batch: _n_(614716, "Optional", lambda: Optional)[_n_(614717, "List", lambda: List)[_n_(614718, "str", lambda: str)]] = None, exclude_keys: _n_(614719, "Optional", lambda: Optional)[_n_(614720, "List", lambda: List)[_n_(614721, "str", lambda: str)]] = None, ) -> _n_(614722, "Tuple", lambda: Tuple)[_n_(614723, "BaseData", lambda: BaseData), _n_(614724, "Mapping", lambda: Mapping), _n_(614725, "Mapping", lambda: Mapping)]:
    _l_(614753)

# Collates a list of data objects into a single object of type cls.
# collate can handle both homogeneous and heterogeneous data objects by# individually collating all their stores.
# In addition, collate can handle nested data structures such as# dictionaries and lists.
    if not _c_(614730, _n_(614726, "isinstance", lambda: isinstance), _n_(614727, "data_list", lambda: data_list), (_n_(614728, "list", lambda: list), _n_(614729, "tuple", lambda: tuple))):
        _l_(614735)

        # Materialize `data_list` to keep the `_parent` weakref alive.
        data_list = _c_(614733, _n_(614731, "list", lambda: list), _n_(614732, "data_list", lambda: data_list))
        _l_(614734)
    if _n_(614736, "cls", lambda: cls) != _a_(614738, _n_(614737, "data_list", lambda: data_list)[0], "__class__"):
        _l_(614747)

        out = _c_(614742, _n_(614739, "cls", lambda: cls), _base_cls=_a_(614741, _n_(614740, "data_list", lambda: data_list)[0], "__class__"))  # Dynamic inheritance.  data_list[0]==>data_list
        _l_(614743)  # Dynamic inheritance.  data_list[0]==>data_list
    else:
        out = _c_(614745, _n_(614744, "cls", lambda: cls))
        _l_(614746)
    # Create empty stores:
    _c_(614751, _a_(614749, _n_(614748, "out", lambda: out), "stores_as"), _n_(614750, "data_list", lambda: data_list)[0])
    _l_(614752)