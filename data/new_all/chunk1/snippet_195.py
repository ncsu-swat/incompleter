# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/25054729/delattr-on-class-instance-produces-unexpected-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class __Sysconfig(_n_(379562, "Config", lambda: Config)):
    _l_(379580)

    """
    H.O.M.I.E.'s system configuration
    """
    ### Application information ###
    APP_NAME = 'H.O.M.I.E.'
    _l_(379563)
    APP_VER = '0.1-indev'
    _l_(379564)
    APP_FULL_NAME = "Cool system"
    _l_(379565)

    ### System logging ###
    LOG_DIR = '/var/log/homie.d'
    _l_(379566)
    LOGFILE = '/var/log/homie'
    _l_(379567)
    LOGLVL = 2
    _l_(379568)

    ### System files ###
    DAEMON_SERVICES_FILE = '/var/run/homie.services'
    _l_(379569)
    DAEMON_SOCK = 'tcp://127.0.0.1'
    _l_(379570)
    GLOBAL_CONFIG_DIR = '/usr/local/etc/homie.d'
    _l_(379571)

    ### System EMail ###
    EMAIL_FROM = 'homie@company.com'
    _l_(379572)
    TECH_EMAIL = 'me@company.com'
    _l_(379573)
    ADMIN_EMAILS = ['me@company.com', 'other@company.com']
    _l_(379574)

    def __init__(self):
        _l_(379579)

        """
        Creates a sysconfig instance
        """
        _c_(379577, _a_(379576, _n_(379575, "super", lambda: super)(), "__init__"), '/usr/local/etc/homie')
        _l_(379578)