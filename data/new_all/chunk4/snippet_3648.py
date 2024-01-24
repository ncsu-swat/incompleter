# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70706978/loginmanager-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from flask import Flask
    _l_(617198)

except ImportError:
    pass
try:
    from flask_login import LoginManager
    _l_(617200)

except ImportError:
    pass
try:
    from .views import views
    _l_(617202)

except ImportError:
    pass
try:
    from .models import db,User
    _l_(617204)

except ImportError:
    pass
try:
    from flask_mobility import Mobility
    _l_(617206)

except ImportError:
    pass
try:
    from os import path
    _l_(617208)

except ImportError:
    pass

DB_NAME="database.db"
_l_(617209)

def create_app():
    _l_(617252)

    app=_c_(617212, _n_(617210, "Flask", lambda: Flask), _n_(617211, "__name__", lambda: __name__))
    _l_(617213)
    _c_(617216, _n_(617214, "Mobility", lambda: Mobility), _n_(617215, "app", lambda: app))
    _l_(617217)
    
    loginmanager=_c_(617220, _n_(617218, "LoginManager", lambda: LoginManager), _n_(617219, "app", lambda: app))
    _l_(617221)
    _c_(617224, _a_(617223, _n_(617222, "loginmanager", lambda: loginmanager), "login_view"), 'auth.login')
    _l_(617225)

    _a_(617227, _n_(617226, "app", lambda: app), "config")['SECRET_KEY']='no nothing nobody'
    _l_(617228)
    _a_(617230, _n_(617229, "app", lambda: app), "config")['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{_n_(617231, "DB_NAME", lambda: DB_NAME)}'
    _l_(617232)
    _a_(617234, _n_(617233, 'app', lambda: app), 'config')['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    _l_(617235)
    _c_(617239, _a_(617237, _n_(617236, 'db', lambda: db), 'init_app'), _n_(617238, 'app', lambda: app))
    _l_(617240)
    _c_(617244, _a_(617242, _n_(617241, 'app', lambda: app), 'register_blueprint'), _n_(617243, 'views', lambda: views), url_prefix='/')
    _l_(617245)
    _c_(617248, _n_(617246, 'create_database', lambda: create_database), _n_(617247, 'app', lambda: app))
    _l_(617249)
    aux = _n_(617250, 'app', lambda: app)
    _l_(617251)
    return aux

def create_database(app):
    _l_(617263)

    if not _c_(617256, _a_(617254, _n_(617253, 'path', lambda: path), 'exists'), 'website/'+_n_(617255, 'DB_NAME', lambda: DB_NAME)):
        _l_(617262)

        _c_(617260, _a_(617258, _n_(617257, 'db', lambda: db), 'create_all'), app=_n_(617259, 'app', lambda: app))
        _l_(617261)