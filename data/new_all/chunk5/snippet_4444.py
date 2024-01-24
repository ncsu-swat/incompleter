# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57703151/typeerror-loads-got-an-unexpected-keyword-argument-max
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(694529, _a_(694528, _n_(694527, "app", lambda: app), "route"), '/email_confirm/<token>')
def confirm_mail(token):
    _l_(694536)

    email = _c_(694533, _a_(694531, _n_(694530, "s", lambda: s), "loads"), _n_(694532, "token", lambda: token), salt='email-confirm', max_age=20)
    _l_(694534)
    aux = '<h1>The token works !</h1>'
    _l_(694535)
    return aux