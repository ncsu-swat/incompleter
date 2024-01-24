# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29835061/typeerror-type-str-doesnt-support-the-buffer-api-when-using-str-rstrip
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        from tkinter import ttk
        _l_(622737)

except ImportError:
        pass
try:
        from tkinter import *
        _l_(622739)

except ImportError:
        pass
try:
        import tkinter, imaplib,email
        _l_(622741)

except ImportError:
        pass
def signin(w,x,s):
        _l_(622836)

        tkgui = _c_(622744, _a_(622743, _n_(622742, "tkinter", lambda: tkinter), "Tk"))
        _l_(622745)
        _c_(622749, _a_(622747, _n_(622746, "tkgui", lambda: tkgui), "title"), 'Inbox %s'%_n_(622748, "w", lambda: w))
        _l_(622750)
        mail=_c_(622754, _a_(622752, _n_(622751, "imaplib", lambda: imaplib), "IMAP4_SSL"), ('%s'%_n_(622753, "s", lambda: s)),993)
        _l_(622755)
        _c_(622760, _a_(622757, _n_(622756, "mail", lambda: mail), "login"), ('%s'%_n_(622758, "w", lambda: w) ), ('%s'%_n_(622759, "x", lambda: x)))
        _l_(622761)
        _c_(622764, _a_(622763, _n_(622762, "mail", lambda: mail), "list"))
        _l_(622765)
        _c_(622768, _a_(622767, _n_(622766, "mail", lambda: mail), "select"), "INBOX")
        _l_(622769)
        result, data = _c_(622772, _a_(622771, _n_(622770, "mail", lambda: mail), "search"), None, "ALL")
        _l_(622773)
        ids = _n_(622774, "data", lambda: data)[0]
        _l_(622775)
        id_list = _c_(622778, _a_(622777, _n_(622776, "ids", lambda: ids), "split"))
        _l_(622779)
        tree = _c_(622783, _a_(622781, _n_(622780, "ttk", lambda: ttk), "Treeview"), _n_(622782, "tkgui", lambda: tkgui))
        _l_(622784)
        for i in _c_(622786, _n_(622785, "range", lambda: range), -1,0):
                _l_(622807)

                result, data = _c_(622791, _a_(622788, _n_(622787, "mail", lambda: mail), "fetch"), _n_(622789, "id_list", lambda: id_list)[_n_(622790, "i", lambda: i)], '(RFC822)')
                _l_(622792)
                raw_email = _n_(622793, "data", lambda: data)[0][1]
                _l_(622794)
                d = _c_(622798, _a_(622796, _n_(622795, "email", lambda: email), "message_from_bytes"), _n_(622797, "raw_email", lambda: raw_email))
                _l_(622799)
                _c_(622805, _a_(622801, _n_(622800, "tree", lambda: tree), "insert"), '',0,value=(_n_(622802, "d", lambda: d)['Date'],_n_(622803, "d", lambda: d)['From'],_n_(622804, "d", lambda: d)['Subject']))
                _l_(622806)
        _n_(622808, "tree", lambda: tree)['columns']=['Date','From','Subject']
        _l_(622809)
        r=_c_(622812, _a_(622811, _n_(622810, "raw_email", lambda: raw_email), "rstrip"), '\r\n')
        _l_(622813)
        _c_(622816, _n_(622814, "print", lambda: print), _n_(622815, "r", lambda: r))
        _l_(622817)
        for col in _n_(622818, "tree", lambda: tree)['columns']:
                _l_(622825)

                _c_(622823, _a_(622820, _n_(622819, "tree", lambda: tree), "heading"), _n_(622821, "col", lambda: col),text=_n_(622822, "col", lambda: col))
                _l_(622824)
        _c_(622830, _a_(622827, _n_(622826, "tree", lambda: tree), "pack"), side=_n_(622828, "TOP", lambda: TOP),fill=_n_(622829, "BOTH", lambda: BOTH),expand=1)
        _l_(622831)
        _c_(622834, _a_(622833, _n_(622832, "tkgui", lambda: tkgui), "mainloop"))
        _l_(622835)