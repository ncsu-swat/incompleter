# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38032782/why-is-my-logstash-handler-throwing-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(667781)

except ImportError:
    pass
try:
    import logstash
    _l_(667783)

except ImportError:
    pass
try:
    from socket import gethostname
    _l_(667785)

except ImportError:
    pass

class CustomLogger(_a_(667787, _n_(667786, "logging", lambda: logging), "Logger")):
    _l_(667805)

    def _log(self, level, msg, args, exc_info=None, extra=None):
        _l_(667804)

        if _n_(667788, "extra", lambda: extra) is None:
            _l_(667792)

            extra = { 'hostname' : _c_(667790, _n_(667789, "gethostname", lambda: gethostname)) }
            _l_(667791)
        _c_(667802, _a_(667796, _n_(667793, "super", lambda: super)(_n_(667794, "CustomLogger", lambda: CustomLogger), _n_(667795, "self", lambda: self)), "_log"), _n_(667797, "level", lambda: level), _n_(667798, "msg", lambda: msg), _n_(667799, "args", lambda: args), _n_(667800, "exc_info", lambda: exc_info), _n_(667801, "extra", lambda: extra))
        _l_(667803)

def setup_custom_logger(host, port):
    _l_(667850)

    # add hostname to the formatter.
    _c_(667809, _a_(667807, _n_(667806, "logging", lambda: logging), "setLoggerClass"), _n_(667808, "CustomLogger", lambda: CustomLogger))
    _l_(667810)

    formatter = _c_(667813, _a_(667812, _n_(667811, "logging", lambda: logging), "Formatter"), fmt='%(hostname)s - %(asctime)s - %(levelname)s - %(module)s - %(message)s')
    _l_(667814)

    logstash_handler = _c_(667819, _a_(667816, _n_(667815, "logstash", lambda: logstash), "LogstashHandler"), _n_(667817, "host", lambda: host), _n_(667818, "port", lambda: port), version=2)
    _l_(667820)
    _c_(667825, _a_(667822, _n_(667821, "logstash_handler", lambda: logstash_handler), "setLevel"), _a_(667824, _n_(667823, "logging", lambda: logging), "DEBUG"))
    _l_(667826)
    _c_(667830, _a_(667828, _n_(667827, "logstash_handler", lambda: logstash_handler), "setFormatter"), _n_(667829, "formatter", lambda: formatter))
    _l_(667831)

    logger = _c_(667835, _a_(667833, _n_(667832, "logging", lambda: logging), "getLogger"), _n_(667834, "__name__", lambda: __name__))
    _l_(667836)
    _c_(667841, _a_(667838, _n_(667837, "logger", lambda: logger), "setLevel"), _a_(667840, _n_(667839, "logging", lambda: logging), "DEBUG"))
    _l_(667842)
    _c_(667846, _a_(667844, _n_(667843, "logger", lambda: logger), "addHandler"), _n_(667845, "logstash_handler", lambda: logstash_handler))
    _l_(667847)
    aux = _n_(667848, "logger", lambda: logger)
    _l_(667849)

    return aux