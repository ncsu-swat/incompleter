# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53383631/nameerror-for-variable-that-i-wont-have-value-for-until-runtime
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
all_fields_dict = {
    'users':
       {
        'first_name': {
            'db_field' : 'FirstName',
            'datatype': 'varchar(50)',
            'test_value': {_c_(664294, _a_(664293, _n_(664292, "utils", lambda: utils), "calc_field_value"), ['zfill', 'FirstName'])}, # another attempt that didn't work
            'num_bool': False
        },
        'username': {
            'db_field' : 'username',
            'datatype': 'varchar(50)',
            'test_value': f"user{_c_(664297, _a_(664296, _n_(664295, 'utils', lambda: utils), 'get_random_str'), 5)}", # this works, but it's a diff kind of calculation
            'num_bool': False,
        },
        'description': {
            'db_field' : 'description',
            'datatype': 'text',
            'test_value': f"{_c_(664301, _a_(664299, _n_(664298, 'utils', lambda: utils), 'get_desc_info'), _n_(664300, 'row_num', lambda: row_num))}", # one of my attempts - fails
            'num_bool': False,
        },
   }
}
_l_(664302)