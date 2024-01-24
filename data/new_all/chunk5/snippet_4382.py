# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58815778/pytest-stop-runnig-with-attributeerror-module-html-has-no-attribute-td-in-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(704095)

except ImportError:
    pass
try:
    import html.parser
    _l_(704097)

except ImportError:
    pass
try:
    import pytest
    _l_(704099)

except ImportError:
    pass

@_a_(704102, _a_(704101, _n_(704100, "pytest", lambda: pytest), "mark"), "optionalhook")
def pytest_html_results_table_header(cells):
    _l_(704121)

    _c_(704108, _a_(704104, _n_(704103, "cells", lambda: cells), "insert"), 2, _c_(704107, _a_(704106, _n_(704105, "html", lambda: html), "th"), 'Status_code'))
    _l_(704109)
    _c_(704115, _a_(704111, _n_(704110, "cells", lambda: cells), "insert"), 1, _c_(704114, _a_(704113, _n_(704112, "html", lambda: html), "th"), 'Time', class_='sortable time', col='time'))
    _l_(704116)
    _c_(704119, _a_(704118, _n_(704117, "cells", lambda: cells), "pop"))
    _l_(704120)

@_a_(704124, _a_(704123, _n_(704122, "pytest", lambda: pytest), "mark"), "optionalhook")
def pytest_html_results_table_row(report, cells):
    _l_(704148)

    _c_(704132, _a_(704126, _n_(704125, "cells", lambda: cells), "insert"), 2, _c_(704131, _a_(704128, _n_(704127, "html", lambda: html), "td"), _a_(704130, _n_(704129, "report", lambda: report), "status_code")))
    _l_(704133)
    _c_(704142, _a_(704135, _n_(704134, "cells", lambda: cells), "insert"), 1, _c_(704141, _a_(704137, _n_(704136, "html", lambda: html), "td"), _c_(704140, _a_(704139, _n_(704138, "datetime", lambda: datetime), "utcnow")), class_='col-time'))
    _l_(704143)
    _c_(704146, _a_(704145, _n_(704144, "cells", lambda: cells), "pop"))
    _l_(704147)

@_a_(704151, _a_(704150, _n_(704149, "pytest", lambda: pytest), "mark"), "hookwrapper")
def pytest_runtest_makereport(item, call):
    _l_(704157)

    outcome = yield
    _l_(704152)
    report = _c_(704155, _a_(704154, _n_(704153, "outcome", lambda: outcome), "get_result"))
    _l_(704156)