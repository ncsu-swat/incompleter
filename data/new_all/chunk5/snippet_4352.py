# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59296980/attributeerror-blueprint-object-has-no-attribute-teardown-appcontext-in-goo
#!/home/kimdev/Documents/pythonwebapp/flask_v1/bin/python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(649985)

except ImportError:
    pass
try:
    import yaml
    _l_(649987)

except ImportError:
    pass
try:
    import datetime
    _l_(649989)

except ImportError:
    pass
try:
    from flask         import Flask, session, make_response, request, url_for, redirect
    _l_(649991)

except ImportError:
    pass
try:
    from flask_mysqldb import MySQL
    _l_(649993)

except ImportError:
    pass
try:
    from functools     import wraps
    _l_(649995)

except ImportError:
    pass

def _directory():
    _l_(650006)

    aux = _c_(650004, _a_(649998, _a_(649997, _n_(649996, "os", lambda: os), "path"), "dirname"), _c_(650003, _a_(650001, _a_(650000, _n_(649999, "os", lambda: os), "path"), "abspath"), _n_(650002, "__file__", lambda: __file__)))
    _l_(650005)
    return aux

def _file(fileTarget):
    _l_(650015)

    aux = _c_(650013, _a_(650009, _a_(650008, _n_(650007, "os", lambda: os), "path"), "join"), _c_(650011, _n_(650010, "_directory", lambda: _directory)), _n_(650012, "fileTarget", lambda: fileTarget))
    _l_(650014)
    return aux

def isFileExists(fileTarget):
    _l_(650024)

    aux = _c_(650022, _a_(650018, _a_(650017, _n_(650016, "os", lambda: os), "path"), "exists"), _c_(650021, _n_(650019, "_file", lambda: _file), _n_(650020, "fileTarget", lambda: fileTarget)))
    _l_(650023)
    return aux

def cookieCheckActive(f):
    _l_(650060)

    @_c_(650027, _n_(650025, "wraps", lambda: wraps), _n_(650026, "f", lambda: f))
    def wrapper(*args, **kwargs):
        _l_(650057)

        _active = _c_(650031, _a_(650030, _a_(650029, _n_(650028, "request", lambda: request), "cookies"), "get"), '_active', '')
        _l_(650032)
        _u      = _c_(650036, _a_(650035, _a_(650034, _n_(650033, "request", lambda: request), "cookies"), "get"), '_u', '')
        _l_(650037)

        if _n_(650038, "_active", lambda: _active) != '' and _n_(650039, "_active", lambda: _active) == '1' and 'login' not in _n_(650040, "session", lambda: session):
            _l_(650056)

            _n_(650041, "session", lambda: session)['login']  = '1'
            _l_(650042)
            _n_(650043, "session", lambda: session)['userID'] = _n_(650044, "_u", lambda: _u)
            _l_(650045)
            aux = _c_(650049, _n_(650046, "redirect", lambda: redirect), _c_(650048, _n_(650047, "url_for", lambda: url_for), 'business_dashboard.dashboard'))
            _l_(650050)

            return aux
        else:
            aux = _c_(650054, _n_(650051, "f", lambda: f), *_n_(650052, "args", lambda: args), **_n_(650053, "kwargs", lambda: kwargs))
            _l_(650055)
            return aux
    aux = _n_(650058, "wrapper", lambda: wrapper)
    _l_(650059)
    return aux

def ifLogin(f):
    _l_(650080)

    @_c_(650063, _n_(650061, "wraps", lambda: wraps), _n_(650062, "f", lambda: f))
    def wrapper(*args, **kwargs):
        _l_(650077)

        if 'login' in _n_(650064, "session", lambda: session) and _n_(650065, "session", lambda: session)['login'] == '1':
            _l_(650076)

            aux = _c_(650069, _n_(650066, "redirect", lambda: redirect), _c_(650068, _n_(650067, "url_for", lambda: url_for), 'business_dashboard.dashboard'))
            _l_(650070)
            return aux
        else:
            aux = _c_(650074, _n_(650071, "f", lambda: f), *_n_(650072, "args", lambda: args), **_n_(650073, "kwargs", lambda: kwargs))
            _l_(650075)
            return aux
    aux = _n_(650078, "wrapper", lambda: wrapper)
    _l_(650079)
    return aux

