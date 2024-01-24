# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41529292/tornado-rediret-incur-typeerror-initialize-missing-1-required-positional-argu
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import bcrypt
    _l_(337581)

except ImportError:
    pass
try:
    import concurrent.futures
    _l_(337583)

except ImportError:
    pass
try:
    import os.path
    _l_(337585)

except ImportError:
    pass
try:
    import re
    _l_(337587)

except ImportError:
    pass
try:
    import subprocess
    _l_(337589)

except ImportError:
    pass
try:
    import tornado.escape
    _l_(337591)

except ImportError:
    pass
try:
    from tornado import gen
    _l_(337593)

except ImportError:
    pass
try:
    import tornado.httpserver
    _l_(337595)

except ImportError:
    pass
try:
    import tornado.ioloop
    _l_(337597)

except ImportError:
    pass
try:
    import tornado.options
    _l_(337599)

except ImportError:
    pass
try:
    import tornado.web
    _l_(337601)

except ImportError:
    pass
try:
    import unicodedata
    _l_(337603)

except ImportError:
    pass
try:
    from tornado.options import define, options
    _l_(337605)

except ImportError:
    pass

_c_(337608, _n_(337606, "define", lambda: define), "port",default=8889,help='run on the given port',type=_n_(337607, "int", lambda: int))
_l_(337609)


class HomeHandler(_a_(337611, _a_(337610, tornado, "web"), "RequestHandler")):
    _l_(337683)


    def get(self):
        _l_(337616)

        #login here
        _c_(337614, _a_(337613, _n_(337612, "self", lambda: self), "render"), 'index.html')
        _l_(337615)

    def post(self):
        _l_(337682)

        def readcodebook(codebook):
            _l_(337644)

            with _c_(337619, _n_(337617, "open", lambda: open), _n_(337618, "codebook", lambda: codebook),'r+') as f:
                _l_(337641)

                CodeLines=_c_(337624, _a_(337623, _c_(337622, _a_(337621, _n_(337620, "f", lambda: f), "read")), "split"), '\n')
                _l_(337625)
                combinations={}
                _l_(337626)
                for c in _n_(337627, "CodeLines", lambda: CodeLines):
                    _l_(337640)

                    if _c_(337630, _n_(337628, "len", lambda: len), _n_(337629, "c", lambda: c))>0:
                        _l_(337639)

                        _n_(337631, "combinations", lambda: combinations)[_c_(337634, _a_(337633, _n_(337632, "c", lambda: c), "split"), '\t')[0]]=_c_(337637, _a_(337636, _n_(337635, "c", lambda: c), "split"), '\t')[1]
                        _l_(337638)
            aux = _n_(337642, "combinations", lambda: combinations)
            _l_(337643)
            return aux
        UserFile='/home/john/PyServer/Users/codebook.txt'
        _l_(337645)
        CodeBook=_c_(337648, _n_(337646, "readcodebook", lambda: readcodebook), _n_(337647, "UserFile", lambda: UserFile))
        _l_(337649)

        if _c_(337652, _a_(337651, _n_(337650, "self", lambda: self), "get_argument"), "login") in _c_(337655, _a_(337654, _n_(337653, "CodeBook", lambda: CodeBook), "keys")):
            _l_(337681)

            if _n_(337656, "CodeBook", lambda: CodeBook)[_c_(337659, _a_(337658, _n_(337657, "self", lambda: self), "get_argument"), "login")]==_c_(337662, _a_(337661, _n_(337660, "self", lambda: self), "get_argument"), "password"):
                _l_(337675)

                #correct pwd
                _c_(337668, _a_(337664, _n_(337663, "self", lambda: self), "redirect"), _c_(337667, _a_(337666, _n_(337665, "self", lambda: self), "get_argument"), "next","/display/"))
                _l_(337669)
            else:
                #incorrect pwd
                _c_(337672, _a_(337671, _n_(337670, "self", lambda: self), "render"), "index.html", error='incorrect password!')
                _l_(337673)
                aux = ""
                _l_(337674)
                return aux
        else:
            #user not found
            _c_(337678, _a_(337677, _n_(337676, "self", lambda: self), "render"), "index.html", error="account not found!")
            _l_(337679)
            aux = ""
            _l_(337680)
            return aux


class DisplayHandler(_a_(337685, _a_(337684, tornado, "web"), "RedirectHandler")):
    _l_(337692)

    def get(self):
        _l_(337690)

        _c_(337688, _a_(337687, _n_(337686, "self", lambda: self), "render"), "displaycontent.html")
        _l_(337689)
    pass
    _l_(337691)


class Application(_a_(337694, _a_(337693, tornado, "web"), "Application")):
    _l_(337724)

    def __init__(self):
        _l_(337723)

        handlers = [
            (r"/", _n_(337695, "HomeHandler", lambda: HomeHandler)),
            (r"/display/", _n_(337696, "DisplayHandler", lambda: DisplayHandler)),
        ]
        _l_(337697)
        settings = _c_(337713, _n_(337698, "dict", lambda: dict), template_path=_c_(337705, _a_(337700, _a_(337699, os, "path"), "join"), _c_(337704, _a_(337702, _a_(337701, os, "path"), "dirname"), _n_(337703, "__file__", lambda: __file__)), "templates"),
            static_path=_c_(337712, _a_(337707, _a_(337706, os, "path"), "join"), _c_(337711, _a_(337709, _a_(337708, os, "path"), "dirname"), _n_(337710, "__file__", lambda: __file__)), "static"),
            #ui_modules={"Entry": EntryModule},
            #xsrf_cookies=True,
            #cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            #login_url="/auth/login",
            debug=True,
        )
        _l_(337714)
        _c_(337721, _a_(337717, _a_(337716, _a_(337715, tornado, "web"), "Application"), "__init__"), _n_(337718, "self", lambda: self),_n_(337719, "handlers", lambda: handlers),**_n_(337720, "settings", lambda: settings))
        _l_(337722)

if _n_(337725, "__name__", lambda: __name__)=="__main__":
    _l_(337749)

    _c_(337728, _a_(337727, _a_(337726, tornado, "options"), "parse_command_line"))
    _l_(337729)
    http_server=_c_(337734, _a_(337731, _a_(337730, tornado, "httpserver"), "HTTPServer"), _c_(337733, _n_(337732, "Application", lambda: Application)))
    _l_(337735)
    _c_(337740, _a_(337737, _n_(337736, "http_server", lambda: http_server), "listen"), _a_(337739, _n_(337738, "options", lambda: options), "port"))
    _l_(337741)
    _c_(337747, _a_(337746, _c_(337745, _a_(337744, _a_(337743, _a_(337742, tornado, "ioloop"), "IOLoop"), "instance")), "start"))
    _l_(337748)