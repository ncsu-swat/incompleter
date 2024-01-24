# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68330275/fastapi-typeerror-retreive-job-got-multiple-values-for-argument-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import Optional
    _l_(569598)

except ImportError:
    pass
try:
    from pydantic import BaseModel
    _l_(569600)

except ImportError:
    pass
try:
    from datetime import date, datetime
    _l_(569602)

except ImportError:
    pass


class JobBase(_n_(569603, "BaseModel", lambda: BaseModel)):
    _l_(569627)

    title: _n_(569604, "Optional", lambda: Optional)[_n_(569605, "str", lambda: str)] = None
    _l_(569606)
    company_name: _n_(569607, "Optional", lambda: Optional)[_n_(569608, "str", lambda: str)] = None
    _l_(569609)
    company_url: _n_(569610, "Optional", lambda: Optional)[_n_(569611, "str", lambda: str)] = None
    _l_(569612)
    location: _n_(569613, "Optional", lambda: Optional)[_n_(569614, "str", lambda: str)] = "remote"
    _l_(569615)
    description: _n_(569616, "Optional", lambda: Optional)[_n_(569617, "str", lambda: str)] = None
    _l_(569618)
    date_posted: _n_(569619, "Optional", lambda: Optional)[_n_(569620, "date", lambda: date)] = _c_(569625, _a_(569624, _c_(569623, _a_(569622, _n_(569621, "datetime", lambda: datetime), "now")), "date"))
    _l_(569626)

class JobCreate(_n_(569628, "JobBase", lambda: JobBase)):
    _l_(569637)

    title: _n_(569629, "str", lambda: str)
    _l_(569630)
    company_name: _n_(569631, "str", lambda: str)
    _l_(569632)
    location: _n_(569633, "str", lambda: str)
    _l_(569634)
    description: _n_(569635, "str", lambda: str)
    _l_(569636)

class ShowJob(_n_(569638, "JobBase", lambda: JobBase)):
    _l_(569654)

    title: _n_(569639, "str", lambda: str)
    _l_(569640)
    company_name: _n_(569641, "str", lambda: str)
    _l_(569642)
    company_url: _n_(569643, "Optional", lambda: Optional)[_n_(569644, "str", lambda: str)]
    _l_(569645)
    location: _n_(569646, "str", lambda: str)
    _l_(569647)
    date_posted: _n_(569648, "date", lambda: date)
    _l_(569649)
    description: _n_(569650, "str", lambda: str)
    _l_(569651)

    class Config():
        _l_(569653)

        orm_mode = True
        _l_(569652)