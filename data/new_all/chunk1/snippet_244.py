# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35998854/sqlalchemy-tablename-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sqlalchemy import Column, String, Integer, ForeignKey
    _l_(380809)

except ImportError:
    pass
try:
    from sqlalchemy.ext.declarative import declarative_base
    _l_(380811)

except ImportError:
    pass
try:
    from sqlalchemy.orm import sessionmaker
    _l_(380813)

except ImportError:
    pass

Base = _c_(380815, _n_(380814, "declarative_base", lambda: declarative_base))
_l_(380816)

class Collection(_n_(380817, "Base", lambda: Base)):
    _l_(380827)

    __tablename__ == 'Collection'
    _l_(380818)
    id = _c_(380821, _n_(380819, "Column", lambda: Column), _n_(380820, "Integer", lambda: Integer), primary_key=True)
    _l_(380822)
    name = _c_(380825, _n_(380823, "Column", lambda: Column), _n_(380824, "String", lambda: String))
    _l_(380826)


class Sheet(_n_(380828, "Base", lambda: Base)):
    _l_(380845)

    __tablename__ = 'sheet'
    _l_(380829)
    id = _c_(380832, _n_(380830, "Column", lambda: Column), _n_(380831, "Integer", lambda: Integer), primary_key=True)
    _l_(380833)
    name = _c_(380837, _n_(380834, "Column", lambda: Column), _c_(380836, _n_(380835, "String", lambda: String), 200), nullable=False)
    _l_(380838)
    collection_id = _c_(380843, _n_(380839, "Column", lambda: Column), _n_(380840, "Integer", lambda: Integer), _c_(380842, _n_(380841, "ForeignKey", lambda: ForeignKey), 'collection.id'))
    _l_(380844)

def main():
    _l_(380867)

    base_name = 'test.db'
    _l_(380846)
    engine = _c_(380851, _n_(380847, "create_engine", lambda: create_engine), _c_(380850, _a_(380848, 'sqlite:///{}', "format"), _n_(380849, "base_name", lambda: base_name)))
    _l_(380852)
    session = _c_(380854, _n_(380853, "sessionmaker", lambda: sessionmaker))
    _l_(380855)
    _c_(380859, _a_(380857, _n_(380856, "session", lambda: session), "configure"), bind=_n_(380858, "engine", lambda: engine))
    _l_(380860)
    _c_(380865, _a_(380863, _a_(380862, _n_(380861, "Base", lambda: Base), "metadata"), "create_all"), _n_(380864, "engine", lambda: engine))
    _l_(380866)

if _n_(380868, "__name__", lambda: __name__) == "__main__":
    _l_(380872)

    _c_(380870, _n_(380869, "main", lambda: main))
    _l_(380871)