# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71450772/flask-pytest-failed-tests-test-data-response-pytest-post-data-response-type
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(585182, _a_(585181, _n_(585180, "discovery_bp", lambda: discovery_bp), "route"), '/', methods=['GET', 'POST'])
def search_fund():
    _l_(585212)

    """ 
    Given function creates a text field for search box &
    renders on index.html then 
    retrieves input data from the user, run that data through 
    function query_fund from data.py to grab the fund 
    & renders back onto index.html 
    """
    form = _c_(585184, _n_(585183, "SearchForm", lambda: SearchForm))
    _l_(585185)
    if _c_(585188, _a_(585187, _n_(585186, "form", lambda: form), "validate_on_submit")):
        _l_(585207)

        query = _c_(585193, _a_(585192, _a_(585191, _a_(585190, _n_(585189, "form", lambda: form), "search"), "data"), "split"), " ")
        _l_(585194)
        fund_results = _c_(585199, _n_(585195, "query_fund", lambda: query_fund), _n_(585196, "query", lambda: query), f"{_n_(585197, 'FUND_STORE_API_HOST', lambda: FUND_STORE_API_HOST)}/{_n_(585198, 'FUND_ENDPOINT', lambda: FUND_ENDPOINT)}")
        _l_(585200)
        aux = _c_(585205, _n_(585201, "render_template", lambda: render_template), "search.html", query =_n_(585202, "query", lambda: query), 
                              fund_results = _n_(585203, "fund_results", lambda: fund_results),
                              form=_n_(585204, "form", lambda: form))
        _l_(585206)
        return aux
    aux = _c_(585210, _n_(585208, "render_template", lambda: render_template), "search.html", form=_n_(585209, "form", lambda: form))    
    _l_(585211)    
    return aux    