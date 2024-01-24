# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38032782/why-is-my-logstash-handler-throwing-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import logging
    _l_(668411)

except ImportError:
    pass
try:
    import logstash
    _l_(668413)

except ImportError:
    pass
try:
    from socket import gethostname
    _l_(668415)

except ImportError:
    pass

class CustomLogger(_a_(668417, _n_(668416, "logging", lambda: logging), "Logger")):
    _l_(668435)

    def _log(self, level, msg, args, exc_info=None, extra=None):
        _l_(668434)

        if _n_(668418, "extra", lambda: extra) is None:
            _l_(668422)

            extra = { 'hostname' : _c_(668420, _n_(668419, "gethostname", lambda: gethostname)) }
            _l_(668421)
        _c_(668432, _a_(668426, _n_(668423, "super", lambda: super)(_n_(668424, "CustomLogger", lambda: CustomLogger), _n_(668425, "self", lambda: self)), "_log"), _n_(668427, "level", lambda: level), _n_(668428, "msg", lambda: msg), _n_(668429, "args", lambda: args), _n_(668430, "exc_info", lambda: exc_info), _n_(668431, "extra", lambda: extra))
        _l_(668433)

def setup_custom_logger(host, port):
    _l_(668480)

    # add hostname to the formatter.
    _c_(668439, _a_(668437, _n_(668436, "logging", lambda: logging), "setLoggerClass"), _n_(668438, "CustomLogger", lambda: CustomLogger))
    _l_(668440)

    formatter = _c_(668443, _a_(668442, _n_(668441, "logging", lambda: logging), "Formatter"), fmt='%(hostname)s - %(asctime)s - %(levelname)s - %(module)s - %(message)s')
    _l_(668444)

    logstash_handler = _c_(668449, _a_(668446, _n_(668445, "logstash", lambda: logstash), "LogstashHandler"), _n_(668447, "host", lambda: host), _n_(668448, "port", lambda: port), version=2)
    _l_(668450)
    _c_(668455, _a_(668452, _n_(668451, "logstash_handler", lambda: logstash_handler), "setLevel"), _a_(668454, _n_(668453, "logging", lambda: logging), "DEBUG"))
    _l_(668456)
    _c_(668460, _a_(668458, _n_(668457, "logstash_handler", lambda: logstash_handler), "setFormatter"), _n_(668459, "formatter", lambda: formatter))
    _l_(668461)

    logger = _c_(668465, _a_(668463, _n_(668462, "logging", lambda: logging), "getLogger"), _n_(668464, "__name__", lambda: __name__))
    _l_(668466)
    _c_(668471, _a_(668468, _n_(668467, "logger", lambda: logger), "setLevel"), _a_(668470, _n_(668469, "logging", lambda: logging), "DEBUG"))
    _l_(668472)
    _c_(668476, _a_(668474, _n_(668473, "logger", lambda: logger), "addHandler"), _n_(668475, "logstash_handler", lambda: logstash_handler))
    _l_(668477)
    aux = _n_(668478, "logger", lambda: logger)
    _l_(668479)

    return aux