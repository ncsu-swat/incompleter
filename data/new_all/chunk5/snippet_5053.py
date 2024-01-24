# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59883883/dont-understand-why-this-nameerror-name-null-is-not-defined-exception-occurs
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = [{"id": 111,
         "description": "",
         "name": _n_(677988, "null", lambda: null),
         "name_with_namespace": "Zzzz",
         "path": "Zzzz"
         },
        {"id": 222,
         "description": "",
         "name": "xp-demo-gradle",
         "name_with_namespace": "xp-demo-gradle",
         "path": "xp-demo-gradle"
         }]
_l_(677989)
for request in _n_(677990, "data", lambda: data):
    _l_(678020)

    lista = []
    _l_(677991)
    _n_(677992, "request", lambda: request)["id"]
    _l_(677993)
    paragraph = "id: " + _c_(677996, _n_(677994, "str", lambda: str), _n_(677995, "request", lambda: request)["id"]) + "; Path: " + _n_(677997, "request", lambda: request)["path"] + "; Name: " + _n_(677998, "request", lambda: request)["name"]
    _l_(677999)
    artifact = {
        "requested_by": "RequestFetcher",
        "argument": {
            "topic": {
                "id": 2
                },
            "key": _c_(678002, _n_(678000, "str", lambda: str), _n_(678001, "request", lambda: request)["id"]),
            "title": "ID " + _c_(678005, _n_(678003, "str", lambda: str), _n_(678004, "request", lambda: request)["id"]),
            "text": _n_(678006, "paragraph", lambda: paragraph),
            "cached": True,
            "_links": [
                {
                    "href": "https://gitlab.local.com/api/v4/projects/" + _c_(678009, _n_(678007, "str", lambda: str), _n_(678008, "request", lambda: request)["name"]),
                    "rel": "self",
                    "method": "GET"
                    }
                ],
            }
        }
    _l_(678010)
    _c_(678014, _a_(678012, _n_(678011, "lista", lambda: lista), "append"), _n_(678013, "artifact", lambda: artifact))
    _l_(678015)
    _c_(678018, _n_(678016, "print", lambda: print), _n_(678017, "lista", lambda: lista))
    _l_(678019)