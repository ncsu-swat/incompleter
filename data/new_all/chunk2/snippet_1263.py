# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59633827/why-does-my-script-return-attributeerror-str-object-has-no-attribute-append
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from observations.constants import PROJECTS_DB_ID
    _l_(444602)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(444604)

except ImportError:
    pass
try:
    from dateutil.relativedelta import relativedelta
    _l_(444606)

except ImportError:
    pass

def get(gs_client):
    _l_(444707)

    #Sheet access
    sheet = _c_(444612, _a_(444611, _c_(444610, _a_(444608, _n_(444607, "gs_client", lambda: gs_client), "open_by_key"), _n_(444609, "PROJECTS_DB_ID", lambda: PROJECTS_DB_ID)), "worksheet"), 'Finance')
    _l_(444613)

    #Columns necessary
    projects = _c_(444616, _a_(444615, _n_(444614, "sheet", lambda: sheet), "col_values"), 1)[2:]
    _l_(444617)
    months = _c_(444620, _a_(444619, _n_(444618, "sheet", lambda: sheet), "col_values"), 2)[2:]
    _l_(444621)
    profit = _c_(444624, _a_(444623, _n_(444622, "sheet", lambda: sheet), "col_values"), 11)[2:]
    _l_(444625)
    revenue = _c_(444628, _a_(444627, _n_(444626, "sheet", lambda: sheet), "col_values"), 6)[2:]
    _l_(444629)
    last_modified = _c_(444632, _a_(444631, _n_(444630, "sheet", lambda: sheet), "col_values"), 13)[2:]
    _l_(444633)

    #Lists
    list_projects = []
    _l_(444634)
    list_months = []
    _l_(444635)
    list_profit = []
    _l_(444636)
    list_revenue = []
    _l_(444637)
    list_last_modified = []
    _l_(444638)
    value = []
    _l_(444639)

    #Gets each project
    for project in _n_(444640, "projects", lambda: projects):
        _l_(444646)

        _c_(444644, _a_(444642, _n_(444641, "list_projects", lambda: list_projects), "append"), _n_(444643, "project", lambda: project))
        _l_(444645)

    #Gets each month
    for month in _n_(444647, "months", lambda: months):
        _l_(444653)

        _c_(444651, _a_(444649, _n_(444648, "list_months", lambda: list_months), "append"), _n_(444650, "month", lambda: month))
        _l_(444652)

    #Gets each value of profit column
    for val in _n_(444654, "profit", lambda: profit):
        _l_(444664)

        _c_(444662, _a_(444656, _n_(444655, "list_profit", lambda: list_profit), "append"), _c_(444661, _a_(444660, _c_(444659, _a_(444658, _n_(444657, "val", lambda: val), "strip"), '$'), "replace"), ',',''))
        _l_(444663)

    #Gets each value in revenue column
    for value in _n_(444665, "revenue", lambda: revenue):
        _l_(444675)

        _c_(444673, _a_(444667, _n_(444666, "list_revenue", lambda: list_revenue), "append"), _c_(444672, _a_(444671, _c_(444670, _a_(444669, _n_(444668, "value", lambda: value), "strip"), '$'), "replace"), ',',''))
        _l_(444674)

    #Gets each date in last modified column
    for update in _n_(444676, "last_modified", lambda: last_modified):
        _l_(444682)

        _c_(444680, _a_(444678, _n_(444677, "list_last_modified", lambda: list_last_modified), "append"), _n_(444679, "update", lambda: update))
        _l_(444681)

    #Get profitability per project (profit divided by revenue)
    for x in _c_(444687, _n_(444683, "range", lambda: range), _c_(444686, _n_(444684, "len", lambda: len), _n_(444685, "projects", lambda: projects))):
        _l_(444702)

        value1 = _c_(444691, _n_(444688, "float", lambda: float), _n_(444689, "list_profit", lambda: list_profit)[_n_(444690, "x", lambda: x)])/_c_(444695, _n_(444692, "float", lambda: float), _n_(444693, "list_revenue", lambda: list_revenue)[_n_(444694, "x", lambda: x)])
        _l_(444696)
        _c_(444700, _a_(444698, _n_(444697, "value", lambda: value), "append"), _n_(444699, "value1", lambda: value1))
        _l_(444701)

    _c_(444705, _n_(444703, "print", lambda: print), _n_(444704, "value", lambda: value))
    _l_(444706)