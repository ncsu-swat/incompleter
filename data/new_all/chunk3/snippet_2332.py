# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50263360/observing-typeerror-while-trying-to-spawn-to-device
#!/usr/local/lib python3.6
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pexpect
    _l_(525577)

except ImportError:
    pass
try:
    import sys
    _l_(525579)

except ImportError:
    pass
try:
    import re
    _l_(525581)

except ImportError:
    pass

def dologin(child):
    _l_(525599)

    # Enter User Name
    _c_(525584, _a_(525583, _n_(525582, "child", lambda: child), "expect"), 'login:')
    _l_(525585)
    _c_(525588, _a_(525587, _n_(525586, "child", lambda: child), "sendline"), 'admin')
    _l_(525589)

    # Enter Password
    _c_(525592, _a_(525591, _n_(525590, "child", lambda: child), "expect"), 'Password:')
    _l_(525593)
    _c_(525596, _a_(525595, _n_(525594, "child", lambda: child), "sendline"), '123')
    _l_(525597)
    aux = ""
    _l_(525598)
    return aux

def doprepcommands(child):
    _l_(525641)

    # Enter config prompt
    _c_(525602, _a_(525601, _n_(525600, "child", lambda: child), "expect"), 'NOS/27179080475072>')
    _l_(525603)
    _c_(525606, _a_(525605, _n_(525604, "child", lambda: child), "sendline"), 'config')
    _l_(525607)

    # Issue command
    _c_(525610, _a_(525609, _n_(525608, "child", lambda: child), "expect"), 'NOS/27179080475072/DEBUG/Config>')
    _l_(525611)
    _c_(525614, _a_(525613, _n_(525612, "child", lambda: child), "sendline"), 'show vlan')
    _l_(525615)
    _c_(525618, _a_(525617, _n_(525616, "child", lambda: child), "expect"), 'NOS/27179080475072/DEBUG/Config>')
    _l_(525619)
    _c_(525622, _a_(525621, _n_(525620, "child", lambda: child), "sendline"), 'exit')
    _l_(525623)
    _c_(525626, _a_(525625, _n_(525624, "child", lambda: child), "expect"), 'NOS/27179080475072/DEBUG>')
    _l_(525627)
    _c_(525630, _a_(525629, _n_(525628, "child", lambda: child), "sendline"), 'exit')
    _l_(525631)
    _c_(525634, _a_(525633, _n_(525632, "child", lambda: child), "expect"), 'NOS/27179080475072')
    _l_(525635)
    _c_(525638, _a_(525637, _n_(525636, "child", lambda: child), "sendline"), 'exit')
    _l_(525639)
    aux = ""
    _l_(525640)
    return aux

# Spawn the telnet session
child = _c_(525644, _a_(525643, _n_(525642, "pexpect", lambda: pexpect), "spawn"), 'telnet 192.168.1.254')
_l_(525645)

 # Display progress on screen
_n_(525646, "child", lambda: child).logfile = _a_(525648, _n_(525647, "sys", lambda: sys), "stdout")
_l_(525649)
_c_(525652, _n_(525650, "dologin", lambda: dologin), _n_(525651, "child", lambda: child))
_l_(525653)
_c_(525656, _n_(525654, "doprepcommands", lambda: doprepcommands), _n_(525655, "child", lambda: child))
_l_(525657)