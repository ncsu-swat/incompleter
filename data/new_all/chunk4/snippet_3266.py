# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76435889/attributeerror-nonetype-object-has-no-attribute-encode-in-flask-app
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(603212, _a_(603211, _n_(603210, "app", lambda: app), "route"), '/signup', methods=['GET', 'POST'])
def signup():
    _l_(603289)

    if _a_(603214, _n_(603213, "request", lambda: request), "method") == 'POST':
        _l_(603285)

        first_name = _c_(603218, _a_(603217, _a_(603216, _n_(603215, "request", lambda: request), "form"), "get"), 'first_name')
        _l_(603219)
        last_name = _c_(603223, _a_(603222, _a_(603221, _n_(603220, "request", lambda: request), "form"), "get"), 'last_name')
        _l_(603224)
        email = _c_(603228, _a_(603227, _a_(603226, _n_(603225, "request", lambda: request), "form"), "get"), 'email')
        _l_(603229)
        password = _c_(603233, _a_(603232, _a_(603231, _n_(603230, "request", lambda: request), "form"), "get"), 'password')
        _l_(603234)
        phone_number = _c_(603238, _a_(603237, _a_(603236, _n_(603235, "request", lambda: request), "form"), "get"), 'phone_number')
        _l_(603239)
        account_type = _c_(603243, _a_(603242, _a_(603241, _n_(603240, "request", lambda: request), "form"), "get"), 'account_type')
        _l_(603244)

        #check if theres already an account using the provided email
        exist = _c_(603251, _a_(603250, _c_(603249, _a_(603247, _a_(603246, _n_(603245, "User", lambda: User), "query"), "filter_by"), email=_n_(603248, "email", lambda: email)), "first"))
        _l_(603252)
        if _n_(603253, "exist", lambda: exist):
            _l_(603260)

            _c_(603255, _n_(603254, "flash", lambda: flash), "Email already exists")
            _l_(603256)
            aux = _c_(603258, _n_(603257, "redirect", lambda: redirect), '/login')
            _l_(603259)
            return aux

        # Hash the password before storing it in the database
        _c_(603263, _n_(603261, "print", lambda: print), _n_(603262, "password", lambda: password))
        _l_(603264)
        hashed_password = _c_(603267, _n_(603265, "generate_password_hash", lambda: generate_password_hash), _n_(603266, "password", lambda: password))
        _l_(603268)

        # Create a new User object
        user = _c_(603276, _n_(603269, "User", lambda: User), first_name=_n_(603270, "first_name", lambda: first_name), last_name=_n_(603271, "last_name", lambda: last_name), email=_n_(603272, "email", lambda: email),
                    password=_n_(603273, "hashed_password", lambda: hashed_password), phone_number=_n_(603274, "phone_number", lambda: phone_number), account_type=_n_(603275, "account_type", lambda: account_type))
        _l_(603277)

        # Add the user to the database
        _c_(603280, _n_(603278, "add_user", lambda: add_user), _n_(603279, "user", lambda: user))
        _l_(603281)
        aux = _c_(603283, _n_(603282, "redirect", lambda: redirect), '/login')
        _l_(603284)

        return aux
    aux = _c_(603287, _n_(603286, "render_template", lambda: render_template), 'html/signup.html')
    _l_(603288)

    return aux