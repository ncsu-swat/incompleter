# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69801765/opening-tun-interface-throws-either-io-unsupportedoperation-or-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(629444)

except ImportError:
    pass
try:
    import sys
    _l_(629446)

except ImportError:
    pass
try:
    import struct
    _l_(629448)

except ImportError:
    pass
try:
    import logging
    _l_(629450)

except ImportError:
    pass
try:
    import threading
    _l_(629452)

except ImportError:
    pass
try:
    import traceback
    _l_(629454)

except ImportError:
    pass
try:
    import subprocess
    _l_(629456)

except ImportError:
    pass

if _a_(629458, _n_(629457, "sys", lambda: sys), "platform") == "linux" or _a_(629460, _n_(629459, "sys", lambda: sys), "platform") == "linux2":
    _l_(629463)

    try:
        import fcntl
        _l_(629462)

    except ImportError:
        pass
try:
    from select import select
    _l_(629465)

except ImportError:
    pass
try:
    import spinel.util as util
    _l_(629467)

except ImportError:
    pass
try:
    import spinel.config as CONFIG
    _l_(629469)

except ImportError:
    pass

IFF_TUN = 0x0001
_l_(629470)
IFF_TAP = 0x0002
_l_(629471)
IFF_NO_PI = 0x1000
_l_(629472)
IFF_TUNSETIFF = 0x400454ca
_l_(629473)
IFF_TUNSETOWNER = _n_(629474, "IFF_TUNSETIFF", lambda: IFF_TUNSETIFF) + 2
_l_(629475)


