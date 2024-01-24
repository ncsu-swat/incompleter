# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31687808/csv-reader-typeerror-unsupported-operand-types-for-nonetype-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def csv_dict_reader(file_obj, x_obj, n_obj):
    _l_(704867)


    data_in_list = []
    _l_(704775)
    x=0
    _l_(704776)

    reader = _c_(704780, _a_(704778, _n_(704777, "csv", lambda: csv), "DictReader"), _n_(704779, "file_obj", lambda: file_obj), delimiter=',')
    _l_(704781)
    f = _c_(704785, _a_(704783, _n_(704782, "csv", lambda: csv), "writer"), _n_(704784, "x_obj", lambda: x_obj), delimiter=',', quotechar='"')
    _l_(704786)
    f1= _c_(704790, _a_(704788, _n_(704787, "csv", lambda: csv), "writer"), _n_(704789, "x_obj", lambda: x_obj), delimiter=',', quotechar='"')
    _l_(704791)
    f2= _c_(704795, _a_(704793, _n_(704792, "csv", lambda: csv), "writer"), _n_(704794, "n_obj", lambda: n_obj), delimiter=',', quotechar='"')
    _l_(704796)

    _c_(704799, _a_(704798, _n_(704797, "f1", lambda: f1), "writerow"), ["name","email","external_id","details","notes","phone","role","restriction","organization","tags"])
    _l_(704800)
    _c_(704803, _a_(704802, _n_(704801, "f2", lambda: f2), "writerow"), ["name","email","phone","office","department", "role"])
    _l_(704804)

    for row in _n_(704805, "reader", lambda: reader):
        _l_(704864)

        _c_(704809, _a_(704807, _n_(704806, "data_in_list", lambda: data_in_list), "append"), _n_(704808, "row", lambda: row))
        _l_(704810)

        name = _n_(704811, "data_in_list", lambda: data_in_list)[_n_(704812, "x", lambda: x)]['firstname'] + " " + _n_(704813, "data_in_list", lambda: data_in_list)[_n_(704814, "x", lambda: x)]['surname']
        _l_(704815)
        firm = _n_(704816, "data_in_list", lambda: data_in_list)[_n_(704817, "x", lambda: x)]['firm']
        _l_(704818)
        phone = _n_(704819, "data_in_list", lambda: data_in_list)[_n_(704820, "x", lambda: x)]['phone']
        _l_(704821)
        email = _n_(704822, "data_in_list", lambda: data_in_list)[_n_(704823, "x", lambda: x)]['email']
        _l_(704824)
        office = _n_(704825, "data_in_list", lambda: data_in_list)[_n_(704826, "x", lambda: x)]['office']
        _l_(704827)
        department = _n_(704828, "data_in_list", lambda: data_in_list)[_n_(704829, "x", lambda: x)]['dept']
        _l_(704830)
        details = ","
        _l_(704831)
        notes = ","
        _l_(704832)
        role = _n_(704833, "data_in_list", lambda: data_in_list)[_n_(704834, "x", lambda: x)]['role']
        _l_(704835)
        restrictions = ","
        _l_(704836)
        tags = ","
        _l_(704837)

        _c_(704850, _a_(704839, _n_(704838, "f", lambda: f), "writerow"), [_n_(704840, "name", lambda: name)] + [_n_(704841, "email", lambda: email)] + [_n_(704842, "details", lambda: details)] + [_n_(704843, "phone", lambda: phone)] + [_n_(704844, "role", lambda: role)] + 
               [_n_(704845, "restrictions", lambda: restrictions)] + [_n_(704846, "firm", lambda: firm)] + [_n_(704847, "tags", lambda: tags)] + [_n_(704848, "office", lambda: office)] + [_n_(704849, "department", lambda: department)])
        _l_(704851)
        _c_(704860, _a_(704853, _n_(704852, "f2", lambda: f2), "writerow"), [_n_(704854, "name", lambda: name)] + [_n_(704855, "email", lambda: email)] + [_n_(704856, "phone", lambda: phone)] + [_n_(704857, "office", lambda: office)] + [_n_(704858, "department", lambda: department)] + [_n_(704859, "role", lambda: role)])
        _l_(704861)

        x= _n_(704862, "x", lambda: x)+1
        _l_(704863)
    aux = _n_(704865, "data_in_list", lambda: data_in_list)
    _l_(704866)
    return aux

if _n_(704868, "__name__", lambda: __name__) == "__main__":
    _l_(704884)


    with _c_(704870, _n_(704869, "open", lambda: open), "stafflist11.csv") as f_obj:
        _l_(704883)

        with _c_(704872, _n_(704871, "open", lambda: open), "new.csv", "w") as x_obj:
            _l_(704882)

            with _c_(704874, _n_(704873, "open", lambda: open), "user_databse_nepo.csv", "w") as n_obj:
                _l_(704881)

                _c_(704879, _n_(704875, "csv_dict_reader", lambda: csv_dict_reader), _n_(704876, "f_obj", lambda: f_obj), _n_(704877, "x_obj", lambda: x_obj), _n_(704878, "n_obj", lambda: n_obj))
                _l_(704880)