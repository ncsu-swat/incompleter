# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2835559/why-cant-python-parse-this-json-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
{
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": [{
        "id": "valore"
    }],
    "om_points": "value",
    "parameters": [{
        "id": "valore"
    }]
}
_l_(61414)
try:
    import json
    _l_(61416)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(61418)

except ImportError:
    pass
with _c_(61420, _n_(61419, "open", lambda: open), 'data.json') as data_file:
    _l_(61426)

    data_item = _c_(61424, _a_(61422, _n_(61421, "json", lambda: json), "load"), _n_(61423, "data_file", lambda: data_file))
    _l_(61425)
_c_(61429, _n_(61427, "pprint", lambda: pprint), _n_(61428, "data_item", lambda: data_item))
_l_(61430)

{'maps': [{'id': 'blabla', 'iscategorical': '0'},
          {'id': 'blabla', 'iscategorical': '0'}],
 'masks': [{'id': 'valore'}],
 'om_points': 'value',
 'parameters': [{'id': 'valore'}]}
_l_(61431)

_n_(61432, "valore", lambda: valore)
_l_(61433)

