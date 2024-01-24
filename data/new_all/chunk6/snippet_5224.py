# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55288202/adding-uuid-type-to-cerberus-leads-to-bad-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import cerberus
    _l_(359712)

except ImportError:
    pass

class UUID:
    _l_(359728)

    name = "UUID"
    _l_(359713)

    def __init__(self, potential_uuid: _n_(359714, "str", lambda: str)):
        _l_(359721)

        _n_(359715, "self", lambda: self).uuid = _c_(359719, _a_(359717, _n_(359716, "uuid", lambda: uuid), "UUID"), _n_(359718, "potential_uuid", lambda: potential_uuid))
        _l_(359720)

    def __str__(self):
        _l_(359727)

        aux = _c_(359725, _n_(359722, "str", lambda: str), _a_(359724, _n_(359723, "self", lambda: self), "uuid"))
        _l_(359726)
        return aux

class Validator(_a_(359730, _n_(359729, "cerberus", lambda: cerberus), "Validator")):
    _l_(359769)

    def _register_types(self) -> _a_(359733, _a_(359732, _n_(359731, "cerberus", lambda: cerberus), "Validator"), "types_mapping"):
        _l_(359756)

        types_mapping = _c_(359737, _a_(359736, _a_(359735, _n_(359734, "Validator", lambda: Validator), "types_mapping"), "copy"))
        _l_(359738)
        for schema_type in _a_(359740, _n_(359739, "datatypes", lambda: datatypes), "ALL_TYPES"):
            _l_(359753)

            cerberus_type = _c_(359746, _a_(359742, _n_(359741, "cerberus", lambda: cerberus), "TypeDefinition"), _a_(359744, _n_(359743, "schema_type", lambda: schema_type), "name"),
                (_n_(359745, "schema_type", lambda: schema_type),),
                ())
            _l_(359747)
            _n_(359748, "types_mapping", lambda: types_mapping)[_a_(359750, _n_(359749, "schema_type", lambda: schema_type), "name")] = _n_(359751, "cerberus_type", lambda: cerberus_type)
            _l_(359752)
        aux = _n_(359754, "types_mapping", lambda: types_mapping)
        _l_(359755)
        return aux

    cerberus_type = _c_(359760, _a_(359758, _n_(359757, "cerberus", lambda: cerberus), "TypeDefinition"), "UUID",
        (_a_(359759, datatypes, "UUID"),),
        ())
    _l_(359761)
    types_mapping = _c_(359766, _a_(359765, _a_(359764, _a_(359763, _n_(359762, "cerberus", lambda: cerberus), "Validator"), "types_mapping"), "copy"))
    _l_(359767)
    types_mapping["UUID"] = cerberus_type
    _l_(359768)