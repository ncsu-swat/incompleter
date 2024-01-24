# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74135982/python-calling-mutiple-my-own-functions-nameerror-not-defined-on-passing-ou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Iser_upd_qur_del_function import *
    _l_(372194)

except ImportError:
    pass

ip_input = _c_(372196, _n_(372195, "input", lambda: input), "Enter the ip: ")
_l_(372197)
exist_DB_name = _c_(372199, _n_(372198, "input", lambda: input), "Enter exist DB name: ")
_l_(372200)
exist_coll_name = _c_(372202, _n_(372201, "input", lambda: input), "Enter exist collection name: ")
_l_(372203)
mydb, mycol  = _c_(372208, _n_(372204, "init_db", lambda: init_db), _n_(372205, "ip_input", lambda: ip_input), _n_(372206, "exist_DB_name", lambda: exist_DB_name), _n_(372207, "exist_coll_name", lambda: exist_coll_name))
_l_(372209)

myquery_str = _c_(372211, _n_(372210, "input", lambda: input), "Enter ur query: ")
_l_(372212)
update_one_or_many = _c_(372214, _n_(372213, "input", lambda: input), "U are update one or many values? (ex:1 for many , 0 for one): ")
_l_(372215)
newvalues_str = _c_(372217, _n_(372216, "input", lambda: input), "Enter new values: ")
_l_(372218)

one_or_many_bool = _c_(372223, _n_(372219, "bool", lambda: bool), _c_(372222, _n_(372220, "int", lambda: int), _n_(372221, "update_one_or_many", lambda: update_one_or_many)))
_l_(372224)

myquery_json =_c_(372228, _a_(372226, _n_(372225, "json", lambda: json), "loads"), _n_(372227, "myquery_str", lambda: myquery_str))
_l_(372229)
newvalues_json =_c_(372233, _a_(372231, _n_(372230, "json", lambda: json), "loads"), _n_(372232, "newvalues_str", lambda: newvalues_str))
_l_(372234)
x = _c_(372239, _n_(372235, "change_db_data", lambda: change_db_data), _n_(372236, "myquery_json", lambda: myquery_json), _n_(372237, "newvalues_json", lambda: newvalues_json), _n_(372238, "one_or_many_bool", lambda: one_or_many_bool))
_l_(372240)
_c_(372243, _n_(372241, "print", lambda: print), _n_(372242, "x", lambda: x))
_l_(372244)
_c_(372248, _n_(372245, "print", lambda: print), _a_(372247, _n_(372246, "x", lambda: x), "modified_count"), "documents updated.")
_l_(372249)