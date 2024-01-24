# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29311509/positional-argument-typeerror-python-tkinter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tkinter import *
    _l_(672746)

except ImportError:
    pass

class Search(_n_(672747, "Tk", lambda: Tk)):
    _l_(672871)

    def __init__(self):
        _l_(672856)

        _c_(672751, _a_(672749, _n_(672748, "Tk", lambda: Tk), "__init__"), _n_(672750, "self", lambda: self))
        _l_(672752)

        _c_(672757, _a_(672754, _n_(672753, "self", lambda: self), "bind"), "<Return>", _a_(672756, _n_(672755, "self", lambda: self), "search_button"))
        _l_(672758)

        _n_(672759, "self", lambda: self).search_bar = _c_(672762, _n_(672760, "Frame", lambda: Frame), _n_(672761, "self", lambda: self), bg="blue")
        _l_(672763)
        _c_(672769, _a_(672766, _a_(672765, _n_(672764, "self", lambda: self), "search_bar"), "pack"), side=_n_(672767, "TOP", lambda: TOP), fill=_n_(672768, "X", lambda: X))
        _l_(672770)
        _n_(672771, "self", lambda: self).index = _c_(672774, _n_(672772, "Frame", lambda: Frame), _n_(672773, "self", lambda: self), width=100)
        _l_(672775)
        _c_(672780, _a_(672778, _a_(672777, _n_(672776, "self", lambda: self), "index"), "pack"), side=_n_(672779, "LEFT", lambda: LEFT))
        _l_(672781)
        _n_(672782, "self", lambda: self).content = _c_(672785, _n_(672783, "Frame", lambda: Frame), _n_(672784, "self", lambda: self), bg="red")
        _l_(672786)
        _c_(672792, _a_(672789, _a_(672788, _n_(672787, "self", lambda: self), "content"), "pack"), side=_n_(672790, "LEFT", lambda: LEFT), fill=_n_(672791, "X", lambda: X))
        _l_(672793)
        _n_(672794, "self", lambda: self).status_bar = _c_(672797, _n_(672795, "Frame", lambda: Frame), _n_(672796, "self", lambda: self), bg="green")
        _l_(672798)
        _c_(672804, _a_(672801, _a_(672800, _n_(672799, "self", lambda: self), "status_bar"), "pack"), side=_n_(672802, "BOTTOM", lambda: BOTTOM), fill=_n_(672803, "X", lambda: X))
        _l_(672805)

        _n_(672806, "self", lambda: self).entry = _c_(672810, _n_(672807, "Entry", lambda: Entry), _a_(672809, _n_(672808, "self", lambda: self), "search_bar"))
        _l_(672811)
        _c_(672816, _a_(672814, _a_(672813, _n_(672812, "self", lambda: self), "entry"), "pack"), side=_n_(672815, "LEFT", lambda: LEFT), padx=4, pady=4)
        _l_(672817)
        _n_(672818, "self", lambda: self).search = _c_(672824, _n_(672819, "Button", lambda: Button), _a_(672821, _n_(672820, "self", lambda: self), "search_bar"), text="Search", command=_a_(672823, _n_(672822, "self", lambda: self), "search_button"))
        _l_(672825)
        _c_(672830, _a_(672828, _a_(672827, _n_(672826, "self", lambda: self), "search"), "pack"), side=_n_(672829, "LEFT", lambda: LEFT))
        _l_(672831)
        _n_(672832, "self", lambda: self).content = _c_(672836, _n_(672833, "Label", lambda: Label), _a_(672835, _n_(672834, "self", lambda: self), "content"), text="DUPA")
        _l_(672837)
        _c_(672842, _a_(672840, _a_(672839, _n_(672838, "self", lambda: self), "content"), "pack"), side=_n_(672841, "LEFT", lambda: LEFT))
        _l_(672843)
        _n_(672844, "self", lambda: self).status_bar = _c_(672848, _n_(672845, "Label", lambda: Label), _a_(672847, _n_(672846, "self", lambda: self), "status_bar"), text="DUPA")
        _l_(672849)
        _c_(672854, _a_(672852, _a_(672851, _n_(672850, "self", lambda: self), "status_bar"), "pack"), side=_n_(672853, "LEFT", lambda: LEFT))
        _l_(672855)

    def search_button(self):
        _l_(672870)

        _c_(672860, _a_(672859, _a_(672858, _n_(672857, "self", lambda: self), "entry"), "get"))
        _l_(672861)
        if _c_(672865, _a_(672864, _a_(672863, _n_(672862, "self", lambda: self), "entry"), "get")) == 'example1':
            _l_(672869)

            _c_(672867, _n_(672866, "print", lambda: print), "lorem ipsum")
            _l_(672868)