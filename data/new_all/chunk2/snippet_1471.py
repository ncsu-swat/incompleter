# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54803231/how-to-fix-attributeerror-environments-in-odoo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import skpy
    _l_(470215)

except ImportError:
    pass
try:
    import logging
    _l_(470217)

except ImportError:
    pass
try:
    import threading
    _l_(470219)

except ImportError:
    pass
try:
    import odoo
    _l_(470221)

except ImportError:
    pass

DB_NAME = 'odootest'
_l_(470222)
UID = _a_(470224, _n_(470223, "odoo", lambda: odoo), "SUPERUSER_ID")
_l_(470225)

_logger = _c_(470229, _a_(470227, _n_(470226, "logging", lambda: logging), "getLogger"), _n_(470228, "__name__", lambda: __name__))
_l_(470230)


registry = _c_(470237, _a_(470235, _a_(470234, _a_(470233, _a_(470232, _n_(470231, "odoo", lambda: odoo), "modules"), "registry"), "Registry"), "new"), _n_(470236, "DB_NAME", lambda: DB_NAME))
_l_(470238)
CR = _c_(470241, _a_(470240, _n_(470239, "registry", lambda: registry), "cursor"))
_l_(470242)
ENV = _c_(470248, _a_(470245, _a_(470244, _n_(470243, "odoo", lambda: odoo), "api"), "Environment"), _n_(470246, "CR", lambda: CR), _n_(470247, "UID", lambda: UID), {})
_l_(470249)


class MySkype(_a_(470251, _n_(470250, "skpy", lambda: skpy), "SkypeEventLoop")):
    _l_(470340)


    def onEvent(self, event):
        _l_(470339)

        if _c_(470256, _n_(470252, "isinstance", lambda: isinstance), _n_(470253, "event", lambda: event), _a_(470255, _n_(470254, "skpy", lambda: skpy), "SkypeNewMessageEvent")):
            _l_(470338)

            _c_(470259, _a_(470258, _n_(470257, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470260)
            _c_(470264, _a_(470262, _n_(470261, "_logger", lambda: _logger), "warning"), _n_(470263, "event", lambda: event))
            _l_(470265)
            _c_(470268, _a_(470267, _n_(470266, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470269)

            message = _c_(470282, _a_(470270, 'New message from user {} at {}: \'{} \'', "format"), _a_(470273, _a_(470272, _n_(470271, "event", lambda: event), "msg"), "userId"),
                                                                     _c_(470278, _a_(470277, _a_(470276, _a_(470275, _n_(470274, "event", lambda: event), "msg"), "time"), "strftime"), '%H:%M dd. %d.%m.%Y'),
                                                                     _a_(470281, _a_(470280, _n_(470279, "event", lambda: event), "msg"), "content"))
            _l_(470283)

            _c_(470286, _a_(470285, _n_(470284, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470287)
            _c_(470291, _a_(470289, _n_(470288, "_logger", lambda: _logger), "warning"), _n_(470290, "message", lambda: message))
            _l_(470292)
            _c_(470295, _a_(470294, _n_(470293, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470296)

            partner_id = _a_(470301, _a_(470300, _c_(470299, _a_(470298, _n_(470297, "ENV", lambda: ENV)['res.users'], "search"), [('id', '=', 2)]), "partner_id"), "id")
            _l_(470302)

            _c_(470305, _a_(470304, _n_(470303, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470306)
            _c_(470310, _a_(470308, _n_(470307, "_logger", lambda: _logger), "warning"), _n_(470309, "partner_id", lambda: partner_id))
            _l_(470311)
            _c_(470314, _a_(470313, _n_(470312, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470315)

            _c_(470324, _a_(470317, _n_(470316, "ENV", lambda: ENV)['mail.message'], "create"), {'message_type': 'notification',
                                             'subtype': _a_(470321, _c_(470320, _a_(470319, _n_(470318, "ENV", lambda: ENV), "ref"), 'mail.mt_comment'), "id"),
                                             'body': _n_(470322, "message", lambda: message),
                                             'subject': 'Message subject',
                                             'partner_ids': [(4, _n_(470323, "partner_id", lambda: partner_id)), ],
                                             })
            _l_(470325)
            _c_(470328, _a_(470327, _n_(470326, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470329)
            _c_(470332, _a_(470331, _n_(470330, "_logger", lambda: _logger), "warning"), 'send')
            _l_(470333)
            _c_(470336, _a_(470335, _n_(470334, "_logger", lambda: _logger), "info"), '--------' * 5)
            _l_(470337)


sk = _c_(470342, _n_(470341, "MySkype", lambda: MySkype), '+3767', '12qW', autoAck=True)
_l_(470343)
thread = _c_(470348, _a_(470345, _n_(470344, "threading", lambda: threading), "Thread"), target=_a_(470347, _n_(470346, "sk", lambda: sk), "loop"))
_l_(470349)
_c_(470352, _a_(470351, _n_(470350, "thread", lambda: thread), "start"))
_l_(470353)