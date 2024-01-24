# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58815778/pytest-stop-runnig-with-attributeerror-module-html-has-no-attribute-td-in-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(677457)

except ImportError:
    pass
try:
    import html.parser
    _l_(677459)

except ImportError:
    pass
try:
    import pytest
    _l_(677461)

except ImportError:
    pass

@_a_(677464, _a_(677463, _n_(677462, "pytest", lambda: pytest), "mark"), "optionalhook")
def pytest_html_results_table_header(cells):
    _l_(677483)

    _c_(677470, _a_(677466, _n_(677465, "cells", lambda: cells), "insert"), 2, _c_(677469, _a_(677468, _n_(677467, "html", lambda: html), "th"), 'Status_code'))
    _l_(677471)
    _c_(677477, _a_(677473, _n_(677472, "cells", lambda: cells), "insert"), 1, _c_(677476, _a_(677475, _n_(677474, "html", lambda: html), "th"), 'Time', class_='sortable time', col='time'))
    _l_(677478)
    _c_(677481, _a_(677480, _n_(677479, "cells", lambda: cells), "pop"))
    _l_(677482)

@_a_(677486, _a_(677485, _n_(677484, "pytest", lambda: pytest), "mark"), "optionalhook")
def pytest_html_results_table_row(report, cells):
    _l_(677510)

    _c_(677494, _a_(677488, _n_(677487, "cells", lambda: cells), "insert"), 2, _c_(677493, _a_(677490, _n_(677489, "html", lambda: html), "td"), _a_(677492, _n_(677491, "report", lambda: report), "status_code")))
    _l_(677495)
    _c_(677504, _a_(677497, _n_(677496, "cells", lambda: cells), "insert"), 1, _c_(677503, _a_(677499, _n_(677498, "html", lambda: html), "td"), _c_(677502, _a_(677501, _n_(677500, "datetime", lambda: datetime), "utcnow")), class_='col-time'))
    _l_(677505)
    _c_(677508, _a_(677507, _n_(677506, "cells", lambda: cells), "pop"))
    _l_(677509)

@_a_(677513, _a_(677512, _n_(677511, "pytest", lambda: pytest), "mark"), "hookwrapper")
def pytest_runtest_makereport(item, call):
    _l_(677519)

    outcome = yield
    _l_(677514)
    report = _c_(677517, _a_(677516, _n_(677515, "outcome", lambda: outcome), "get_result"))
    _l_(677518)