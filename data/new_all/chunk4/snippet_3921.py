# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65307806/attributeerror-shiftchangefilter-object-has-no-attribute-values-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.utils import timezone
    _l_(642150)

except ImportError:
    pass
now_aware = _c_(642153, _a_(642152, _n_(642151, "timezone", lambda: timezone), "now"))
_l_(642154)
try:
    import xlwt,openpyxl
    _l_(642156)

except ImportError:
    pass
def exportgenesys_data(request):
    _l_(642243)

    allgenesys = _c_(642160, _a_(642159, _a_(642158, _n_(642157, "ShiftChange", lambda: ShiftChange), "objects"), "all"))
    _l_(642161)
    genesys_filter = _c_(642166, _n_(642162, "ShiftChangeFilter", lambda: ShiftChangeFilter), _a_(642164, _n_(642163, "request", lambda: request), "GET"),queryset=_n_(642165, "allgenesys", lambda: allgenesys) )
    _l_(642167)
    _c_(642171, _n_(642168, "print", lambda: print), 'download:',_a_(642170, _n_(642169, "genesys_filter", lambda: genesys_filter), "qs"))
    _l_(642172)

    response = _c_(642174, _n_(642173, "HttpResponse", lambda: HttpResponse), content_type='application/ms-excel')
    _l_(642175)
    _n_(642176, "response", lambda: response)['Content-Disposition'] = 'attachment; filename="Genesys_ShiftTiming.xls"'
    _l_(642177)
    wb = _c_(642180, _a_(642179, _n_(642178, "xlwt", lambda: xlwt), "Workbook"), encoding='utf-8')
    _l_(642181)
    ws = _c_(642184, _a_(642183, _n_(642182, "wb", lambda: wb), "add_sheet"), 'GenesysShiftChange Data')  # this will make a sheet named Users Data
    _l_(642185)  # this will make a sheet named Users Data
    # Sheet header, first row
    row_num = 0
    _l_(642186)
    font_style = _c_(642189, _a_(642188, _n_(642187, "xlwt", lambda: xlwt), "XFStyle"))
    _l_(642190)
    _a_(642192, _n_(642191, "font_style", lambda: font_style), "font").bold = True
    _l_(642193)
    columns = ['id', 'ConnectID', 'Shift_timing', 'EmailID', 'Vendor_Company', 'Project_name', 'SerialNumber',
               'Reason', 'last_updated_time']
    _l_(642194)
    for col_num in _c_(642199, _n_(642195, "range", lambda: range), _c_(642198, _n_(642196, "len", lambda: len), _n_(642197, "columns", lambda: columns))):
        _l_(642209)

        _c_(642207, _a_(642201, _n_(642200, "ws", lambda: ws), "write"), _n_(642202, "row_num", lambda: row_num), _n_(642203, "col_num", lambda: col_num), _n_(642204, "columns", lambda: columns)[_n_(642205, "col_num", lambda: col_num)], _n_(642206, "font_style", lambda: font_style))  # at 0 row 0 column
        _l_(642208)  # at 0 row 0 column
    # Sheet body, remaining rows
    font_style = _c_(642212, _a_(642211, _n_(642210, "xlwt", lambda: xlwt), "XFStyle"))
    _l_(642213)
    rows = _c_(642216, _a_(642215, _n_(642214, "genesys_filter", lambda: genesys_filter), "values_list"), 'id', 'ConnectID', 'Shift_timing',
                           'EmailID', 'Vendor_Company', 'Project_name',
                           'SerialNumber', 'Reason', 'last_updated_time')
    _l_(642217)


    for row in _n_(642218, "rows", lambda: rows):
        _l_(642235)

        row_num += 1
        _l_(642219)
        for col_num in _c_(642224, _n_(642220, "range", lambda: range), _c_(642223, _n_(642221, "len", lambda: len), _n_(642222, "row", lambda: row))):
            _l_(642234)

            _c_(642232, _a_(642226, _n_(642225, "ws", lambda: ws), "write"), _n_(642227, "row_num", lambda: row_num), _n_(642228, "col_num", lambda: col_num), _n_(642229, "row", lambda: row)[_n_(642230, "col_num", lambda: col_num)], _n_(642231, "font_style", lambda: font_style))
            _l_(642233)
    _c_(642239, _a_(642237, _n_(642236, "wb", lambda: wb), "save"), _n_(642238, "response", lambda: response))
    _l_(642240)
    aux = _n_(642241, "response", lambda: response)
    _l_(642242)
    return aux