# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59425913/typeerror-object-of-type-location-is-not-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(556788, _a_(556787, _n_(556786, "app", lambda: app), "route"), '/register', methods=['GET', 'POST'])
def register_user():
    _l_(556865)

    if _a_(556790, _n_(556789, "request", lambda: request), "method") == 'POST':
        _l_(556861)

        login_user = _a_(556793, _a_(556792, _n_(556791, "mongo", lambda: mongo), "db"), "mylogin")
        _l_(556794)
        existing_user = _c_(556799, _a_(556796, _n_(556795, "login_user", lambda: login_user), "find_one"), {'email': _a_(556798, _n_(556797, "request", lambda: request), "form")['email']})
        _l_(556800)
        # final_location = geolocator.geocode(session['address'].encode('utf-8'))
        if _n_(556801, "existing_user", lambda: existing_user) is None:
            _l_(556852)

            hashpass = _c_(556811, _a_(556803, _n_(556802, "bcrypt", lambda: bcrypt), "hashpw"), _c_(556807, _a_(556806, _a_(556805, _n_(556804, "request", lambda: request), "form")['pass'], "encode"), 'utf-8'), _c_(556810, _a_(556809, _n_(556808, "bcrypt", lambda: bcrypt), "gensalt")))
            _l_(556812)
            _c_(556823, _a_(556814, _n_(556813, "login_user", lambda: login_user), "insert"), {'name': _a_(556816, _n_(556815, "request", lambda: request), "form")['username'], 'email': _a_(556818, _n_(556817, "request", lambda: request), "form")['email'], 'password': _n_(556819, "hashpass", lambda: hashpass), 'address': _a_(556821, _n_(556820, "request", lambda: request), "form")['add'], 'location' : _n_(556822, "session", lambda: session)['location'] })
            _l_(556824)
            _n_(556825, "session", lambda: session)['password'] = _a_(556827, _n_(556826, "request", lambda: request), "form")['pass']
            _l_(556828)
            _n_(556829, "session", lambda: session)['username'] = _a_(556831, _n_(556830, "request", lambda: request), "form")['username']
            _l_(556832)
            _n_(556833, "session", lambda: session)['address'] = _a_(556835, _n_(556834, "request", lambda: request), "form")['add']
            _l_(556836)
            _n_(556837, "session", lambda: session)['location'] = _c_(556841, _a_(556839, _n_(556838, "geolocator", lambda: geolocator), "geocode"), _n_(556840, "session", lambda: session)['address'])
            _l_(556842)
            _c_(556845, _n_(556843, "flash", lambda: flash), f"You are Registerd as {_n_(556844, 'session', lambda: session)['username']}")
            _l_(556846)
            aux = _c_(556850, _n_(556847, "redirect", lambda: redirect), _c_(556849, _n_(556848, "url_for", lambda: url_for), 'home'))
            _l_(556851)
            return aux
        _c_(556854, _n_(556853, "flash", lambda: flash), 'Username is taken !')
        _l_(556855)
        aux = _c_(556859, _n_(556856, "redirect", lambda: redirect), _c_(556858, _n_(556857, "url_for", lambda: url_for), 'home'))
        _l_(556860)
        return aux
    aux = _c_(556863, _n_(556862, "render_template", lambda: render_template), 'index.html')
    _l_(556864)
    return aux