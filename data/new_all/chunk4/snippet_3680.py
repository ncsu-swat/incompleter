# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69801765/opening-tun-interface-throws-either-io-unsupportedoperation-or-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(641013)

except ImportError:
    pass
try:
    import sys
    _l_(641015)

except ImportError:
    pass
try:
    import struct
    _l_(641017)

except ImportError:
    pass
try:
    import logging
    _l_(641019)

except ImportError:
    pass
try:
    import threading
    _l_(641021)

except ImportError:
    pass
try:
    import traceback
    _l_(641023)

except ImportError:
    pass
try:
    import subprocess
    _l_(641025)

except ImportError:
    pass

if _a_(641027, _n_(641026, "sys", lambda: sys), "platform") == "linux" or _a_(641029, _n_(641028, "sys", lambda: sys), "platform") == "linux2":
    _l_(641032)

    try:
        import fcntl
        _l_(641031)

    except ImportError:
        pass
try:
    from select import select
    _l_(641034)

except ImportError:
    pass
try:
    import spinel.util as util
    _l_(641036)

except ImportError:
    pass
try:
    import spinel.config as CONFIG
    _l_(641038)

except ImportError:
    pass

IFF_TUN = 0x0001
_l_(641039)
IFF_TAP = 0x0002
_l_(641040)
IFF_NO_PI = 0x1000
_l_(641041)
IFF_TUNSETIFF = 0x400454ca
_l_(641042)
IFF_TUNSETOWNER = _n_(641043, "IFF_TUNSETIFF", lambda: IFF_TUNSETIFF) + 2
_l_(641044)


