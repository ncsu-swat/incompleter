# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41883486/datatype-mismatch-beautifulsoup-typeerror-unhashable-type-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
jobs_by_city = [
'http://boston.website.org/search/widget',
]
_l_(699388)

job_kw = [['web site','user', 'account'],['permission', 'name']]
_l_(699389)
job_kw = _c_(699392, _n_(699390, "sum", lambda: sum), _n_(699391, "job_kw", lambda: job_kw), [])
_l_(699393)

jobs = []
_l_(699394)

for job_in_city in _n_(699395, "jobs_by_city", lambda: jobs_by_city):
    _l_(699422)

    a_job = _c_(699399, _a_(699397, _n_(699396, "requests", lambda: requests), "get"), _n_(699398, "job_in_city", lambda: job_in_city))
    _l_(699400)
    soup = _c_(699404, _n_(699401, "BeautifulSoup", lambda: BeautifulSoup), _a_(699403, _n_(699402, "a_job", lambda: a_job), "text"), "lxml")
    _l_(699405)
    for a in _c_(699414, _a_(699407, _n_(699406, "soup", lambda: soup), "find_all"), 'a', class_="result-title hdrlnk", text=_c_(699413, _a_(699409, _n_(699408, "re", lambda: re), "compile"), _n_(699410, "job_kw", lambda: job_kw),_a_(699412, _n_(699411, "re", lambda: re), "IGNORECASE"))):
        _l_(699421)

        _c_(699419, _n_(699415, "print", lambda: print), _c_(699418, _a_(699417, _n_(699416, "a", lambda: a), "get"), 'href'))
        _l_(699420)