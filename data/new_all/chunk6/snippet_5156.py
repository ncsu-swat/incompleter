# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73786094/error-attributeerror-connection-object-has-no-attribute-fetchall
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
db_engine = _c_(361817, _a_(361814, _n_(361813, "extrac_db", lambda: extrac_db), "create_engine"), _a_(361816, _n_(361815, "Config", lambda: Config), "db_uri"))
_l_(361818)
db_connection = _c_(361821, _a_(361820, _n_(361819, "db_engine", lambda: db_engine), "connect"))
_l_(361822)