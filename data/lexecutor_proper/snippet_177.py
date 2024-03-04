# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(61875)

except ImportError:
    pass

_c_(61881, _a_(61877, _n_(61876, "json", lambda: json), "dumps"), _n_(61878, "your_object", lambda: your_object), default=lambda __o: _a_(61880, _n_(61879, "__o", lambda: __o), "__dict__"))
_l_(61882)
try:
    import json
    _l_(61884)

except ImportError:
    pass
try:
    from dataclasses import dataclass
    _l_(61886)

except ImportError:
    pass


@_n_(61887, "dataclass", lambda: dataclass)
class Company:
    _l_(61892)

    id: _n_(61888, "int", lambda: int)
    _l_(61889)
    name: _n_(61890, "str", lambda: str)
    _l_(61891)

@_n_(61893, "dataclass", lambda: dataclass)
class User:
    _l_(61902)

    id: _n_(61894, "int", lambda: int)
    _l_(61895)
    name: _n_(61896, "str", lambda: str)
    _l_(61897)
    email: _n_(61898, "str", lambda: str)
    _l_(61899)
    company: _n_(61900, "Company", lambda: Company)
    _l_(61901)


company = _c_(61904, _n_(61903, "Company", lambda: Company), id=1, name="Example Ltd")
_l_(61905)
user = _c_(61908, _n_(61906, "User", lambda: User), id=1, name="John Doe", email="john@doe.net", company=_n_(61907, "company", lambda: company))
_l_(61909)


_c_(61915, _a_(61911, _n_(61910, "json", lambda: json), "dumps"), _n_(61912, "user", lambda: user), default=lambda __o: _a_(61914, _n_(61913, "__o", lambda: __o), "__dict__"))
_l_(61916)

{
  "id": 1, 
  "name": "John Doe", 
  "email": "john@doe.net", 
  "company": {
    "id": 1, 
    "name": "Example Ltd"
  }
}
_l_(61917)

