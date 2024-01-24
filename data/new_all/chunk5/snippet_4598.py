# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54575267/typeerror-for-datefield-django-xlwt-library
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xlwt
    _l_(705453)

except ImportError:
    pass
try:
    from django.http import HttpResponse
    _l_(705455)

except ImportError:
    pass
try:
    from django.contrib.auth.models import User
    _l_(705457)

except ImportError:
    pass

def GenerateCompanyCSV(request):
    _l_(705537)

    response = _c_(705459, _n_(705458, "HttpResponse", lambda: HttpResponse), content_type='application/ms-excel')
    _l_(705460)
    _n_(705461, "response", lambda: response)['Content-Disposition'] = 'attachment; filename="users.xls"'
    _l_(705462)

    wb = _c_(705465, _a_(705464, _n_(705463, "xlwt", lambda: xlwt), "Workbook"), encoding='utf-8')
    _l_(705466)
    ws = _c_(705469, _a_(705468, _n_(705467, "wb", lambda: wb), "add_sheet"), 'Users')
    _l_(705470)

    # Sheet header, first row
    row_num = 0
    _l_(705471)

    font_style = _c_(705474, _a_(705473, _n_(705472, "xlwt", lambda: xlwt), "XFStyle"))
    _l_(705475)
    _a_(705477, _n_(705476, "font_style", lambda: font_style), "font").bold = True
    _l_(705478)

    columns = ['Company Name', 'Company Email', 'Count of people','Created Date', 'Current Monthly Payment', 'Is TABopts Customer', 'Status', ]
    _l_(705479)

    for col_num in _c_(705484, _n_(705480, "range", lambda: range), _c_(705483, _n_(705481, "len", lambda: len), _n_(705482, "columns", lambda: columns))):
        _l_(705494)

        _c_(705492, _a_(705486, _n_(705485, "ws", lambda: ws), "write"), _n_(705487, "row_num", lambda: row_num), _n_(705488, "col_num", lambda: col_num), _n_(705489, "columns", lambda: columns)[_n_(705490, "col_num", lambda: col_num)], _n_(705491, "font_style", lambda: font_style))
        _l_(705493)

    # Sheet body, remaining rows
    font_style = _c_(705497, _a_(705496, _n_(705495, "xlwt", lambda: xlwt), "XFStyle"))
    _l_(705498)

    rows = _c_(705510, _a_(705509, _c_(705508, _a_(705505, _c_(705504, _a_(705503, _c_(705502, _a_(705501, _a_(705500, _n_(705499, "Company", lambda: Company), "objects"), "exclude"), id=1), "exclude"), company_is_deleted=True
                ), "annotate"), number_of_company_users=_c_(705507, _n_(705506, "Count", lambda: Count), 'userprofile')
                ), "values_list"), 'company_name', 
                    'company_email', 
                    'number_of_company_users',
                    'company_created',
                    'company_monthly_payment', 
                    'company_tab_opts',
                    'company_status',

                )
    _l_(705511)
    for row in _n_(705512, "rows", lambda: rows):
        _l_(705529)

        row_num += 1
        _l_(705513)
        for col_num in _c_(705518, _n_(705514, "range", lambda: range), _c_(705517, _n_(705515, "len", lambda: len), _n_(705516, "row", lambda: row))):
            _l_(705528)

            _c_(705526, _a_(705520, _n_(705519, "ws", lambda: ws), "write"), _n_(705521, "row_num", lambda: row_num), _n_(705522, "col_num", lambda: col_num), _n_(705523, "row", lambda: row)[_n_(705524, "col_num", lambda: col_num)], _n_(705525, "font_style", lambda: font_style))
            _l_(705527)

    _c_(705533, _a_(705531, _n_(705530, "wb", lambda: wb), "save"), _n_(705532, "response", lambda: response))
    _l_(705534)
    aux = _n_(705535, "response", lambda: response)
    _l_(705536)
    return aux