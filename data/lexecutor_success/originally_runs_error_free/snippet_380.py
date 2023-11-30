# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6130768/return-a-default-value-if-a-dictionary-key-is-not-available
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_dict = {'level_1': {
             'level_2': {
                  'level_3': 'more_data'
                  }
              }
           }
_l_(1539609)
result = _c_(1539616, _a_(1539615, _c_(1539614, _a_(1539613, _c_(1539612, _a_(1539611, _n_(1539610, "my_dict", lambda: my_dict), "get"), 'level_1', {}), "get"), 'level_2', {}), "get"), 'level_3')
_l_(1539617)
# result -> 'more_data'
none_result = _c_(1539624, _a_(1539623, _c_(1539622, _a_(1539621, _c_(1539620, _a_(1539619, _n_(1539618, "my_dict", lambda: my_dict), "get"), 'level_1', {}), "get"), 'what_level', {}), "get"), 'level_3')
_l_(1539625)
# none_result -> None