class TunInterface(_n_(641045, "object", lambda: object)):
    _l_(641275)

    """ Utility class for creating a TUN network interface. """

    def __init__(self, identifier):
        _l_(641089)

        _n_(641046, "self", lambda: self).identifier = _n_(641047, "identifier", lambda: identifier)
        _l_(641048)
        _n_(641049, "self", lambda: self).ifname = "tun" + _c_(641053, _n_(641050, "str", lambda: str), _a_(641052, _n_(641051, "self", lambda: self), "identifier"))
        _l_(641054)
        _n_(641055, "self", lambda: self).tun = None
        _l_(641056)
        _n_(641057, "self", lambda: self).fd = None
        _l_(641058)

        platform = _a_(641060, _n_(641059, "sys", lambda: sys), "platform")
        _l_(641061)
        if _n_(641062, "platform", lambda: platform) == "linux" or _n_(641063, "platform", lambda: platform) == "linux2":
            _l_(641080)

            _c_(641066, _a_(641065, _n_(641064, "self", lambda: self), "__init_linux"))
            _l_(641067)
        elif _n_(641068, "platform", lambda: platform) == "darwin":
            _l_(641079)

            _c_(641071, _a_(641070, _n_(641069, "self", lambda: self), "__init_osx"))
            _l_(641072)
        else:
            raise _c_(641077, _n_(641073, "RuntimeError", lambda: RuntimeError), _c_(641076, _a_(641074, "Platform \"{}\" is not supported.", "format"), _n_(641075, "platform", lambda: platform)))
            _l_(641078)

        _c_(641083, _a_(641082, _n_(641081, "self", lambda: self), "ifconfig"), "up")
        _l_(641084)
        #self.ifconfig("inet6 add fd00::1/64")
        _c_(641087, _a_(641086, _n_(641085, "self", lambda: self), "__start_tun_thread"))
        _l_(641088)

    def __init_osx(self):
        _l_(641120)

        _c_(641095, _a_(641092, _a_(641091, _n_(641090, "CONFIG", lambda: CONFIG), "LOGGER"), "info"), "TUN: Starting osx " + _a_(641094, _n_(641093, "self", lambda: self), "ifname"))
        _l_(641096)
        filename = "/dev/" + _a_(641098, _n_(641097, "self", lambda: self), "ifname")
        _l_(641099)
        _n_(641100, "self", lambda: self).tun = _c_(641106, _a_(641102, _n_(641101, "os", lambda: os), "open"), _n_(641103, "filename", lambda: filename), _a_(641105, _n_(641104, "os", lambda: os), "O_RDWR"))
        _l_(641107)
        _n_(641108, "self", lambda: self).fd = _a_(641110, _n_(641109, "self", lambda: self), "tun")
        _l_(641111)
        # trick osx to auto-assign a link local address
        _c_(641114, _a_(641113, _n_(641112, "self", lambda: self), "addr_add"), "fe80::1")
        _l_(641115)
        _c_(641118, _a_(641117, _n_(641116, "self", lambda: self), "addr_del"), "fe80::1")
        _l_(641119)



    def __init_linux(self):
        _l_(641161)

        _c_(641126, _a_(641123, _a_(641122, _n_(641121, "CONFIG", lambda: CONFIG), "LOGGER"), "info"), "TUN: Starting linux " + _a_(641125, _n_(641124, "self", lambda: self), "ifname"))
        _l_(641127)
        _n_(641128, "self", lambda: self).tun = _c_(641130, _n_(641129, "open", lambda: open), "/dev/net/tun", "r+b")
        _l_(641131)
        _n_(641132, "self", lambda: self).fd = _c_(641136, _a_(641135, _a_(641134, _n_(641133, "self", lambda: self), "tun"), "fileno"))
        _l_(641137)

        ifr = _c_(641144, _a_(641139, _n_(641138, "struct", lambda: struct), "pack"), "16sH", _a_(641141, _n_(641140, "self", lambda: self), "ifname"), _n_(641142, "IFF_TUN", lambda: IFF_TUN) | _n_(641143, "IFF_NO_PI", lambda: IFF_NO_PI))
        _l_(641145)
        _c_(641152, _a_(641147, _n_(641146, "fcntl", lambda: fcntl), "ioctl"), _a_(641149, _n_(641148, "self", lambda: self), "tun"), _n_(641150, "IFF_TUNSETIFF", lambda: IFF_TUNSETIFF), _n_(641151, "ifr", lambda: ifr))  # Name interface tun#
        _l_(641153)  # Name interface tun#
        _c_(641159, _a_(641155, _n_(641154, "fcntl", lambda: fcntl), "ioctl"), _a_(641157, _n_(641156, "self", lambda: self), "tun"), _n_(641158, "IFF_TUNSETOWNER", lambda: IFF_TUNSETOWNER), 1000)  # Allow non-sudo access
        _l_(641160)  # Allow non-sudo access


    def close(self):
        _l_(641175)

        """ Close this tunnel interface. """
        if _a_(641163, _n_(641162, "self", lambda: self), "tun"):
            _l_(641174)

            _c_(641168, _a_(641165, _n_(641164, "os", lambda: os), "close"), _a_(641167, _n_(641166, "self", lambda: self), "fd"))
            _l_(641169)
            _n_(641170, "self", lambda: self).fd = None
            _l_(641171)
            _n_(641172, "self", lambda: self).tun = None
            _l_(641173)

    @_n_(641176, "classmethod", lambda: classmethod)
    def command(cls, cmd):
        _l_(641182)

        """ Utility to make a system call. """
        _c_(641180, _a_(641178, _n_(641177, "subprocess", lambda: subprocess), "check_call"), _n_(641179, "cmd", lambda: cmd), shell=True)
        _l_(641181)

    def ifconfig(self, args):
        _l_(641190)

        """ Bring interface up and/or assign addresses. """
        _c_(641188, _a_(641184, _n_(641183, "self", lambda: self), "command"), 'ifconfig ' + _a_(641186, _n_(641185, "self", lambda: self), "ifname") + ' ' + _n_(641187, "args", lambda: args))
        _l_(641189)


    def __run_tun_thread(self):
        _l_(641254)

        while _a_(641192, _n_(641191, "self", lambda: self), "fd"):
            _l_(641237)

            try:
                _l_(641236)

                ready_fd = _c_(641196, _n_(641193, "select", lambda: select), [_a_(641195, _n_(641194, "self", lambda: self), "fd")], [], [])[0][0]
                _l_(641197)
                if _n_(641198, "ready_fd", lambda: ready_fd) == _a_(641200, _n_(641199, "self", lambda: self), "fd"):
                    _l_(641229)

                    packet = _c_(641205, _a_(641202, _n_(641201, "os", lambda: os), "read"), _a_(641204, _n_(641203, "self", lambda: self), "fd"), 4000)
                    _l_(641206)
                    if _a_(641208, _n_(641207, "CONFIG", lambda: CONFIG), "DEBUG_TUN"):
                        _l_(641223)

                        _c_(641221, _a_(641211, _a_(641210, _n_(641209, "CONFIG", lambda: CONFIG), "LOGGER"), "debug"), "\nTUN: RX (" + _c_(641216, _n_(641212, "str", lambda: str), _c_(641215, _n_(641213, "len", lambda: len), _n_(641214, "packet", lambda: packet))) +
                                            ") " + _c_(641220, _a_(641218, _n_(641217, "util", lambda: util), "hexify_str"), _n_(641219, "packet", lambda: packet)))
                        _l_(641222)
                    _c_(641227, _a_(641225, _n_(641224, "self", lambda: self), "write"), _n_(641226, "packet", lambda: packet))
                    _l_(641228)
            except:
                _l_(641235)

                _c_(641232, _a_(641231, _n_(641230, "traceback", lambda: traceback), "print_exc"))
                _l_(641233)
                break
                _l_(641234)

        _c_(641241, _a_(641240, _a_(641239, _n_(641238, "CONFIG", lambda: CONFIG), "LOGGER"), "info"), "TUN: exiting")
        _l_(641242)
        if _a_(641244, _n_(641243, "self", lambda: self), "fd"):
            _l_(641253)

            _c_(641249, _a_(641246, _n_(641245, "os", lambda: os), "close"), _a_(641248, _n_(641247, "self", lambda: self), "fd"))
            _l_(641250)
            _n_(641251, "self", lambda: self).fd = None
            _l_(641252)

    def __start_tun_thread(self):
        _l_(641274)

        """Start reader thread"""
        _n_(641255, "self", lambda: self)._reader_alive = True
        _l_(641256)
        _n_(641257, "self", lambda: self).receiver_thread = _c_(641262, _a_(641259, _n_(641258, "threading", lambda: threading), "Thread"), target=_a_(641261, _n_(641260, "self", lambda: self), "__run_tun_thread"))
        _l_(641263)
        _c_(641267, _a_(641266, _a_(641265, _n_(641264, "self", lambda: self), "receiver_thread"), "setDaemon"), True)
        _l_(641268)
        _c_(641272, _a_(641271, _a_(641270, _n_(641269, "self", lambda: self), "receiver_thread"), "start"))
        _l_(641273)