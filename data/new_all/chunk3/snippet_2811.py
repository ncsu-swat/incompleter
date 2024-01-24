# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62397348/filenotfounderror-on-heroku-after-creating-that-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Logger:
    _l_(556140)

    def __init__(self, name, file_handler, formatter, stream_handler):
        _l_(556139)

        if not _c_(556092, _a_(556091, _a_(556090, _n_(556089, "os", lambda: os), "path"), "exists"), 'Logs'):
            _l_(556097)

            _c_(556095, _a_(556094, _n_(556093, "os", lambda: os), "makedirs"), 'Logs')
            _l_(556096)

        _n_(556098, "self", lambda: self).logger = _c_(556102, _a_(556100, _n_(556099, "logging", lambda: logging), "getLogger"), _n_(556101, "name", lambda: name))
        _l_(556103)
        _c_(556109, _a_(556106, _a_(556105, _n_(556104, "self", lambda: self), "logger"), "setLevel"), _a_(556108, _n_(556107, "logging", lambda: logging), "DEBUG"))
        _l_(556110)

        _c_(556114, _a_(556112, _n_(556111, "file_handler", lambda: file_handler), "setFormatter"), _n_(556113, "formatter", lambda: formatter))
        _l_(556115)
        _c_(556120, _a_(556118, _a_(556117, _n_(556116, "self", lambda: self), "logger"), "addHandler"), _n_(556119, "file_handler", lambda: file_handler))
        _l_(556121)

        if _n_(556122, "stream_handler", lambda: stream_handler):
            _l_(556138)

            stream_handler = _c_(556125, _a_(556124, _n_(556123, "logging", lambda: logging), "StreamHandler"))
            _l_(556126)
            _c_(556130, _a_(556128, _n_(556127, "stream_handler", lambda: stream_handler), "setFormatter"), _n_(556129, "formatter", lambda: formatter))
            _l_(556131)
            _c_(556136, _a_(556134, _a_(556133, _n_(556132, "self", lambda: self), "logger"), "addHandler"), _n_(556135, "stream_handler", lambda: stream_handler))
            _l_(556137)


logger_dev = _c_(556148, _n_(556141, "Logger", lambda: Logger), 'dev',
                    _c_(556144, _a_(556143, _n_(556142, "handlers", lambda: handlers), "TimedRotatingFileHandler"), f'Logs/dev.log', when='midnight', backupCount=2),
                    _c_(556147, _a_(556146, _n_(556145, 'logging', lambda: logging), 'Formatter'), '%(asctime)s : %(levelname)s : %(filename)s : %(funcName)s : %(message)s'),
                    True)
_l_(556149)

logger_usr = _c_(556157, _n_(556150, 'Logger', lambda: Logger), 'usr',
                    _c_(556153, _a_(556152, _n_(556151, 'handlers', lambda: handlers), 'RotatingFileHandler'), f'Logs/usr.log', maxBytes=7 * 1024 * 1024, backupCount=2),
                    _c_(556156, _a_(556155, _n_(556154, 'logging', lambda: logging), 'Formatter'), '%(asctime)s : %(message)s'),
                    False)
_l_(556158)