def ifNotLogin(f):
    _l_(650106)

    @_c_(650083, _n_(650081, "wraps", lambda: wraps), _n_(650082, "f", lambda: f))
    def wrapper(*args, **kwargs):
        _l_(650103)

        cookieUserID = _c_(650087, _a_(650086, _a_(650085, _n_(650084, "request", lambda: request), "cookies"), "get"), '_u', '') if '_u' in _a_(650089, _n_(650088, "request", lambda: request), "cookies") else None
        _l_(650090)

        if 'login' not in _n_(650091, "session", lambda: session):
            _l_(650102)

            aux = _c_(650095, _n_(650092, "redirect", lambda: redirect), _c_(650094, _n_(650093, "url_for", lambda: url_for), 'business_login.login'))
            _l_(650096)
            return aux
        # elif cookieUserID == None:
        #     '''
        #         I'm so confuse with this block of code; cause if i will not
        #         remember my session eventhough it must equals to NONE it return
        #         to true and store the cookie but when i reverse it, then the trouble
        #         comes in when you are logging in.
        #     '''
        #     if cookieUserID != session['userID']:
        #         session.clear()
        #
        #         today   = datetime.datetime.now()
        #         expires = datetime.timedelta(days=1)
        #         expires = today - expires
        #
        #         response = make_response(redirect(url_for('business_login.login')))
        #
        #         response.set_cookie('_u', '', expires = expires)
        #         response.set_cookie('_active', '', expires = expires)
        #
        #         return response
        else:
            aux = _c_(650100, _n_(650097, "f", lambda: f), *_n_(650098, "args", lambda: args), **_n_(650099, "kwargs", lambda: kwargs))
            _l_(650101)
            return aux
    aux = _n_(650104, "wrapper", lambda: wrapper)
    _l_(650105)
    return aux

app = _c_(650109, _n_(650107, "Flask", lambda: Flask), _n_(650108, "__name__", lambda: __name__))
_l_(650110)

_n_(650111, "app", lambda: app).secret_key = b'\x0c\xcd\xc4\x95ri\xb9\xb2O\xea\xd9\xea\x87&*\xb3'
_l_(650112)

_dbconfig = _c_(650121, _a_(650114, _n_(650113, "yaml", lambda: yaml), "load"), _c_(650118, _n_(650115, "open", lambda: open), _c_(650117, _n_(650116, "_file", lambda: _file), 'config/dbconnection.yaml')), Loader = _a_(650120, _n_(650119, "yaml", lambda: yaml), "FullLoader"))
_l_(650122)

_a_(650124, _n_(650123, "app", lambda: app), "config")['MYSQL_HOST']        = _n_(650125, "_dbconfig", lambda: _dbconfig)['DB_HOST']
_l_(650126)
_a_(650128, _n_(650127, "app", lambda: app), "config")['MYSQL_USER']        = _n_(650129, "_dbconfig", lambda: _dbconfig)['DB_USERNAME']
_l_(650130)
_a_(650132, _n_(650131, "app", lambda: app), "config")['MYSQL_PASSWORD']    = _n_(650133, "_dbconfig", lambda: _dbconfig)['DB_PASSWORD']
_l_(650134)
_a_(650136, _n_(650135, "app", lambda: app), "config")['MYSQL_DB']          = _n_(650137, "_dbconfig", lambda: _dbconfig)['DB_NAME']
_l_(650138)
_a_(650140, _n_(650139, "app", lambda: app), "config")['MYSQL_CURSORCLASS'] = 'DictCursor'
_l_(650141)

_mysql = _c_(650144, _n_(650142, "MySQL", lambda: MySQL), _n_(650143, "app", lambda: app))
_l_(650145)
try:
    from blueprints import *
    _l_(650147)

except ImportError:
    pass

@_c_(650150, _a_(650149, _n_(650148, "app", lambda: app), "errorhandler"), 404)
def page_not_found(error):
    _l_(650152)

    aux = 'page not found', 404
    _l_(650151)
    return aux

@_a_(650154, _n_(650153, "app", lambda: app), "context_processor")
def inject_dateYear():
    _l_(650162)

    aux = {'dateYear': _c_(650160, _a_(650159, _c_(650158, _a_(650157, _a_(650156, _n_(650155, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), '%Y')}
    _l_(650161)
    return aux

if _n_(650163, "__name__", lambda: __name__) == "__main__":
    _l_(650168)

    _c_(650166, _a_(650165, _n_(650164, "app", lambda: app), "run"), host='127.0.0.1', port=8080, debug=True)
    _l_(650167)