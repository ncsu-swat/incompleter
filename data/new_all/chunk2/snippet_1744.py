# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58814134/why-typeerror-is-showing-while-storing-fetchone-value
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(431737, _a_(431736, _n_(431735, "app", lambda: app), "route"), '/', methods=['GET', 'POST'])
def index():
    _l_(431780)

    recur_next = ''
    _l_(431738)
    if _a_(431740, _n_(431739, "request", lambda: request), "method") == 'POST' and _a_(431742, _n_(431741, "request", lambda: request), "form")['btn']=='XYZ':
        _l_(431778)

        date = _a_(431744, _n_(431743, "request", lambda: request), "form")['date']
        _l_(431745)
        subject = 'Event'
        _l_(431746)
        reminders='Placement Drive'
        _l_(431747)
        cur = _c_(431751, _a_(431750, _a_(431749, _n_(431748, "mysql", lambda: mysql), "connection"), "cursor"))
        _l_(431752)
        search = _c_(431758, _a_(431754, _n_(431753, "cur", lambda: cur), "execute"), 'SELECT DATE,SUBJECT,DESCRIPTION,RECUR_NEXT FROM set_reminder WHERE DATE=%s AND SUBJECT=%s AND DESCRIPTION=%s',(_n_(431755, "date", lambda: date),_n_(431756, "subject", lambda: subject),_n_(431757, "reminders", lambda: reminders)))
        _l_(431759)
        data = _c_(431762, _a_(431761, _n_(431760, "cur", lambda: cur), "fetchall"))
        _l_(431763)
        a = _c_(431766, _a_(431765, _n_(431764, "cur", lambda: cur), "fetchone"))
        _l_(431767)
        recur_next = _n_(431768, "a", lambda: a)['RECUR_NEXT']
        _l_(431769)
        _c_(431772, _n_(431770, "print", lambda: print), _n_(431771, "recur_next", lambda: recur_next))
        _l_(431773)
        _c_(431776, _a_(431775, _n_(431774, "cur", lambda: cur), "close"))
        _l_(431777)
    aux = '''<form method="post">
    <input type="date" name="date">
    <input type="submit" name="btn" value="XYZ">
    </form>'''
    _l_(431779)

    return aux