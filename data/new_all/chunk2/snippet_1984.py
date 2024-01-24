# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73217356/with-headersection-attributeerror-enter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import streamlit as st
    _l_(421190)

except ImportError:
    pass
try:
    from user import login
    _l_(421192)

except ImportError:
    pass

headerSection = _a_(421194, _n_(421193, "st", lambda: st), "container")
_l_(421195)
mainSection = _a_(421197, _n_(421196, "st", lambda: st), "container")
_l_(421198)
loginSection = _a_(421200, _n_(421199, "st", lambda: st), "container")
_l_(421201)
logoutSection = _a_(421203, _n_(421202, "st", lambda: st), "container")
_l_(421204)

def main_page():
    _l_(421211)

    with _n_(421205, "mainSection", lambda: mainSection):
        _l_(421210)

        _c_(421208, _a_(421207, _n_(421206, "st", lambda: st), "text"), "Things to do")
        _l_(421209)

def loggedOut_clicked():
    _l_(421215)

    _a_(421213, _n_(421212, "st", lambda: st), "session_state")['loggedIn'] = False
    _l_(421214)


def logout_page():
    _l_(421227)

    _c_(421218, _a_(421217, _n_(421216, "loginSection", lambda: loginSection), "empty"));
    _l_(421219)
    with _n_(421220, "logoutSection", lambda: logoutSection):
        _l_(421226)

        _c_(421224, _a_(421222, _n_(421221, "st", lambda: st), "button"), "Log out", key="logout", on_click=_n_(421223, "loggedOut_clicked", lambda: loggedOut_clicked))
        _l_(421225)


def loggedIn_clicked(userName, password):
    _l_(421243)

    if _c_(421231, _n_(421228, "login", lambda: login), _n_(421229, "userName", lambda: userName), _n_(421230, "password", lambda: password)):
        _l_(421242)

        _a_(421233, _n_(421232, "st", lambda: st), "session_state")['loggedIn'] = True
        _l_(421234)
    else:
        _a_(421236, _n_(421235, "st", lambda: st), "session_state")['loggedIn'] = False
        _l_(421237)
        _c_(421240, _a_(421239, _n_(421238, "st", lambda: st), "error"), "Invalid user name or password")
        _l_(421241)


def login_page():
    _l_(421264)

    with _n_(421244, "loginSection", lambda: loginSection):
        _l_(421263)

        if _a_(421246, _n_(421245, "st", lambda: st), "session_state")['loggedIn'] == False:
            _l_(421262)

            userName = _c_(421249, _a_(421248, _n_(421247, "st", lambda: st), "text_input"), placeholder="Enter emailAddress")
            _l_(421250)
            password = _c_(421253, _a_(421252, _n_(421251, "st", lambda: st), "text_input"), placeholder="Enter password", type="password")
            _l_(421254)
            _c_(421260, _a_(421256, _n_(421255, "st", lambda: st), "button"), "Login", on_click=_n_(421257, "loggedIn_clicked", lambda: loggedIn_clicked), args=(_n_(421258, "userName", lambda: userName), _n_(421259, "password", lambda: password)))
            _l_(421261)


with _n_(421265, "headerSection", lambda: headerSection):
    _l_(421288)

    _c_(421268, _a_(421267, _n_(421266, "st", lambda: st), "title"), "Talent Search")
    _l_(421269)
    if 'loggedIn' not in _a_(421271, _n_(421270, "st", lambda: st), "session_state"):
        _l_(421287)

        _a_(421273, _n_(421272, "st", lambda: st), "session_state")['loggedIn'] = False
        _l_(421274)
        _c_(421276, _n_(421275, "login_page", lambda: login_page))
        _l_(421277)
    else:
        if _a_(421279, _n_(421278, "st", lambda: st), "session_state")['loggedIn']:
            _l_(421286)

            _c_(421281, _n_(421280, "logout_page", lambda: logout_page))
            _l_(421282)
            _c_(421284, _n_(421283, "main_page", lambda: main_page))
            _l_(421285)