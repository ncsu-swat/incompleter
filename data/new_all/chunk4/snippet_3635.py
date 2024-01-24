# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70921863/fastapi-mongodb-error-id-struser-id-typeerror-string-indices-must
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(585847, _a_(585846, _n_(585845, "authentication", lambda: authentication), "post"), '/login')
async def login(form_email: _n_(585848, "OAuth2PasswordRequestForm", lambda: OAuth2PasswordRequestForm) = _c_(585850, _n_(585849, "Depends", lambda: Depends)),
                form_password: _n_(585851, "OAuth2PasswordRequestForm", lambda: OAuth2PasswordRequestForm) = _c_(585853, _n_(585852, "Depends", lambda: Depends))):
    _l_(585894)

    email = _c_(585860, _n_(585854, "users_serializer", lambda: users_serializer), _c_(585859, _a_(585856, _n_(585855, "user_list", lambda: user_list), "find_one"), {"email": _a_(585858, _n_(585857, "form_email", lambda: form_email), "username")}))
    _l_(585861)
    password = _c_(585868, _n_(585862, "users_serializer", lambda: users_serializer), _c_(585867, _a_(585864, _n_(585863, "user_list", lambda: user_list), "find_one"), {"password": _a_(585866, _n_(585865, "form_password", lambda: form_password), "password")}))
    _l_(585869)
    _c_(585872, _n_(585870, "print", lambda: print), _n_(585871, "email", lambda: email))
    _l_(585873)
    _c_(585876, _n_(585874, "print", lambda: print), _n_(585875, "password", lambda: password))
    _l_(585877)
    if _a_(585879, _n_(585878, "form_email", lambda: form_email), "username") == _n_(585880, "email", lambda: email):
        _l_(585888)

        if _a_(585882, _n_(585881, "form_password", lambda: form_password), "password") == _n_(585883, "password", lambda: password):
            _l_(585887)

            aux = {"status": "ok", "details": f"Welcome! {_a_(585885, _n_(585884, 'form_email', lambda: form_email), 'username')} "}
            _l_(585886)
            return aux
    raise _c_(585892, _n_(585889, "HTTPException", lambda: HTTPException), status_code=_a_(585891, _n_(585890, "status", lambda: status), "HTTP_404_NOT_FOUND"), detail='Incorrect email or password')
    _l_(585893)