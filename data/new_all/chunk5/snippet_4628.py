# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53906364/attributeerror-nonetype-object-has-no-attribute-split-sending-post-request
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(701992, "require_POST", lambda: require_POST)
def user_login(request):
    _l_(702056)

    data = _c_(701999, _a_(701994, _n_(701993, "json", lambda: json), "loads"), _c_(701998, _a_(701997, _a_(701996, _n_(701995, "request", lambda: request), "body"), "decode"), 'utf-8'))
    _l_(702000)
    phone_number = _n_(702001, "data", lambda: data)['phone_number']
    _l_(702002)
    password = _n_(702003, "data", lambda: data)['password']
    _l_(702004)
    user = _c_(702008, _n_(702005, "authenticate", lambda: authenticate), phone_number=_n_(702006, "phone_number", lambda: phone_number), password=_n_(702007, "password", lambda: password))
    _l_(702009)
    if _n_(702010, "user", lambda: user) is None:
        _l_(702020)

        message = 'The username or password is wrong.'
        _l_(702011)
        _c_(702014, _n_(702012, "print", lambda: print), _n_(702013, "message", lambda: message))
        _l_(702015)
        aux = _c_(702018, _n_(702016, "JsonResponse", lambda: JsonResponse), {'message':_n_(702017, "message", lambda: message)},status=406)
        _l_(702019)
        return aux
    if not _a_(702022, _n_(702021, "user", lambda: user), "two_step_auth"):
        _l_(702037)

        _c_(702026, _n_(702023, "login", lambda: login), _n_(702024, "request", lambda: request),_n_(702025, "user", lambda: user))
        _l_(702027)
        message='successfully loged in'
        _l_(702028)
        _c_(702031, _n_(702029, "print", lambda: print), _n_(702030, "message", lambda: message))
        _l_(702032)
        aux = _c_(702035, _n_(702033, "JsonResponse", lambda: JsonResponse), {'message':_n_(702034, "message", lambda: message)}, status=200)
        _l_(702036)
        return aux
    gg = _c_(702040, _n_(702038, "generate_activation_code", lambda: generate_activation_code), _n_(702039, "phone_number", lambda: phone_number))
    _l_(702041)
    if _n_(702042, "gg", lambda: gg):
        _l_(702052)

        message='The Activation code has been sent to your phone'
        _l_(702043)
        _c_(702046, _n_(702044, "print", lambda: print), _n_(702045, "message", lambda: message))
        _l_(702047)
        aux = _c_(702050, _n_(702048, "JsonResponse", lambda: JsonResponse), {'message':_n_(702049, "message", lambda: message)}, status=200)
        _l_(702051)
        return aux
    aux = _c_(702054, _n_(702053, "JsonResponse", lambda: JsonResponse), {}, status=400)
    _l_(702055)
    return aux