# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42019886/python-3-mechanical-soup-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
browser = _c_(669007, _a_(669006, _n_(669005, "mechanicalsoup", lambda: mechanicalsoup), "Browser"))
_l_(669008)

# Request page
login_page = _c_(669011, _a_(669010, _n_(669009, "browser", lambda: browser), "get"), "https://www.website.com/login")
_l_(669012)

login_form = _c_(669016, _a_(669015, _a_(669014, _n_(669013, "login_page", lambda: login_page), "soup"), "find"), "form", {"id":"login"})
_l_(669017)

# specify username and password
_c_(669020, _a_(669019, _n_(669018, "login_form", lambda: login_form), "find"), "input", {"id": "username"})["value"] = 'myUsername'
_l_(669021)
_c_(669024, _a_(669023, _n_(669022, "login_form", lambda: login_form), "find"), "input", {"id": "password"})["value"] = 'myPassword'
_l_(669025)

# submit form
response = _c_(669031, _a_(669027, _n_(669026, "browser", lambda: browser), "submit"), _n_(669028, "login_form", lambda: login_form), _a_(669030, _n_(669029, "login_page", lambda: login_page), "url"))
_l_(669032)