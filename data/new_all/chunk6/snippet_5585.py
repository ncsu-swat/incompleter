# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74135982/python-calling-mutiple-my-own-functions-nameerror-not-defined-on-passing-ou
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Iser_upd_qur_del_function import *
    _l_(340469)

except ImportError:
    pass

ip_input = _c_(340471, _n_(340470, "input", lambda: input), "Enter the ip: ")
_l_(340472)
exist_DB_name = _c_(340474, _n_(340473, "input", lambda: input), "Enter exist DB name: ")
_l_(340475)
exist_coll_name = _c_(340477, _n_(340476, "input", lambda: input), "Enter exist collection name: ")
_l_(340478)
mydb, mycol  = _c_(340483, _n_(340479, "init_db", lambda: init_db), _n_(340480, "ip_input", lambda: ip_input), _n_(340481, "exist_DB_name", lambda: exist_DB_name), _n_(340482, "exist_coll_name", lambda: exist_coll_name))
_l_(340484)

myquery_str = _c_(340486, _n_(340485, "input", lambda: input), "Enter ur query: ")
_l_(340487)
update_one_or_many = _c_(340489, _n_(340488, "input", lambda: input), "U are update one or many values? (ex:1 for many , 0 for one): ")
_l_(340490)
newvalues_str = _c_(340492, _n_(340491, "input", lambda: input), "Enter new values: ")
_l_(340493)

one_or_many_bool = _c_(340498, _n_(340494, "bool", lambda: bool), _c_(340497, _n_(340495, "int", lambda: int), _n_(340496, "update_one_or_many", lambda: update_one_or_many)))
_l_(340499)

myquery_json =_c_(340503, _a_(340501, _n_(340500, "json", lambda: json), "loads"), _n_(340502, "myquery_str", lambda: myquery_str))
_l_(340504)
newvalues_json =_c_(340508, _a_(340506, _n_(340505, "json", lambda: json), "loads"), _n_(340507, "newvalues_str", lambda: newvalues_str))
_l_(340509)
x = _c_(340514, _n_(340510, "change_db_data", lambda: change_db_data), _n_(340511, "myquery_json", lambda: myquery_json), _n_(340512, "newvalues_json", lambda: newvalues_json), _n_(340513, "one_or_many_bool", lambda: one_or_many_bool))
_l_(340515)
_c_(340518, _n_(340516, "print", lambda: print), _n_(340517, "x", lambda: x))
_l_(340519)
_c_(340523, _n_(340520, "print", lambda: print), _a_(340522, _n_(340521, "x", lambda: x), "modified_count"), "documents updated.")
_l_(340524)