# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75889310/attributeerror-testorders-object-has-no-attribute-token
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from API_project.Requests.api_clients import *
    _l_(589122)

except ImportError:
    pass
try:
    import unittest
    _l_(589124)

except ImportError:
    pass

class TestOrders(_a_(589126, _n_(589125, "unittest", lambda: unittest), "TestCase")):
    _l_(589166)


    def setup_method(self):
        _l_(589131)

        _n_(589127, "self", lambda: self).token = _c_(589129, _n_(589128, "get_token", lambda: get_token))
        _l_(589130)

    def test_add_order_book_out_of_stock(self):
        _l_(589144)

        response = _c_(589135, _n_(589132, "add_order", lambda: add_order), _a_(589134, _n_(589133, "self", lambda: self), "token"), 2, '100 years in prison - fiction')
        _l_(589136)
        assert _a_(589138, _n_(589137, "response", lambda: response), "status_code") == 404, 'Status code is not correct'
        _l_(589139)
        assert _c_(589142, _a_(589141, _n_(589140, "response", lambda: response), "json"))['error'] == 'This book is not in stock. Try again later.'
        _l_(589143)

    def test_add_valid_order(self):
        _l_(589165)

        response = _c_(589148, _n_(589145, "add_order", lambda: add_order), _a_(589147, _n_(589146, "self", lambda: self), "token"), 1, '1% rule')
        _l_(589149)
        assert _a_(589151, _n_(589150, "response", lambda: response), "status_code") == 201, 'Status code is not correct'
        _l_(589152)
        assert _c_(589155, _a_(589154, _n_(589153, "response", lambda: response), "json"))['created'] is True, 'Order not created'
        _l_(589156)
        # cleanup
        _c_(589163, _n_(589157, "delete_order", lambda: delete_order), _a_(589159, _n_(589158, "self", lambda: self), "token"), _c_(589162, _a_(589161, _n_(589160, "response", lambda: response), "json"))['orderId'])
        _l_(589164)