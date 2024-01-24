# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56242706/flask-bcrypt-check-password-method-always-return-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(544926, _a_(544925, _n_(544924, "app", lambda: app), "route"), '/sign_up' , methods=['POST', 'GET'])
def sign_up():
    _l_(545007)

    form = _c_(544928, _n_(544927, "register_form", lambda: register_form)) # imported from forms.py file as a class
    _l_(544929) # imported from forms.py file as a class
    _c_(544932, _a_(544931, _n_(544930, "db", lambda: db), "connect"))
    _l_(544933)
    if _c_(544936, _a_(544935, _n_(544934, "form", lambda: form), "validate_on_submit")):
        _l_(545002)

        first_name = _a_(544939, _a_(544938, _n_(544937, "form", lambda: form), "first_name"), "data")
        _l_(544940)
        last_name = _a_(544943, _a_(544942, _n_(544941, "form", lambda: form), "last_name"), "data")
        _l_(544944)
        email = _a_(544947, _a_(544946, _n_(544945, "form", lambda: form), "email"), "data")
        _l_(544948)
        hashed_password = _c_(544956, _a_(544955, _c_(544954, _a_(544950, _n_(544949, "bcrypt", lambda: bcrypt), "generate_password_hash"), _a_(544953, _a_(544952, _n_(544951, "form", lambda: form), "password"), "data")), "decode"), 'utf-8')
        _l_(544957)
        _c_(544961, _a_(544959, _n_(544958, "cur", lambda: cur), "execute"), "SELECT email FROM users WHERE email ='%s'", _n_(544960, "email", lambda: (email)))
        _l_(544962)
        email_exsist = _c_(544965, _a_(544964, _n_(544963, "cur", lambda: cur), "fetchone"))
        _l_(544966)
        if _n_(544967, "email_exsist", lambda: email_exsist):
            _l_(545001)


            _c_(544969, _n_(544968, "flash", lambda: flash), 'email is already exisist','danger')
            _l_(544970)
        else :    

            _c_(544977, _a_(544972, _n_(544971, "cur", lambda: cur), "execute"), 'INSERT INTO users(first_name, last_name,email,password) VALUES(%s,%s,%s,%s)''',(_n_(544973, "first_name", lambda: first_name), _n_(544974, "last_name", lambda: last_name), _n_(544975, "email", lambda: email), _n_(544976, "hashed_password", lambda: hashed_password)) )
            _l_(544978)
            _c_(544981, _a_(544980, _n_(544979, "db", lambda: db), "commit"))
            _l_(544982)
            _c_(544990, _n_(544983, "flash", lambda: flash), f'Account Successfully created for {_a_(544986, _a_(544985, _n_(544984, "form", lambda: form), "first_name"), "data") + " " + _a_(544989, _a_(544988, _n_(544987, "form", lambda: form), "last_name"), "data")} !' , 'success' )
            _l_(544991)
            aux = _c_(544995, _n_(544992, 'redirect', lambda: redirect), _c_(544994, _n_(544993, 'url_for', lambda: url_for), 'sign_up'))
            _l_(544996)

            return aux
            _c_(544999, _a_(544998, _n_(544997, 'cur', lambda: cur), 'close'))
            _l_(545000)
    aux = _c_(545005, _n_(545003, 'render_template', lambda: render_template), 'sign_up.html' , title='Sign up' , form= _n_(545004, 'form', lambda: form))
    _l_(545006)

    return aux