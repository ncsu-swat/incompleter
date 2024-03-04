# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/22604564/create-pandas-dataframe-from-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import io
    _l_(64298)

except ImportError:
    pass
try:
    import re
    _l_(64300)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(64302)

except ImportError:
    pass


def read_psv(str_input: _n_(64303, "str", lambda: str), **kwargs) -> _a_(64305, _n_(64304, "pd", lambda: pd), "DataFrame"):
    _l_(64349)

    """Read a Pandas object from a pipe-separated table contained within a string.

    Input example:
        | int_score | ext_score | eligible |
        |           | 701       | True     |
        | 221.3     | 0         | False    |
        |           | 576       | True     |
        | 300       | 600       | True     |

    The leading and trailing pipes are optional, but if one is present,
    so must be the other.

    `kwargs` are passed to `read_csv`. They must not include `sep`.

    In PyCharm, the "Pipe Table Formatter" plugin has a "Format" feature that can 
    be used to neatly format a table.

    Ref: https://stackoverflow.com/a/46471952/
    """

    substitutions = [
        ('^ *', ''),  # Remove leading spaces
        (' *$', ''),  # Remove trailing spaces
        (r' *\| *', '|'),  # Remove spaces between columns
    ]
    _l_(64306)
    if _c_(64323, _n_(64307, "all", lambda: all), (_c_(64312, _a_(64311, _c_(64310, _a_(64309, _n_(64308, "line", lambda: line), "lstrip")), "startswith"), '|') and _c_(64317, _a_(64316, _c_(64315, _a_(64314, _n_(64313, "line", lambda: line), "rstrip")), "endswith"), '|') for line in _c_(64322, _a_(64321, _c_(64320, _a_(64319, _n_(64318, "str_input", lambda: str_input), "strip")), "split"), '\n'))):
        _l_(64328)

        _c_(64326, _a_(64325, _n_(64324, "substitutions", lambda: substitutions), "extend"), [
            (r'^\|', ''),  # Remove redundant leading delimiter
            (r'\|$', ''),  # Remove redundant trailing delimiter
        ])
        _l_(64327)
    for pattern, replacement in _n_(64329, "substitutions", lambda: substitutions):
        _l_(64339)

        str_input = _c_(64337, _a_(64331, _n_(64330, "re", lambda: re), "sub"), _n_(64332, "pattern", lambda: pattern), _n_(64333, "replacement", lambda: replacement), _n_(64334, "str_input", lambda: str_input), flags=_a_(64336, _n_(64335, "re", lambda: re), "MULTILINE"))
        _l_(64338)
    aux = _c_(64347, _a_(64341, _n_(64340, "pd", lambda: pd), "read_csv"), _c_(64345, _a_(64343, _n_(64342, "io", lambda: io), "StringIO"), _n_(64344, "str_input", lambda: str_input)), sep='|', **_n_(64346, "kwargs", lambda: kwargs))
    _l_(64348)
    return aux


df = _c_(64356, _a_(64351, _n_(64350, "pd", lambda: pd), "read_csv"), _c_(64355, _a_(64353, _n_(64352, "io", lambda: io), "StringIO"), _n_(64354, "df_str", lambda: df_str)), sep=r'\s*\|\s*', engine='python')
_l_(64357)

