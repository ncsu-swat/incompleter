# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52166054/typeerror-the-first-argument-must-be-callable-when-i-import-a-scheduler-in-my-v
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(414234)
try:
    from django.shortcuts import render
    _l_(414236)

except ImportError:
    pass
try:
    from django.utils import timezone
    _l_(414238)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(414240)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(414242)

except ImportError:
    pass
try:
    import requests
    _l_(414244)

except ImportError:
    pass
try:
    import schedule
    _l_(414246)

except ImportError:
    pass
try:
    import time
    _l_(414248)

except ImportError:
    pass


def republic(request):
    _l_(414252)

    aux = _c_(414250, _n_(414249, "HttpResponse", lambda: HttpResponse), "<h1>Success Hindustan</h1>")
    _l_(414251)
    return aux


def indiatv(request):
    _l_(414256)

    aux = _c_(414254, _n_(414253, "HttpResponse", lambda: HttpResponse), "<h1>Success Hindustan</h1>")
    _l_(414255)
    return aux

def ndtv(request):
    _l_(414260)

    aux = _c_(414258, _n_(414257, "HttpResponse", lambda: HttpResponse), "<h1>Success NDTV</h1>")
    _l_(414259)
    return aux


_c_(414271, _a_(414267, _c_(414266, _a_(414265, _a_(414264, _c_(414263, _a_(414262, _n_(414261, "schedule", lambda: schedule), "every")), "day"), "at"), "17:19"), "do"), _c_(414270, _n_(414268, "republic", lambda: republic), _n_(414269, "requests", lambda: requests)))
_l_(414272)
_c_(414283, _a_(414279, _c_(414278, _a_(414277, _a_(414276, _c_(414275, _a_(414274, _n_(414273, "schedule", lambda: schedule), "every")), "day"), "at"), "17:19"), "do"), _c_(414282, _n_(414280, "indiatv", lambda: indiatv), _n_(414281, "requests", lambda: requests)))
_l_(414284)
_c_(414295, _a_(414291, _c_(414290, _a_(414289, _a_(414288, _c_(414287, _a_(414286, _n_(414285, "schedule", lambda: schedule), "every")), "day"), "at"), "17:19"), "do"), _c_(414294, _n_(414292, "ndtv", lambda: ndtv), _n_(414293, "requests", lambda: requests)))
_l_(414296)

while 1:
    _l_(414305)

    _c_(414299, _a_(414298, _n_(414297, "schedule", lambda: schedule), "run_pending"))
    _l_(414300)
    _c_(414303, _a_(414302, _n_(414301, "time", lambda: time), "sleep"), 1)
    _l_(414304)