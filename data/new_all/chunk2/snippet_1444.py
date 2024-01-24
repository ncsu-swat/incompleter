# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57904984/sqlalchemy-attributeerror-table-object-has-no-attribute-id
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Catalog(_a_(466916, _n_(466915, "db", lambda: db), "Model")):
    _l_(466953)

    __tablename__ = 'catalog'
    _l_(466917)

    id            = _c_(466920, _a_(466918, db, "Column"), _a_(466919, db, "Integer"), primary_key=True)
    _l_(466921)
    name          = _c_(466925, _a_(466922, db, "Column"), _c_(466924, _a_(466923, db, "String"), 60), index=True, nullable=False)
    _l_(466926)
    parent_id     = _c_(466931, _a_(466927, db, "Column"), _a_(466928, db, "Integer"), _c_(466930, _a_(466929, db, "ForeignKey"), 'catalog.id'), default=None)
    _l_(466932)
    url           = _c_(466936, _a_(466933, db, "Column"), _c_(466935, _a_(466934, db, "String")))
    _l_(466937)
    created       = _c_(466942, _a_(466938, db, "Column"), _a_(466939, db, "DateTime"), default=_c_(466941, _a_(466940, datetime, "now")))
    _l_(466943)
    last_modified = _c_(466948, _a_(466944, db, "Column"), _a_(466945, db, "DateTime"), index=True, onupdate=_c_(466947, _a_(466946, datetime, "now")))
    _l_(466949)

    categories = _c_(466951, _a_(466950, db, "relationship"), 'Catalog', remote_side='catalog.id', backref='parent')
    _l_(466952)

class Competitors(_a_(466955, _n_(466954, "db", lambda: db), "Model")):
    _l_(466993)

    __tablename__ = 'competitors'
    _l_(466956)

    id            = _c_(466959, _a_(466957, db, "Column"), _a_(466958, db, "Integer"), primary_key=True)
    _l_(466960)
    name          = _c_(466964, _a_(466961, db, "Column"), _c_(466963, _a_(466962, db, "String"), 40), index=True, nullable=False)
    _l_(466965)
    base_url      = _c_(466969, _a_(466966, db, "Column"), _c_(466968, _a_(466967, db, "String")))
    _l_(466970)
    cat_url       = _c_(466974, _a_(466971, db, "Column"), _c_(466973, _a_(466972, db, "String")))
    _l_(466975)
    created       = _c_(466980, _a_(466976, db, "Column"), _a_(466977, db, "DateTime"), default=_c_(466979, _a_(466978, datetime, "now")))
    _l_(466981)
    last_modified = _c_(466988, _a_(466982, db, "Column"), _a_(466983, db, "DateTime"), onupdate=_c_(466985, _a_(466984, datetime, "now")), default=_c_(466987, _a_(466986, datetime, "now")))
    _l_(466989)

    sells = _c_(466991, _a_(466990, db, "relationship"), 'Competitors_catalog', backref='competitor', cascade="all, delete-orphan", passive_deletes=True, lazy='dynamic')
    _l_(466992)

class CompCatalog(_a_(466995, _n_(466994, "db", lambda: db), "Model")):
    _l_(467037)

    __tablename__ = 'compcatalog'
    _l_(466996)

    id            = _c_(466999, _a_(466997, db, "Column"), _a_(466998, db, "Integer"), primary_key=True)
    _l_(467000)
    out_id        = _c_(467003, _a_(467001, db, "Column"), _a_(467002, db, "Integer"))
    _l_(467004)
    name          = _c_(467008, _a_(467005, db, "Column"), _c_(467007, _a_(467006, db, "String"), 60), index=True, nullable=False)
    _l_(467009)
    top_section   = _c_(467012, _a_(467010, db, "Column"), _a_(467011, db, "Integer"), default=None)
    _l_(467013)
    comp_id       = _c_(467018, _a_(467014, db, "Column"), _a_(467015, db, "Integer"), _c_(467017, _a_(467016, db, "ForeignKey"), 'competitors.id', ondelete="CASCADE"))
    _l_(467019)
    url           = _c_(467023, _a_(467020, db, "Column"), _c_(467022, _a_(467021, db, "String")))
    _l_(467024)
    created       = _c_(467029, _a_(467025, db, "Column"), _a_(467026, db, "DateTime"), default=_c_(467028, _a_(467027, datetime, "now")))
    _l_(467030)
    last_modified = _c_(467035, _a_(467031, db, "Column"), _a_(467032, db, "DateTime"), index=True, onupdate=_c_(467034, _a_(467033, datetime, "now")))
    _l_(467036)