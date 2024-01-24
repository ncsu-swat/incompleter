# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66959972/attributeerror-method-object-has-no-attribute-backend
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.shortcuts import render
    _l_(423884)

except ImportError:
    pass
try:
    from django.http import HttpResponse, HttpRequest
    _l_(423886)

except ImportError:
    pass
try:
    from django.shortcuts import redirect
    _l_(423888)

except ImportError:
    pass
try:
    from django.contrib.auth import authenticate, login
    _l_(423890)

except ImportError:
    pass
try:
    import requests
    _l_(423892)

except ImportError:
    pass

client_id = "my_id"
_l_(423893)

def home_view(request: _n_(423894, "HttpRequest", lambda: HttpRequest), *args, **kwargs):
    _l_(423913)

    code = _c_(423898, _a_(423897, _a_(423896, _n_(423895, "request", lambda: request), "GET"), "get"), "code")
    _l_(423899)
    user = _c_(423902, _n_(423900, "exchange_code", lambda: exchange_code), _n_(423901, "code", lambda: code))
    _l_(423903)
    _c_(423907, _n_(423904, "authenticate", lambda: authenticate), _n_(423905, "request", lambda: request), user=_n_(423906, "user", lambda: user))
    _l_(423908)
    aux = _c_(423911, _n_(423909, "render", lambda: render), _n_(423910, "request", lambda: request), "home.html", {})
    _l_(423912)
    return aux

def exchange_code(code: _n_(423914, "str", lambda: str)):
    _l_(423950)

    data = {
        "client_id": _n_(423915, "client_id", lambda: client_id),
        "client_secret": "my_secret",
        "grant_type": "authorization_code",
        "code": _n_(423916, "code", lambda: code),
        "redirect_uri": "http://localhost:8000/home/",
        "scope": "identify guilds"
    }
    _l_(423917)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    _l_(423918)

    response = _c_(423923, _a_(423920, _n_(423919, "requests", lambda: requests), "post"), "https://discord.com/api/oauth2/token", data=_n_(423921, "data", lambda: data), headers=_n_(423922, "headers", lambda: headers))
    _l_(423924)
    credentials = _c_(423927, _a_(423926, _n_(423925, "response", lambda: response), "json"))
    _l_(423928)
    
    access_token = _n_(423929, "credentials", lambda: credentials)['access_token']
    _l_(423930)
    response = _c_(423934, _a_(423932, _n_(423931, "requests", lambda: requests), "get"), 'https://discord.com/api/v6/users/@me', headers={
        'Authorization': 'Bearer %s' % _n_(423933, "access_token", lambda: access_token)
    })
    _l_(423935)
    _c_(423938, _n_(423936, "print", lambda: print), _n_(423937, "response", lambda: response))
    _l_(423939)
    user = _c_(423942, _a_(423941, _n_(423940, "response", lambda: response), "json"))
    _l_(423943)
    _c_(423946, _n_(423944, "print", lambda: print), _n_(423945, "user", lambda: user))
    _l_(423947)
    aux = _n_(423948, "user", lambda: user)
    _l_(423949)
    return aux