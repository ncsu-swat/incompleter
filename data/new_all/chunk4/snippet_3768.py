# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68329046/fastapi-attributeerror-job-board-object-has-no-attribute-query
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from typing import Optional
    _l_(622037)

except ImportError:
    pass
try:
    from pydantic import BaseModel
    _l_(622039)

except ImportError:
    pass
try:
    from datetime import date, datetime
    _l_(622041)

except ImportError:
    pass


class JobBase(_n_(622042, "BaseModel", lambda: BaseModel)):
    _l_(622066)

    title: _n_(622043, "Optional", lambda: Optional)[_n_(622044, "str", lambda: str)] = None
    _l_(622045)
    company_name: _n_(622046, "Optional", lambda: Optional)[_n_(622047, "str", lambda: str)] = None
    _l_(622048)
    company_url: _n_(622049, "Optional", lambda: Optional)[_n_(622050, "str", lambda: str)] = None
    _l_(622051)
    location: _n_(622052, "Optional", lambda: Optional)[_n_(622053, "str", lambda: str)] = "remote"
    _l_(622054)
    description: _n_(622055, "Optional", lambda: Optional)[_n_(622056, "str", lambda: str)] = None
    _l_(622057)
    date_posted: _n_(622058, "Optional", lambda: Optional)[_n_(622059, "date", lambda: date)] = _c_(622064, _a_(622063, _c_(622062, _a_(622061, _n_(622060, "datetime", lambda: datetime), "now")), "date"))
    _l_(622065)

class JobCreate(_n_(622067, "JobBase", lambda: JobBase)):
    _l_(622076)

    title: _n_(622068, "str", lambda: str)
    _l_(622069)
    company_name: _n_(622070, "str", lambda: str)
    _l_(622071)
    location: _n_(622072, "str", lambda: str)
    _l_(622073)
    description: _n_(622074, "str", lambda: str)
    _l_(622075)

class ShowJob(_n_(622077, "JobBase", lambda: JobBase)):
    _l_(622093)

    title: _n_(622078, "str", lambda: str)
    _l_(622079)
    company_name: _n_(622080, "str", lambda: str)
    _l_(622081)
    company_url: _n_(622082, "Optional", lambda: Optional)[_n_(622083, "str", lambda: str)]
    _l_(622084)
    location: _n_(622085, "str", lambda: str)
    _l_(622086)
    date_posted: _n_(622087, "date", lambda: date)
    _l_(622088)
    description: _n_(622089, "str", lambda: str)
    _l_(622090)

    class Config():
        _l_(622092)

        orm_mode = True
        _l_(622091)