# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50037254/pathaccounts-includeaccounts-urls-nameerror-name-accounts-is-not-def
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.contrib import admin
    _l_(475007)

except ImportError:
    pass
try:
    from django.urls import path, include
    _l_(475009)

except ImportError:
    pass
try:
    from products import views
    _l_(475011)

except ImportError:
    pass

urlpatterns = [
    _c_(475016, _n_(475012, "path", lambda: path), 'admin/', _a_(475015, _a_(475014, _n_(475013, "admin", lambda: admin), "site"), "urls")),
    _c_(475020, _n_(475017, "path", lambda: path), '', _a_(475019, _n_(475018, "views", lambda: views), "home"), name="home"),
    _c_(475026, _n_(475021, "path", lambda: path), 'accounts/', _c_(475025, _n_(475022, "include", lambda: include), _a_(475024, _n_(475023, "accounts", lambda: accounts), "urls"))),
]
_l_(475027)