# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66194956/typeerror-contact-got-an-unexpected-keyword-argument-name-while-using-flask
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_c_(538022, _a_(538021, _n_(538020, "app", lambda: app), "route"), "/contact", methods=['GET', 'POST'])
def contact():
    _l_(538071)

    if (_a_(538024, _n_(538023, "request", lambda: request), "method") == 'POST'):
        _l_(538067)

        '''Add entry to the database'''
        _l_(538025)
        Name = _c_(538029, _a_(538028, _a_(538027, _n_(538026, "request", lambda: request), "form"), "get"), 'Name')
        _l_(538030)
        Email = _c_(538034, _a_(538033, _a_(538032, _n_(538031, "request", lambda: request), "form"), "get"), 'Email')
        _l_(538035)
        Phone = _c_(538039, _a_(538038, _a_(538037, _n_(538036, "request", lambda: request), "form"), "get"), 'Phone_no')
        _l_(538040)
        Message = _c_(538044, _a_(538043, _a_(538042, _n_(538041, "request", lambda: request), "form"), "get"), 'Msg')
        _l_(538045)
        entry = _c_(538054, _n_(538046, "contact", lambda: contact), name=_n_(538047, "Name", lambda: Name), email=_n_(538048, "Email", lambda: Email), phone_no=_n_(538049, "Phone", lambda: Phone), msg=_n_(538050, "Message", lambda: Message), date=_c_(538053, _a_(538052, _n_(538051, "datetime", lambda: datetime), "now")))
        _l_(538055)
        _c_(538060, _a_(538058, _a_(538057, _n_(538056, "db", lambda: db), "session"), "add"), _n_(538059, "entry", lambda: entry))
        _l_(538061)
        _c_(538065, _a_(538064, _a_(538063, _n_(538062, "db", lambda: db), "session"), "commit"))
        _l_(538066)
    aux = _c_(538069, _n_(538068, "render_template", lambda: render_template), 'contact.html')
    _l_(538070)
    return aux