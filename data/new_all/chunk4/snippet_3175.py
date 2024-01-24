# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/27559733/python-3-2-typeerror-argument-must-be-an-int-or-have-a-fileno-method
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(599408, _n_(599407, "open", lambda: open), 'addons.txt', 'r') as addonsFile:
    _l_(599421)

    for line in _n_(599409, "addonsFile", lambda: addonsFile):
        _l_(599420)

        addon = _c_(599412, _a_(599411, _n_(599410, "line", lambda: line), "rstrip"))
        _l_(599413)
        fileUrl = 'http://www.google.com/%s/ncr' % _n_(599414, "addon", lambda: addon)
        _l_(599415)
        response = _c_(599418, _n_(599416, "urlopen", lambda: urlopen), _n_(599417, "fileUrl", lambda: fileUrl))
        _l_(599419)