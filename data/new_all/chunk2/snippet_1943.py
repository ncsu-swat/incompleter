# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76815214/nameerror-name-user-is-not-defined-python-classmethod-not-recognizing-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy import MetaData
    _l_(422264)

except ImportError:
    pass
try:
    from sqlalchemy.orm import DeclarativeBase
    _l_(422266)

except ImportError:
    pass

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
_l_(422267)


class Base(_n_(422268, "DeclarativeBase", lambda: DeclarativeBase)):
    _l_(422295)

    __abstract__ = True
    _l_(422269)
    metadata = _c_(422272, _n_(422270, "MetaData", lambda: MetaData), naming_convention=_n_(422271, "convention", lambda: convention))
    _l_(422273)

    def __repr__(self) -> _n_(422274, "str", lambda: str):
        _l_(422294)

        columns = _c_(422287, _a_(422275, ", ", "join"), [f"{_n_(422276, 'k', lambda: k)}={_c_(422279, _n_(422277, 'repr', lambda: repr), _n_(422278, 'v', lambda: v))}" for k, v in _c_(422283, _a_(422282, _a_(422281, _n_(422280, "self", lambda: self), "__dict__"), "items")) if not _c_(422286, _a_(422285, _n_(422284, "k", lambda: k), "startswith"), "_")]
        )
        _l_(422288)
        aux = f"<{_a_(422291, _a_(422290, _n_(422289, 'self', lambda: self), '__class__'), '__name__')}({_n_(422292, 'columns', lambda: columns)})>"
        _l_(422293)
        return aux