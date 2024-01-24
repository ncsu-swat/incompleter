# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68603734/pandas-error-typeerror-bad-operand-type-for-unary-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dummy_data1 = {
    'id': ['1', '2', '3', '4', '5'],
    'Feature1': ['A', 'C', 'E', 'G', 'I'],
    'Feature2': ['Mouse', 'dog', 'house and parrot', '23', _a_(545286, _n_(545285, "np", lambda: np), "NaN")],
    'dates': ['12/12/2020','12/12/2020','12/12/2020','12/12/2020','12/12/2020']}
_l_(545287)

df1 = _c_(545291, _a_(545289, _n_(545288, "pd", lambda: pd), "DataFrame"), _n_(545290, "dummy_data1", lambda: dummy_data1), columns = ['id', 'Feature1', 'Feature2', 'dates'])
_l_(545292)

df1 = _c_(545311, _a_(545294, _n_(545293, "df1", lambda: df1), "assign"), Feature2=lambda df: _c_(545310, _a_(545297, _a_(545296, _n_(545295, "df", lambda: df), "Feature2"), "where"), ~_c_(545302, _a_(545301, _a_(545300, _a_(545299, _n_(545298, "df", lambda: df), "Feature2"), "str"), "isnumeric")),
                        _c_(545309, _a_(545308, _c_(545307, _a_(545304, _n_(545303, "pd", lambda: pd), "to_numeric"), _a_(545306, _n_(545305, "df", lambda: df), "Feature2"), errors="coerce"), "astype"), "Int64"),
                    )
    )
_l_(545312)
    
_c_(545315, _n_(545313, "print", lambda: print), _n_(545314, "df1", lambda: df1))
_l_(545316)