class TunInterface(_n_(629476, "object", lambda: object)):
    _l_(629706)

    """ Utility class for creating a TUN network interface. """

    def __init__(self, identifier):
        _l_(629520)

        _n_(629477, "self", lambda: self).identifier = _n_(629478, "identifier", lambda: identifier)
        _l_(629479)
        _n_(629480, "self", lambda: self).ifname = "tun" + _c_(629484, _n_(629481, "str", lambda: str), _a_(629483, _n_(629482, "self", lambda: self), "identifier"))
        _l_(629485)
        _n_(629486, "self", lambda: self).tun = None
        _l_(629487)
        _n_(629488, "self", lambda: self).fd = None
        _l_(629489)

        platform = _a_(629491, _n_(629490, "sys", lambda: sys), "platform")
        _l_(629492)
        if _n_(629493, "platform", lambda: platform) == "linux" or _n_(629494, "platform", lambda: platform) == "linux2":
            _l_(629511)

            _c_(629497, _a_(629496, _n_(629495, "self", lambda: self), "__init_linux"))
            _l_(629498)
        elif _n_(629499, "platform", lambda: platform) == "darwin":
            _l_(629510)

            _c_(629502, _a_(629501, _n_(629500, "self", lambda: self), "__init_osx"))
            _l_(629503)
        else:
            raise _c_(629508, _n_(629504, "RuntimeError", lambda: RuntimeError), _c_(629507, _a_(629505, "Platform \"{}\" is not supported.", "format"), _n_(629506, "platform", lambda: platform)))
            _l_(629509)

        _c_(629514, _a_(629513, _n_(629512, "self", lambda: self), "ifconfig"), "up")
        _l_(629515)
        #self.ifconfig("inet6 add fd00::1/64")
        _c_(629518, _a_(629517, _n_(629516, "self", lambda: self), "__start_tun_thread"))
        _l_(629519)

    def __init_osx(self):
        _l_(629551)

        _c_(629526, _a_(629523, _a_(629522, _n_(629521, "CONFIG", lambda: CONFIG), "LOGGER"), "info"), "TUN: Starting osx " + _a_(629525, _n_(629524, "self", lambda: self), "ifname"))
        _l_(629527)
        filename = "/dev/" + _a_(629529, _n_(629528, "self", lambda: self), "ifname")
        _l_(629530)
        _n_(629531, "self", lambda: self).tun = _c_(629537, _a_(629533, _n_(629532, "os", lambda: os), "open"), _n_(629534, "filename", lambda: filename), _a_(629536, _n_(629535, "os", lambda: os), "O_RDWR"))
        _l_(629538)
        _n_(629539, "self", lambda: self).fd = _a_(629541, _n_(629540, "self", lambda: self), "tun")
        _l_(629542)
        # trick osx to auto-assign a link local address
        _c_(629545, _a_(629544, _n_(629543, "self", lambda: self), "addr_add"), "fe80::1")
        _l_(629546)
        _c_(629549, _a_(629548, _n_(629547, "self", lambda: self), "addr_del"), "fe80::1")
        _l_(629550)



    def __init_linux(self):
        _l_(629592)

        _c_(629557, _a_(629554, _a_(629553, _n_(629552, "CONFIG", lambda: CONFIG), "LOGGER"), "info"), "TUN: Starting linux " + _a_(629556, _n_(629555, "self", lambda: self), "ifname"))
        _l_(629558)
        _n_(629559, "self", lambda: self).tun = _c_(629561, _n_(629560, "open", lambda: open), "/dev/net/tun", "r+b")
        _l_(629562)
        _n_(629563, "self", lambda: self).fd = _c_(629567, _a_(629566, _a_(629565, _n_(629564, "self", lambda: self), "tun"), "fileno"))
        _l_(629568)

        ifr = _c_(629575, _a_(629570, _n_(629569, "struct", lambda: struct), "pack"), "16sH", _a_(629572, _n_(629571, "self", lambda: self), "ifname"), _n_(629573, "IFF_TUN", lambda: IFF_TUN) | _n_(629574, "IFF_NO_PI", lambda: IFF_NO_PI))
        _l_(629576)
        _c_(629583, _a_(629578, _n_(629577, "fcntl", lambda: fcntl), "ioctl"), _a_(629580, _n_(629579, "self", lambda: self), "tun"), _n_(629581, "IFF_TUNSETIFF", lambda: IFF_TUNSETIFF), _n_(629582, "ifr", lambda: ifr))  # Name interface tun#
        _l_(629584)  # Name interface tun#
        _c_(629590, _a_(629586, _n_(629585, "fcntl", lambda: fcntl), "ioctl"), _a_(629588, _n_(629587, "self", lambda: self), "tun"), _n_(629589, "IFF_TUNSETOWNER", lambda: IFF_TUNSETOWNER), 1000)  # Allow non-sudo access
        _l_(629591)  # Allow non-sudo access


    def close(self):
        _l_(629606)

        """ Close this tunnel interface. """
        if _a_(629594, _n_(629593, "self", lambda: self), "tun"):
            _l_(629605)

            _c_(629599, _a_(629596, _n_(629595, "os", lambda: os), "close"), _a_(629598, _n_(629597, "self", lambda: self), "fd"))
            _l_(629600)
            _n_(629601, "self", lambda: self).fd = None
            _l_(629602)
            _n_(629603, "self", lambda: self).tun = None
            _l_(629604)

    @_n_(629607, "classmethod", lambda: classmethod)
    def command(cls, cmd):
        _l_(629613)

        """ Utility to make a system call. """
        _c_(629611, _a_(629609, _n_(629608, "subprocess", lambda: subprocess), "check_call"), _n_(629610, "cmd", lambda: cmd), shell=True)
        _l_(629612)

    def ifconfig(self, args):
        _l_(629621)

        """ Bring interface up and/or assign addresses. """
        _c_(629619, _a_(629615, _n_(629614, "self", lambda: self), "command"), 'ifconfig ' + _a_(629617, _n_(629616, "self", lambda: self), "ifname") + ' ' + _n_(629618, "args", lambda: args))
        _l_(629620)


    def __run_tun_thread(self):
        _l_(629685)

        while _a_(629623, _n_(629622, "self", lambda: self), "fd"):
            _l_(629668)

            try:
                _l_(629667)

                ready_fd = _c_(629627, _n_(629624, "select", lambda: select), [_a_(629626, _n_(629625, "self", lambda: self), "fd")], [], [])[0][0]
                _l_(629628)
                if _n_(629629, "ready_fd", lambda: ready_fd) == _a_(629631, _n_(629630, "self", lambda: self), "fd"):
                    _l_(629660)

                    packet = _c_(629636, _a_(629633, _n_(629632, "os", lambda: os), "read"), _a_(629635, _n_(629634, "self", lambda: self), "fd"), 4000)
                    _l_(629637)
                    if _a_(629639, _n_(629638, "CONFIG", lambda: CONFIG), "DEBUG_TUN"):
                        _l_(629654)

                        _c_(629652, _a_(629642, _a_(629641, _n_(629640, "CONFIG", lambda: CONFIG), "LOGGER"), "debug"), "\nTUN: RX (" + _c_(629647, _n_(629643, "str", lambda: str), _c_(629646, _n_(629644, "len", lambda: len), _n_(629645, "packet", lambda: packet))) +
                                            ") " + _c_(629651, _a_(629649, _n_(629648, "util", lambda: util), "hexify_str"), _n_(629650, "packet", lambda: packet)))
                        _l_(629653)
                    _c_(629658, _a_(629656, _n_(629655, "self", lambda: self), "write"), _n_(629657, "packet", lambda: packet))
                    _l_(629659)
            except:
                _l_(629666)

                _c_(629663, _a_(629662, _n_(629661, "traceback", lambda: traceback), "print_exc"))
                _l_(629664)
                break
                _l_(629665)

        _c_(629672, _a_(629671, _a_(629670, _n_(629669, "CONFIG", lambda: CONFIG), "LOGGER"), "info"), "TUN: exiting")
        _l_(629673)
        if _a_(629675, _n_(629674, "self", lambda: self), "fd"):
            _l_(629684)

            _c_(629680, _a_(629677, _n_(629676, "os", lambda: os), "close"), _a_(629679, _n_(629678, "self", lambda: self), "fd"))
            _l_(629681)
            _n_(629682, "self", lambda: self).fd = None
            _l_(629683)

    def __start_tun_thread(self):
        _l_(629705)

        """Start reader thread"""
        _n_(629686, "self", lambda: self)._reader_alive = True
        _l_(629687)
        _n_(629688, "self", lambda: self).receiver_thread = _c_(629693, _a_(629690, _n_(629689, "threading", lambda: threading), "Thread"), target=_a_(629692, _n_(629691, "self", lambda: self), "__run_tun_thread"))
        _l_(629694)
        _c_(629698, _a_(629697, _a_(629696, _n_(629695, "self", lambda: self), "receiver_thread"), "setDaemon"), True)
        _l_(629699)
        _c_(629703, _a_(629702, _a_(629701, _n_(629700, "self", lambda: self), "receiver_thread"), "start"))
        _l_(629704)