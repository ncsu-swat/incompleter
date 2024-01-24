# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65530677/need-help-for-python-and-sqlite-typeerror-nonetype-object-is-not-subscrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(579063)

except ImportError:
    pass
try:
    from tkinter import ttk
    _l_(579065)

except ImportError:
    pass
try:
    from datetime import datetime
    _l_(579067)

except ImportError:
    pass
try:
    import sqlite3
    _l_(579069)

except ImportError:
    pass

class Main:
    _l_(579350)


    db_name = 'materiales.db'
    _l_(579070)
    
    def __init__(self,window):
        _l_(579157)

        _n_(579071, "self", lambda: self).wind = _n_(579072, "window", lambda: window)
        _l_(579073)
        _c_(579077, _a_(579076, _a_(579075, _n_(579074, "self", lambda: self), "wind"), "title"), 'Stock App')
        _l_(579078)

        #create frame
        frame = _c_(579082, _n_(579079, "LabelFrame", lambda: LabelFrame), _a_(579081, _n_(579080, "self", lambda: self), "wind"), text = 'Add stock')
        _l_(579083)
        _c_(579086, _a_(579085, _n_(579084, "frame", lambda: frame), "grid"), row = 0, column = 0, columnspan = 3, pady = 20)
        _l_(579087)

        # Name Input
        _c_(579092, _a_(579091, _c_(579090, _n_(579088, "Label", lambda: Label), _n_(579089, "frame", lambda: frame), text = 'Name: '), "grid"), row = 1, column = 0)
        _l_(579093)
        _n_(579094, "self", lambda: self).name = _c_(579097, _n_(579095, "Entry", lambda: Entry), _n_(579096, "frame", lambda: frame))
        _l_(579098)
        _c_(579102, _a_(579101, _a_(579100, _n_(579099, "self", lambda: self), "name"), "focus"))
        _l_(579103)
        _c_(579107, _a_(579106, _a_(579105, _n_(579104, "self", lambda: self), "name"), "grid"), row = 1, column = 1)
        _l_(579108)

        # Quantity Input
        _c_(579113, _a_(579112, _c_(579111, _n_(579109, "Label", lambda: Label), _n_(579110, "frame", lambda: frame), text = 'Quantity: '), "grid"), row = 2, column = 0)
        _l_(579114)
        _n_(579115, "self", lambda: self).quantity = _c_(579118, _n_(579116, "Entry", lambda: Entry), _n_(579117, "frame", lambda: frame))
        _l_(579119)
        _c_(579123, _a_(579122, _a_(579121, _n_(579120, "self", lambda: self), "quantity"), "grid"), row = 2, column = 1)
        _l_(579124)

        # Button Add Stock
        _c_(579134, _a_(579131, _c_(579130, _a_(579126, _n_(579125, "ttk", lambda: ttk), "Button"), _n_(579127, "frame", lambda: frame), text = 'Add Stock', command = _a_(579129, _n_(579128, "self", lambda: self), "add_stock")), "grid"), row = 3, columnspan = 2, sticky = _n_(579132, "W", lambda: W) + _n_(579133, "E", lambda: E))
        _l_(579135)

        #Log Message
        _n_(579136, "self", lambda: self).message = _c_(579138, _n_(579137, "Label", lambda: Label), text = '', fg = 'red')
        _l_(579139)
        _c_(579145, _a_(579142, _a_(579141, _n_(579140, "self", lambda: self), "message"), "grid"), row = 3, column = 0, columnspan = 2, sticky = _n_(579143, "W", lambda: W) + _n_(579144, "E", lambda: E))
        _l_(579146)

        #Button Search Stocks
        _c_(579155, _a_(579152, _c_(579151, _a_(579148, _n_(579147, "ttk", lambda: ttk), "Button"), text = 'Search Stocks', command = _a_(579150, _n_(579149, "self", lambda: self), "search_stocks")), "grid"), row = 5, column = 0, columnspan = 3, pady = 20, sticky = _n_(579153, "W", lambda: W) + _n_(579154, "E", lambda: E)) 
        _l_(579156) 



    def run_query(self, query, parameters = ()):
        _l_(579180)

        with _c_(579162, _a_(579159, _n_(579158, "sqlite3", lambda: sqlite3), "connect"), _a_(579161, _n_(579160, "self", lambda: self), "db_name")) as conn:
            _l_(579177)

            cursor = _c_(579165, _a_(579164, _n_(579163, "conn", lambda: conn), "cursor"))
            _l_(579166)
            result = _c_(579171, _a_(579168, _n_(579167, "cursor", lambda: cursor), "execute"), _n_(579169, "query", lambda: query), _n_(579170, "parameters", lambda: parameters))
            _l_(579172)
            _c_(579175, _a_(579174, _n_(579173, "conn", lambda: conn), "commit"))
            _l_(579176)
        aux = _n_(579178, "result", lambda: result)
        _l_(579179)
        return aux

    def validation(self):
        _l_(579194)

        aux = _c_(579186, _n_(579181, "len", lambda: len), _c_(579185, _a_(579184, _a_(579183, _n_(579182, "self", lambda: self), "name"), "get"))) != 0 and _c_(579192, _n_(579187, "len", lambda: len), _c_(579191, _a_(579190, _a_(579189, _n_(579188, "self", lambda: self), "quantity"), "get"))) !=0
        _l_(579193)
        return aux

    def add_stock(self):
        _l_(579281)

        time = _c_(579199, _a_(579198, _c_(579197, _a_(579196, _n_(579195, "datetime", lambda: datetime), "now")), "strftime"), "%B %d, %Y")
        _l_(579200)
        hour = _c_(579205, _a_(579204, _c_(579203, _a_(579202, _n_(579201, "datetime", lambda: datetime), "now")), "strftime"), "%I:%M%p")
        _l_(579206)
        query = 'SELECT totalstock FROM stocks WHERE name = ? AND MovementID = ( SELECT max( MovementID ) FROM stocks)'
        _l_(579207)
        parameters = (_c_(579211, _a_(579210, _a_(579209, _n_(579208, "self", lambda: self), "name"), "get")),)
        _l_(579212)
        lastrecord = _c_(579217, _a_(579214, _n_(579213, "self", lambda: self), "run_query"), _n_(579215, "query", lambda: query), _n_(579216, "parameters", lambda: parameters))
        _l_(579218)
        total = _c_(579221, _a_(579220, _n_(579219, "lastrecord", lambda: lastrecord), "fetchone"))[0]
        _l_(579222)
        total += _c_(579228, _n_(579223, "int", lambda: int), _c_(579227, _a_(579226, _a_(579225, _n_(579224, "self", lambda: self), "quantity"), "get")))
        _l_(579229)
        if _c_(579232, _a_(579231, _n_(579230, "self", lambda: self), "validation")):
            _l_(579276)

            query = 'INSERT INTO stocks VALUES(NULL, ?, ?, ?, ?, ?)'
            _l_(579233)
            parameters = (_c_(579237, _a_(579236, _a_(579235, _n_(579234, "self", lambda: self), "name"), "get")), _c_(579241, _a_(579240, _a_(579239, _n_(579238, "self", lambda: self), "quantity"), "get")), _n_(579242, "total", lambda: total), _n_(579243, "time", lambda: time), _n_(579244, "hour", lambda: hour))
            _l_(579245)
            _c_(579250, _a_(579247, _n_(579246, "self", lambda: self), "run_query"), _n_(579248, "query", lambda: query), _n_(579249, "parameters", lambda: parameters))
            _l_(579251)
            _a_(579253, _n_(579252, "self", lambda: self), "message")['text'] = _c_(579259, _a_(579254, 'Stock for {} added succesfully', "format"), _c_(579258, _a_(579257, _a_(579256, _n_(579255, "self", lambda: self), "name"), "get")))
            _l_(579260)
            _c_(579265, _a_(579263, _a_(579262, _n_(579261, "self", lambda: self), "name"), "delete"), 0, _n_(579264, "END", lambda: END))
            _l_(579266)
            _c_(579271, _a_(579269, _a_(579268, _n_(579267, "self", lambda: self), "quantity"), "delete"), 0, _n_(579270, "END", lambda: END))
            _l_(579272)
        else:
            _a_(579274, _n_(579273, "self", lambda: self), "message")['text'] = 'Name and Quantity required'
            _l_(579275)
        _c_(579279, _a_(579278, _n_(579277, "self", lambda: self), "get_product"))
        _l_(579280)

    def search_stocks(self):
        _l_(579324)

        _n_(579282, "self", lambda: self).edit_wind = _c_(579284, _n_(579283, "Toplevel", lambda: Toplevel))
        _l_(579285)
        _a_(579287, _n_(579286, "self", lambda: self), "edit_wind").title = 'Search Stocks'
        _l_(579288)

        #Name Product
        _c_(579294, _a_(579293, _c_(579292, _n_(579289, "Label", lambda: Label), _a_(579291, _n_(579290, "self", lambda: self), "edit_wind"), text = 'Name: '), "grid"), row = 0, column = 1)
        _l_(579295)
        name = _c_(579299, _n_(579296, "Entry", lambda: Entry), _a_(579298, _n_(579297, "self", lambda: self), "edit_wind"))
        _l_(579300)
        _c_(579303, _a_(579302, _n_(579301, "name", lambda: name), "grid"), row = 0, column = 2)
        _l_(579304)

        _c_(579322, _a_(579320, _c_(579319, _n_(579305, "Button", lambda: Button), _a_(579307, _n_(579306, "self", lambda: self), "edit_wind"), text = 'Search', command = lambda: _c_(579318, _a_(579309, _n_(579308, "self", lambda: self), "edit_records"), _c_(579312, _a_(579311, _n_(579310, "new_name", lambda: new_name), "get")), _n_(579313, "name", lambda: name), _c_(579316, _a_(579315, _n_(579314, "new_price", lambda: new_price), "get")), _n_(579317, "old_price", lambda: old_price))), "grid"), row = 4, column = 2, sticky = _n_(579321, "W", lambda: W))
        _l_(579323)

    def edit_records(self, name):
        _l_(579349)

        query = 'SELECT totalstock FROM stocks WHERE name = ? AND MovementID = ( SELECT max( MovementID ) FROM stocks)'
        _l_(579325)
        parameters = _n_(579326, "name", lambda: (name))
        _l_(579327)
        _c_(579332, _a_(579329, _n_(579328, "self", lambda: self), "run_query"), _n_(579330, "query", lambda: query), _n_(579331, "parameters", lambda: parameters))
        _l_(579333)
        _c_(579337, _a_(579336, _a_(579335, _n_(579334, "self", lambda: self), "edit_wind"), "destroy"))
        _l_(579338)
        _a_(579340, _n_(579339, "self", lambda: self), "message")['text'] = _c_(579343, _a_(579341, 'Total stock is {}', "format"), _n_(579342, "totalstock", lambda: totalstock))
        _l_(579344)
        _c_(579347, _a_(579346, _n_(579345, "self", lambda: self), "get_product"))
        _l_(579348)
if _n_(579351, "__name__", lambda: __name__) == '__main__':
    _l_(579363)

    window = _c_(579353, _n_(579352, "Tk", lambda: Tk))
    _l_(579354)
    application = _c_(579357, _n_(579355, "Main", lambda: Main), _n_(579356, "window", lambda: window))
    _l_(579358)
    _c_(579361, _a_(579360, _n_(579359, "window", lambda: window), "mainloop"))
    _l_(579362)