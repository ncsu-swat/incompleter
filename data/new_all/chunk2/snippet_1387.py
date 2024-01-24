# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66137185/python-3-attributeerror-module-sys-has-no-attribute-argv
#! python3
# pw.py password locker program

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
PASSWORDS = {'email': 'F7min18DDuvMJuxESSLHFhTxFtjvB6',
             'blog': 'VmALQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}
_l_(453638)
try:
    import sys, pyperclip
    _l_(453640)

except ImportError:
    pass
if _c_(453644, _n_(453641, "len", lambda: len), _a_(453643, _n_(453642, "sys", lambda: sys), "agrv")) < 2:
    _l_(453652)

    _c_(453646, _n_(453645, "print", lambda: print), 'Usage: python3 pw.py [account] - copy account password')
    _l_(453647)
    _c_(453650, _a_(453649, _n_(453648, "sys", lambda: sys), "exit"))
    _l_(453651)

account = _a_(453654, _n_(453653, "sys", lambda: sys), "argv")[1]
_l_(453655)

if _n_(453656, "account", lambda: account) in _n_(453657, "PASSWORDS", lambda: PASSWORDS):
    _l_(453672)

    _c_(453662, _a_(453659, _n_(453658, "pyperclip", lambda: pyperclip), "copy"), _n_(453660, "PASSWORDS", lambda: PASSWORDS)[_n_(453661, "account", lambda: account)])
    _l_(453663)
    _c_(453666, _n_(453664, "print", lambda: print), 'Password for ' + _n_(453665, "account", lambda: account) + 'copied to clipboard.')
    _l_(453667)
else:
    _c_(453670, _n_(453668, "print", lambda: print), 'There is no account named ' + _n_(453669, "account", lambda: account))
    _l_(453671)