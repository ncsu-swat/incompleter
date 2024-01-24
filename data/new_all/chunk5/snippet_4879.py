# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41883486/datatype-mismatch-beautifulsoup-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
jobs_by_city = [
'http://boston.website.org/search/widget',
]
_l_(646628)

job_kw = [['web site','user', 'account'],['permission', 'name']]
_l_(646629)
job_kw = _c_(646632, _n_(646630, "sum", lambda: sum), _n_(646631, "job_kw", lambda: job_kw), [])
_l_(646633)

jobs = []
_l_(646634)

for job_in_city in _n_(646635, "jobs_by_city", lambda: jobs_by_city):
    _l_(646662)

    a_job = _c_(646639, _a_(646637, _n_(646636, "requests", lambda: requests), "get"), _n_(646638, "job_in_city", lambda: job_in_city))
    _l_(646640)
    soup = _c_(646644, _n_(646641, "BeautifulSoup", lambda: BeautifulSoup), _a_(646643, _n_(646642, "a_job", lambda: a_job), "text"), "lxml")
    _l_(646645)
    for a in _c_(646654, _a_(646647, _n_(646646, "soup", lambda: soup), "find_all"), 'a', class_="result-title hdrlnk", text=_c_(646653, _a_(646649, _n_(646648, "re", lambda: re), "compile"), _n_(646650, "job_kw", lambda: job_kw),_a_(646652, _n_(646651, "re", lambda: re), "IGNORECASE"))):
        _l_(646661)

        _c_(646659, _n_(646655, "print", lambda: print), _c_(646658, _a_(646657, _n_(646656, "a", lambda: a), "get"), 'href'))
        _l_(646660)