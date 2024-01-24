# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59848259/typeerror-int-object-is-not-iterable-serializer-django-serializer-for-one-to
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Sector(_a_(473652, _n_(473651, "models", lambda: models), "Model")):
    _l_(473667)

    sector_name = _c_(473654, _a_(473653, models, "CharField"), max_length=255, null=False)
    _l_(473655)
    sector_desc = _c_(473657, _a_(473656, models, "CharField"), max_length=1024, null=False)
    _l_(473658)

    def __set__(self):
        _l_(473666)

        aux = _c_(473664, _a_(473659, "{} - {}", "format"), _a_(473661, _n_(473660, "self", lambda: self), "sector_name"), _a_(473663, _n_(473662, "self", lambda: self), "sector_desc"))
        _l_(473665)
        return aux


class TrailCompany(_a_(473669, _n_(473668, "models", lambda: models), "Model")):
    _l_(473691)

    sector = _c_(473673, _a_(473670, models, "ForeignKey"), _n_(473671, "Sector", lambda: Sector), on_delete=_a_(473672, models, "CASCADE"), related_name="sector_id")
    _l_(473674)
    comp_name = _c_(473676, _a_(473675, models, "CharField"), max_length=255, null=False)
    _l_(473677)
    comp_desc = _c_(473679, _a_(473678, models, "CharField"), max_length=1024, null=False)
    _l_(473680)

    def __set__(self):
        _l_(473690)

        aux = _c_(473688, _a_(473681, "{} - {}", "format"), _a_(473683, _n_(473682, "self", lambda: self), "sector"), _a_(473685, _n_(473684, "self", lambda: self), "comp_name"), _a_(473687, _n_(473686, "self", lambda: self), "comp_desc"))
        _l_(473689)
        return aux


class Trail(_a_(473693, _n_(473692, "models", lambda: models), "Model")):
    _l_(473722)

    company = _c_(473697, _a_(473694, models, "ForeignKey"), _n_(473695, "TrailCompany", lambda: TrailCompany), on_delete=_a_(473696, models, "CASCADE"), related_name="company_id")
    _l_(473698)
    trail_id = _c_(473700, _a_(473699, models, "CharField"), max_length=255, null=False)
    _l_(473701)
    tri = _c_(473703, _a_(473702, models, "CharField"), max_length=255, null=False)
    _l_(473704)
    exp_pdufa = _c_(473706, _a_(473705, models, "CharField"), max_length=255, null=False)
    _l_(473707)

    def __set__(self):
        _l_(473721)

        aux = _c_(473719, _a_(473708, "{} - {}", "format"), _a_(473710, _n_(473709, "self", lambda: self), "company"), _a_(473712, _n_(473711, "self", lambda: self), "exp_pdufa"), _a_(473714, _n_(473713, "self", lambda: self), "trail_id"), _a_(473716, _n_(473715, "self", lambda: self), "tri"), _a_(473718, _n_(473717, "self", lambda: self), "exp_pdufa"))
        _l_(473720)
        return aux