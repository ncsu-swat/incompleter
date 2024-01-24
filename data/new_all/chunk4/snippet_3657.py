# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70546376/any-way-to-fix-this-typeerror-a-bytes-like-object-is-required-not-str-when-o
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(639151, _n_(639150, "open", lambda: open), "final_project_dataset.pkl", "rb") as data_file:
        _l_(639157)

        data_dict = _c_(639155, _a_(639153, _n_(639152, "pickle", lambda: pickle), "load"), _n_(639154, "data_file", lambda: data_file), encoding='utf8')
        _l_(639156)