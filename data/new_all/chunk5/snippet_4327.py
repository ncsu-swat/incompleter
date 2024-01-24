# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59614941/python-facebookchat-attributeerror-str-object-has-no-attribute-to-send-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import fbchat
    _l_(651951)

except ImportError:
    pass
try:
    from getpass import getpass
    _l_(651953)

except ImportError:
    pass
username = _c_(651957, _n_(651954, "str", lambda: str), _c_(651956, _n_(651955, "input", lambda: input), "Username: "))
_l_(651958)
client = _c_(651964, _a_(651960, _n_(651959, "fbchat", lambda: fbchat), "Client"), _n_(651961, "username", lambda: username), _c_(651963, _n_(651962, "getpass", lambda: getpass)))
_l_(651965)
no_of_friends = _c_(651969, _n_(651966, "int", lambda: int), _c_(651968, _n_(651967, "input", lambda: input), "Number of friends: "))
_l_(651970)
for i in _c_(651973, _n_(651971, "range", lambda: range), _n_(651972, "no_of_friends", lambda: no_of_friends)):
    _l_(652003)

    name = _c_(651977, _n_(651974, "str", lambda: str), _c_(651976, _n_(651975, "input", lambda: input), "Name: "))
    _l_(651978)
    friends = _c_(651982, _a_(651980, _n_(651979, "client", lambda: client), "searchForUsers"), _n_(651981, "name", lambda: name))  # return a list of names
    _l_(651983)  # return a list of names
    friend = _n_(651984, "friends", lambda: friends)[0]
    _l_(651985)
    msg = _c_(651989, _n_(651986, "str", lambda: str), _c_(651988, _n_(651987, "input", lambda: input), "Message: "))
    _l_(651990)
    sent = _c_(651996, _a_(651992, _n_(651991, "client", lambda: client), "send"), _a_(651994, _n_(651993, "friend", lambda: friend), "uid"), _n_(651995, "msg", lambda: msg))
    _l_(651997)
    if _n_(651998, "sent", lambda: sent):
        _l_(652002)

        _c_(652000, _n_(651999, "print", lambda: print), "Message sent successfully!")
        _l_(652001)