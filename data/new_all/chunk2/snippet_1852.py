# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50647042/typeerror-object-supporting-the-buffer-api-required-in-flask-api
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class UserLogin(_n_(422586, "Resource", lambda: Resource)):
    _l_(422637)

    def post(self):
        _l_(422636)


        # Parse the arguments

        parser = _c_(422589, _a_(422588, _n_(422587, "reqparse", lambda: reqparse), "RequestParser"))
        _l_(422590)
        _c_(422593, _a_(422592, _n_(422591, "parser", lambda: parser), "add_argument"), 'username')
        _l_(422594)
        _c_(422597, _a_(422596, _n_(422595, "parser", lambda: parser), "add_argument"), 'password')
        _l_(422598)
        args = _c_(422601, _a_(422600, _n_(422599, "parser", lambda: parser), "parse_args"))
        _l_(422602)

        _user = _n_(422603, "args", lambda: args)['username']
        _l_(422604)
        _userPassword = _n_(422605, "args", lambda: args)['password']
        _l_(422606)
        _h = _c_(422612, _a_(422608, _n_(422607, "hashlib", lambda: hashlib), "md5"), _c_(422611, _a_(422610, _n_(422609, "_userPassword", lambda: _userPassword), "encode")))
        _l_(422613)
        conn = _c_(422616, _a_(422615, _n_(422614, "mysql", lambda: mysql), "connect"))
        _l_(422617)
        cursor = _c_(422620, _a_(422619, _n_(422618, "conn", lambda: conn), "cursor"))
        _l_(422621)
        _c_(422626, _a_(422623, _n_(422622, "cursor", lambda: cursor), "execute"), '''select * from user where username = %s && password = %s''', (_n_(422624, "_user", lambda: _user), _n_(422625, "_h", lambda: _h)))
        _l_(422627)
        data = _c_(422630, _a_(422629, _n_(422628, "cursor", lambda: cursor), "fetchall"))
        _l_(422631)
        aux = _c_(422634, _n_(422632, "jsonify", lambda: jsonify), _n_(422633, "data", lambda: data))
        _l_(422635)

        return aux