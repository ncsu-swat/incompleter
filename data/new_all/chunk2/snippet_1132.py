# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51141597/django-typeerror-got-multiple-values-for-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class LocationManager(_a_(451828, _n_(451827, "models", lambda: models), "Manager")):
    _l_(451889)

    def exist(city, state):
        _l_(451838)

        if _c_(451834, _a_(451831, _a_(451830, _n_(451829, "self", lambda: self), "queryset"), "get"), city=_n_(451832, "city", lambda: city), state=_n_(451833, "state", lambda: state)):
            _l_(451836)

            aux = True
            _l_(451835)
            return aux
        aux = False
        _l_(451837)
        return aux

    def create_new(self, ip_address, city_data):
        _l_(451888)

        location = _c_(451841, _a_(451840, _n_(451839, "self", lambda: self), "model"))
        _l_(451842)
        if _n_(451843, "ip_address", lambda: ip_address) is not None:
            _l_(451887)

            if _n_(451844, "city_data", lambda: city_data):
                _l_(451886)

                city = _n_(451845, "city_data", lambda: city_data)['city']
                _l_(451846)
                state = _n_(451847, "city_data", lambda: city_data)['region']
                _l_(451848)
                if not _c_(451853, _a_(451850, _n_(451849, "self", lambda: self), "exist"), city=_n_(451851, "city", lambda: city), state=_n_(451852, "state", lambda: state)):
                    _l_(451885)

                    _n_(451854, "location", lambda: location).city_data = _n_(451855, "city_data", lambda: city_data)
                    _l_(451856)
                    _n_(451857, "location", lambda: location).city = _n_(451858, "city", lambda: city)
                    _l_(451859)
                    _n_(451860, "location", lambda: location).state = _n_(451861, "state", lambda: state)
                    _l_(451862)
                    _n_(451863, "location", lambda: location).country = _n_(451864, "city_data", lambda: city_data)['country_name']
                    _l_(451865)
                    _n_(451866, "location", lambda: location).latitude = _n_(451867, "city_data", lambda: city_data)['latitude']
                    _l_(451868)
                    _n_(451869, "location", lambda: location).longitude = _n_(451870, "city_data", lambda: city_data)['longitude']
                    _l_(451871)
                    _c_(451874, _a_(451873, _n_(451872, "location", lambda: location), "save"))
                    _l_(451875)
                    aux = _n_(451876, "location", lambda: location)
                    _l_(451877)
                    return aux
                else:
                    aux = _c_(451883, _a_(451880, _a_(451879, _n_(451878, "Location", lambda: Location), "objects"), "get"), city=_n_(451881, "city", lambda: city), state=_n_(451882, "state", lambda: state))
                    _l_(451884)
                    return aux

class Location(_a_(451891, _n_(451890, "models", lambda: models), "Model")):
    _l_(451921)

    city_data   = _c_(451893, _a_(451892, models, "TextField"), null=True, blank=True)
    _l_(451894)
    city        = _c_(451896, _a_(451895, models, "CharField"), max_length=120, null=True, blank=True)
    _l_(451897)
    state       = _c_(451899, _a_(451898, models, "CharField"), max_length=2, null=True, blank=True)
    _l_(451900)
    country     = _c_(451902, _a_(451901, models, "CharField"), max_length=20, null=True, blank=True)
    _l_(451903)
    latitude    = _c_(451905, _a_(451904, models, "FloatField"))
    _l_(451906)
    longitude   = _c_(451908, _a_(451907, models, "FloatField"))
    _l_(451909)

    objects = _c_(451911, _n_(451910, "LocationManager", lambda: LocationManager))
    _l_(451912)

    def __str__(self):
        _l_(451920)

        aux = _c_(451918, _a_(451913, '{}, {}', "format"), _a_(451915, _n_(451914, "self", lambda: self), "city"), _a_(451917, _n_(451916, "self", lambda: self), "state"))
        _l_(451919)
        return aux