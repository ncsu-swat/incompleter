# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55538090/typeerror-index-takes-2-positional-arguments-but-3-were-given
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def calendar():
    _l_(566013)

    def print_sel():
        _l_(565989)

        _c_(565987, _a_(565982, _n_(565981, "dob", lambda: dob), "index"), _n_(565983, "INSERT", lambda: INSERT), _c_(565986, _a_(565985, _n_(565984, "cal", lambda: cal), "selection_get")))
        _l_(565988)

    top = _c_(565992, _n_(565990, "Toplevel", lambda: Toplevel), _n_(565991, "root", lambda: root))
    _l_(565993)
    _c_(565996, _a_(565995, _n_(565994, "top", lambda: top), "title"), "Select Registration Date")
    _l_(565997)

    cal = _c_(566000, _n_(565998, "Calendar", lambda: Calendar), _n_(565999, "top", lambda: top), font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2019, month=4, day=4)
    _l_(566001)

    _c_(566004, _a_(566003, _n_(566002, "cal", lambda: cal), "pack"), fill="both", expand=True)
    _l_(566005)

    _c_(566011, _a_(566010, _c_(566009, _n_(566006, "Button", lambda: Button), _n_(566007, "top", lambda: top), text="ok", command=_n_(566008, "print_sel", lambda: print_sel)), "pack"))
    _l_(566012)


dob=_c_(566016, _n_(566014, "Entry", lambda: Entry), _n_(566015, "Registration_Frame", lambda: Registration_Frame),style='TEntry')
_l_(566017)
_c_(566021, _a_(566019, _n_(566018, "dob", lambda: dob), "grid"), row=3,column=1,columnspan=2,sticky=_n_(566020, "NSEW", lambda: NSEW))
_l_(566022)

_c_(566028, _a_(566027, _c_(566026, _n_(566023, "Button", lambda: Button), _n_(566024, "Registration_Frame", lambda: Registration_Frame), text='Select',command=_n_(566025, "calendar", lambda: calendar),width=5,style='TButton'), "grid"), row=3,column=3)
_l_(566029)