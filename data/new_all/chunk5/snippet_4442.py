# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57703151/typeerror-loads-got-an-unexpected-keyword-argument-max
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(673053, _a_(673052, _n_(673051, "app", lambda: app), "route"), '/email_confirm/<token>')
def confirm_mail(token):
    _l_(673060)

    email = _c_(673057, _a_(673055, _n_(673054, "s", lambda: s), "loads"), _n_(673056, "token", lambda: token), salt='email-confirm', max_age=20)
    _l_(673058)
    aux = '<h1>The token works !</h1>'
    _l_(673059)
    return aux